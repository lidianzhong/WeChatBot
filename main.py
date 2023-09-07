import asyncio
import json
import time
import chatgpt
import wxRobot
import tool


class MsgHandle(wxRobot.WeChatEventSink):

    def __init__(self, robot):
        self.robot = robot

    def OnGetMessageEvent(self, msg):
        msg = json.loads(msg[0])
        print(msg)

        is_send_msg = msg['isSendMsg']
        message = msg['message']
        self_id = msg['self']  # 自己的微信id
        sender = msg['sender']  # 消息的发送者id
        type_msg = msg['type']  # 消息的类型
        wxid = msg['wxid']  # 消息的发送者id

        res_msg = None

        # 如果是文本信息
        if type_msg == 1:
            res_msg = chatgpt.text_handle(sender, is_send_msg, message)

        if res_msg is not None:
            robot.SendText(sender, res_msg)


robot: wxRobot.WeChatRobot = wxRobot.start_wechat()
robot_pid = robot.pid

print("等待微信启动.....")
tool.countdown(10)

status = robot.StartService()
if status != 0:
    print("StartService服务失败")
    exit(-1)

status = robot.StartReceiveMessage()
if status != 0:
    print("StartReceiveMessage服务失败")
    exit(-1)

msg_handle = MsgHandle(robot)
wxRobot.register_msg_event(robot_pid, msg_handle)

while True:
    pass
