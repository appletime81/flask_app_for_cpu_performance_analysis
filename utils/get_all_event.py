import re
from tokenize import String
from typing import List


def condition_option(opt_name: String):
    condition_dict = {
        'task_profile_info_ss_rt_task': ['TASK PROFILE INFO', 'SS_RT_TASK', 'SS_NRT_TASK'],
        'task_profile_info_ss_nrt_task': ['TASK PROFILE INFO', 'SS_NRT_TASK', 'QUEUE PROFILE INFO'],
        'queue_profile_info_ss_rt_task': ['QUEUE PROFILE INFO', 'SS_RT_TASK', 'SS_NRT_TASK'],
        'queue_profile_info_ss_nrt_task': ['QUEUE PROFILE INFO', 'SS_NRT_TASK']
    }
    return condition_dict.get(opt_name)


def get_all_events(fileName: String, condtion_list: List):
    # -------------------------declare vars-------------------------
    with open(fileName, 'r') as f:
        lines = f.readlines()
    event_list = list()
    ss_rt_or_nrt_flag = False
    start_record_flag = False
    record_list = list()
    n = len(lines)  # lines' length
    # --------------------------------------------------------------
    """
    1. get ss rt task from task profile info part
        - Condition 1:
            * String: 'TASK PROFILE INFO'
            * Bool Value: start_flag_record: True
        - Condition 2:
            * String: 'SS_RT_TASK'
            * Bool Value: ss_rt_or_nrt_flag: True
        - Condition 3:
            * String: 'SS_NRT_TASK'
            * Bool Value:  start_record_flag: False
                           ss_rt_or_nrt_flag: False
    2. get ss nrt task from task profile info part
        - Condition 1:
            * String: 'TASK PROFILE INFO'
            * Bool Value: start_flag_record: True
        - Condition 2:
            * String: 'SS_NRT_TASK'
            * Bool Value: ss_rt_or_nrt_flag: True
        - Condition 3:
            * String: 'QUEUE PROFILE INFO'
            * Bool Value:  start_record_flag: False
                           ss_rt_or_nrt_flag: False
    3. get ss rt task from queue profile info part
        - Condition 1:
            * String: 'QUEUE PROFILE INFO'
            * Bool Value: start_flag_record: True
        - Condition 2:
            * String: 'SS_RT_TASK'
            * Bool Value: ss_rt_or_nrt_flag: True
        - Condition 3:
            * String: 'SS_NRT_TASK'
            * Bool Value:  start_record_flag: False
                           ss_rt_or_nrt_flag: False
    4. get ss nrt task from queue profile info part
        - Condition 1:
            * String: 'QUEUE PROFILE INFO'
            * Bool Value: start_flag_record: True
        - Condition 2:
            * String: 'SS_NRT_TASK'
            * Bool Value: ss_rt_or_nrt_flag: True
        - Condition 3:
            * text1 = 'gnb_du_1           | 311'
            * text2 = 'gnb_cu_1           | [17/02/2022 10:09:16.573696][SCTP][ERR][ngp_inet.cpp:208]SCTP Socket Bind Failed'
            * re.match method: re.findall(r'gnb_du_1           \| \d+', text1) or 
                               'gnb_cu_1' in text2
            * Bool Value:  start_record_flag: False
                           ss_rt_or_nrt_flag: False
    """

    start_record_flag_index = None
    ss_rt_or_nrt_flag_index = None

    for i in range(n):
        if condtion_list[0] in lines[i]:  # Condition1
            start_record_flag = True
            start_record_flag_index = i
        if condtion_list[1] in lines[i]:  # Condition2
            ss_rt_or_nrt_flag = True
            ss_rt_or_nrt_flag_index = i
        try:
            index_condition = start_record_flag_index < ss_rt_or_nrt_flag_index
        except:
            pass

        if len(condtion_list) == 3:
            if condtion_list[2] in lines[i]:  # Condition3
                if ss_rt_or_nrt_flag and start_record_flag:
                    record_list.append('##########')
                    start_record_flag = False
                    ss_rt_or_nrt_flag = False
        elif len(condtion_list) == 2:
            try:
                if re.findall(r'gnb_du_1           \| \d+', lines[i + 1]) and len(
                        lines[i + 1].split(" ")) == 13:  # Condition3
                    if ss_rt_or_nrt_flag and start_record_flag and index_condition:
                        record_list.append('##########')
                        start_record_flag = False
                        ss_rt_or_nrt_flag = False
                elif 'gnb_cu_1' in lines[i + 1]:
                    if ss_rt_or_nrt_flag and start_record_flag and index_condition:
                        record_list.append('##########')
                        start_record_flag = False
                        ss_rt_or_nrt_flag = False
            except IndexError:
                pass

        if ss_rt_or_nrt_flag and start_record_flag and index_condition:
            if 'EVT_' in lines[i]:
                temp_line = lines[i].replace(' ', '_')
                temp_line_list = temp_line.split('_')
                temp_line_list = [element for element in temp_line_list if element != '']
                if condtion_list[0] == 'QUEUE PROFILE INFO':
                    temp_line_list = ['_'.join(temp_line_list[:4])] + ['_'.join(temp_line_list[4:-4])] + temp_line_list[-4:]
                else:
                    temp_line_list = ['_'.join(temp_line_list[:4])] + ['_'.join(temp_line_list[4:-5])] + temp_line_list[-5:]
                record_list.append(temp_line_list)
                event_list.append(temp_line_list[1])

    event_list = sorted(list(set(event_list)), reverse=True)
    return record_list, event_list
