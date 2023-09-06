from revChatGPT.V1 import Chatbot
from wxRobot import WeChatRobot

auth_config = {
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJsaWRpYW56aG9uZzAwQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlfSwiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS9hdXRoIjp7InVzZXJfaWQiOiJ1c2VyLTNqcnhXOG04RzNDanJHUEs4OGQ4MWdRVCJ9LCJpc3MiOiJodHRwczovL2F1dGgwLm9wZW5haS5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDE2MjMzNTE2MDc2OTY1NTMwNDQiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLm9wZW5haS5hdXRoMGFwcC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjkzODk5MjE3LCJleHAiOjE2OTUxMDg4MTcsImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb3JnYW5pemF0aW9uLndyaXRlIG9mZmxpbmVfYWNjZXNzIn0.Ng4ipvL9LxxT67gvRrzjwhtBQnvAY6tmt0qyUgv-XHnRM1hnbfvFya6As2abd543xhyBkzmy2Oc-4bHogszf3UYcNmheyup6Dlk-JBb2wvgNJTuYpm_rA_ziCUkJoQGu8nuD09E-HvFgbq0qAoAOv7QtAdV8kJuFnoluNxsvncsGDsw2CvKH_IcETxDZRosuJvFphYxDphaRB8UyAxsJQjN-QUjdoEueFhnpk43H8xpXWOiaj0eH71i3_cgpIsNmLTy21ElQKzmeYgRixNeE-FPTmMe9fiqevZZu8U5beeUHFWFmsdLbjpw0PSSpX7hDKQaguAtd5De9i-O83CgZRw"}

assistant_dict = {}

prompt_dict = {
    'default': '让我们进入角色扮演吧。你现在是一个群聊机器人，需要根据用户输入的信息，进行群助手消息的回复，'
               '你回复的消息内容不宜过长，一般可控制在100字以内，说话应该更符合人类的口吻，伴有诙谐幽默的语气和友善的态度。'
               '现在开启群聊小助手，请回复一句简短幽默的开头欢迎语'
}


class Assistant:
    def __init__(self, uuid: str):
        self.chatbot: Chatbot = Chatbot(config=auth_config)
        self.uuid: str = uuid
        self.conversation_id = self.chatbot.conversation_id
        self.type = self._type()  # 1表示私聊，2表示群聊
        self.status = self._is_open()  # 如果是群，默认关闭，如果是私聊，默认开启

    # 如果是群，默认关闭，如果是私聊，默认开启
    def _is_open(self) -> bool:
        if self.type == 1:
            return True
        else:
            return False

    def _type(self) -> int:
        # 0表示未知，1表示私聊，2表示群聊
        if self.uuid.endswith("@chatroom"):
            return 2
        else:
            return 1

    # 发送信息
    def chat(self, prompt):
        response = ""
        for data in self.chatbot.ask(prompt, conversation_id=self.conversation_id):
            response = data["message"]
        return response


def text_handle(uuid, message) -> str:
    print('----------文本消息----------')
    print('sender:', uuid)
    print('message:', message)

    # 先对管理员命令处理

    # 如果这个群或者联系人从未出现过
    if uuid not in assistant_dict:
        # 创建新助手
        assistant = Assistant(uuid)
        assistant_dict[uuid] = assistant  # 加入助手列表中

    # 已知对话
    assistant: Assistant = assistant_dict[uuid]
    if need_response(assistant.status, message):
        response = assistant.chat(message)
        return response


def need_response(status, message: str):
    if status and message.endswith(' '):
        return True
    else:
        return False
