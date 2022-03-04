import pandas as pd

from tokenize import String
from typing import List
from datetime import datetime


def genDataDict(record_list: List, event_list: List, option: String, ue_nums: int, pool_nums: int, ue_per_tti: int):
    column_names = ['EVT_NAME', 'UE_NUMS', 'POOL_NUMS', 'UR_PER_TTI', 'IN_QUEUE', 'RT', 'NRT', 'NOT_IN_QUEUE',
                    'MIN_CYCLES',
                    'MAX_CYCLES', 'AVG_CYCLES', 'NUM_TIMES']
    data_dict = dict([(column_name, list()) for column_name in column_names])
    in_queue = 'False'
    not_in_queue = 'True'
    rt = 'True'
    nrt = 'False'
    if '_queue_' in option:
        in_queue = 'True'
        not_in_queue = 'False'
    if 'nrt' in option:
        rt = 'False'
        nrt = 'True'

    for record in record_list:
        if record != '##########':
            data_dict['EVT_NAME'].append(record[1])
            data_dict['UE_NUMS'].append(ue_nums)
            data_dict['POOL_NUMS'].append(pool_nums)
            data_dict['UR_PER_TTI'].append(ue_per_tti)
            data_dict['IN_QUEUE'].append(in_queue)
            data_dict['NOT_IN_QUEUE'].append(not_in_queue)
            data_dict['MIN_CYCLES'].append(record[2])
            data_dict['MAX_CYCLES'].append(record[3])
            data_dict['AVG_CYCLES'].append(record[4])
            if '_queue_' in option:
                data_dict['NUM_TIMES'].append(0)
            else:
                data_dict['NUM_TIMES'].append(record[6])

            if '_rt_' in option:
                data_dict['RT'].append('True')
                data_dict['NRT'].append('False')
            else:
                data_dict['RT'].append('False')
                data_dict['NRT'].append('True')

    print(data_dict)
    for key, val in data_dict.items():
        print(key, len(val))
    return data_dict


def createExcelReport(record_list: List, event_list: List, option: String, ue_nums: int, pool_nums: int,
                      ue_per_tti: int):

    data_dict = genDataDict(record_list, event_list, option, ue_nums, pool_nums, ue_per_tti)
    df = pd.DataFrame(data_dict)
    df.to_csv(f'{option}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv', index=False)
