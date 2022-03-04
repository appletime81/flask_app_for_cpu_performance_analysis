import os
from flask import Flask, render_template, flash, request, redirect, url_for
from analysis_main import *
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'upload_folder'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'


@app.route('/', methods=['GET', 'POST'])
def plot_func():
    file_name = '3-1-1/3-1-32.txt'
    option = 'task_profile_info_ss_nrt_task'
    column_name = 'AVG_CYCLES'

    # --------------------------------------- 分析log ---------------------------------------
    condition_list = condition_option(option)
    record_list, event_list = get_all_events(file_name, condition_list)
    event_dict = genTaskDict(event_list)
    event_dict = statsEvent(event_list, record_list, event_dict, column_name)

    # --------------------------------------- 畫圖表 ---------------------------------------
    color_dict = gen_color_dict()
    fig = plot_bar(event_dict, color_dict, file_name, option, column_name)

    # 序列化
    fig_js = fig.to_json()
    return render_template('index.html', title='Home', context=fig_js)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/')
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run()
