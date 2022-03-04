from pprint import pprint
from utils.gen_random_color import gen_random_color

events_text = """EVT_COMMON_UE_ACK_INDICATION
EVT_CTF_CONFIG_REQUEST
EVT_KW_AMUL_STA_PROH_TIMER
EVT_KW_UMUL_REASSEMBLE_TIMER
EVT_L1_MSG_INDICATION
EVT_RGR_LVL1_CCCH_DATA_REQUEST
EVT_RGR_LVL1_CONFIG_REQUEST
EVT_RGR_LVL1_SI_CONFIG_REQUEST
EVT_RGR_LVL2_CONFIG_REQUEST
EVT_TFU_CRC_INDICATION
EVT_TFU_RA_REQUEST_INDICATION
EVT_UDX_STA_PHBT_START_TIMER
EVT_APP_LCL_CELL_ADD_REQ
EVT_APP_LCL_CELL_ADD_RSP
EVT_APP_UE_RRC_RECONFIG_DELIVERY_INDICATION
EVT_CKW_UL_CONFIG_REQUEST
EVT_CTF_CONFIG_CONFIRM
EVT_EGTP_ADD_TUNNEL_REQUEST
EVT_EGTP_ADD_TUNNEL_RESPONSE
EVT_EGTP_INIT_REQUEST
EVT_EGTP_TTI_INDICATION
EVT_F1AP_MGMT_MSG_RX
EVT_F1AP_MGMT_MSG_TX
EVT_F1AP_UE_ID_REQUEST
EVT_F1AP_UE_ID_RESPONSE
EVT_F1AP_UE_MSG_RX
EVT_F1AP_UE_MSG_TX
EVT_KWU_DATA_INDICATION
EVT_KWU_DATA_REQUEST
EVT_NRUP_ADD_RAB_REQUEST
EVT_NRUP_ADD_RAB_RESPONSE
EVT_NRUP_EGTPU_DATA_INDICATION
EVT_OAM_CELL_CONFIG_REQUEST
EVT_OAM_DU_CONFIG_REQUEST
EVT_RGR_LVL1_CCCH_DATA_INDICATION
EVT_RGR_LVL1_CONFIG_CONFIRM
EVT_RGR_LVL1_SI_CONFIG_CONFIRM
EVT_RGR_LVL1_TTI_INDICATION
EVT_RGR_LVL2_CONFIG_CONFIRM
EVT_RLC_FLW_CTRL_INFO_INDICATION
EVT_RLC_REQ_FLW_CTRL_INFO
EVT_RLC_UE_CONFIG_CONFIRM
EVT_RRM_CELL_ADD_CONFIRM
EVT_RRM_CELL_ADD_REQUEST
EVT_RRM_UE_ADMIT_CONFIRM
EVT_RRM_UE_ADMIT_REQUEST
EVT_RRM_UE_RECONFIG_REQUEST
EVT_RRM_UE_RECONFIG_RESPONSE
EVT_SCTP_ASSOC_STATUS
EVT_SCTP_CONFIG_REQUEST
EVT_SCTP_CONFIG_RESPONSE
EVT_SCTP_USER_PAYLOAD_INDICATION
EVT_SCTP_USER_PAYLOAD_REQUEST
EVT_TIMER_TICK_INDICATION
EVT_UDX_CONFIG_CONFIRM
EVT_UDX_CONFIG_REQUEST
EVT_UDX_DL_CLEANUP_MEM
EVT_UDX_STA_PDU_REQUEST
EVT_UDX_STA_UPD_REQUEST
"""


def gen_color_dict():
    color_dict = dict()
    temp_string = ''
    color_list = gen_random_color()
    i = 0
    color_list_idx = 1
    for char in events_text:
        temp_string += char
        if char == '\n':
            if temp_string not in color_dict:
                color_dict[temp_string.strip()] = color_list[color_list_idx]
                color_list_idx += 1
            temp_string = ''

    return color_dict


if __name__ == '__main__':
    color_dict = gen_color_dict()
    pprint(color_dict)