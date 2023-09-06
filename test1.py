import json
import chatgpt


def OnGetMessageEvent(msg):
    is_send_msg = msg['isSendMsg']
    message = msg['message']
    self_id = msg['self']  # 自己的微信id
    sender = msg['sender']  # 消息的发送者id
    type_msg = msg['type']  # 消息的类型
    wxid = msg['wxid']  # 消息的发送者id

    res_msg = None

    # 如果是文本信息
    if type_msg == 'text':
        res_msg = chatgpt.text_handle(sender, message)

    if res_msg is not None:
        SendText(sender, res_msg)


def SendText(sender, res_msg):
    print("sender:", sender, "res_msg:", res_msg)


msg1 = {'extrainfo': '<msgsource>\n\t<signature>v1_sobSEEnb</signature>\n</msgsource>\n', 'filepath': '',
       'isSendByPhone': 1, 'isSendMsg': 1, 'message': '1+3=? ', 'msgid': 8997047107752004202, 'pid': 32,
       'self': 'huaxxxx', 'sender': 'wxid_123456@chatroom', 'sign': 'c926ab68d2df643bac8c0bd776b0a7ee', 'thumb_path': '',
       'time': '2022-10-12 09:41:55', 'timestamp': 1665564115, 'type': 'text', 'wxid': 'wxid_xxxxxxxxx'}

msg2 = {'extrainfo': '<msgsource>\n\t<signature>v1_sobSEEnb</signature>\n</msgsource>\n', 'filepath': '',
       'isSendByPhone': 1, 'isSendMsg': 1, 'message': '2+3=? ', 'msgid': 8997047107752004202, 'pid': 32,
       'self': 'huaxxxx', 'sender': 'wxid_654321@chatroom', 'sign': 'c926ab68d2df643bac8c0bd776b0a7ee', 'thumb_path': '',
       'time': '2022-10-12 09:41:55', 'timestamp': 1665564115, 'type': 'text', 'wxid': 'wxid_xxxxxxxxx'}

msg3 = {'extrainfo': '<msgsource>\n\t<signature>v1_sobSEEnb</signature>\n</msgsource>\n', 'filepath': '',
       'isSendByPhone': 1, 'isSendMsg': 1, 'message': '3+3=? ', 'msgid': 8997047107752004202, 'pid': 32,
       'self': 'huaxxxx', 'sender': 'wxid_123456', 'sign': 'c926ab68d2df643bac8c0bd776b0a7ee', 'thumb_path': '',
       'time': '2022-10-12 09:41:55', 'timestamp': 1665564115, 'type': 'text', 'wxid': 'wxid_xxxxxxxxx'}
OnGetMessageEvent(msg=msg1)
OnGetMessageEvent(msg=msg2)
OnGetMessageEvent(msg=msg3)