from revChatGPT.V1 import Chatbot

auth_config = {
    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJsaWRpYW56aG9uZzAwQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlfSwiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS9hdXRoIjp7InVzZXJfaWQiOiJ1c2VyLTNqcnhXOG04RzNDanJHUEs4OGQ4MWdRVCJ9LCJpc3MiOiJodHRwczovL2F1dGgwLm9wZW5haS5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDE2MjMzNTE2MDc2OTY1NTMwNDQiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLm9wZW5haS5hdXRoMGFwcC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjkzODk5MjE3LCJleHAiOjE2OTUxMDg4MTcsImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb3JnYW5pemF0aW9uLndyaXRlIG9mZmxpbmVfYWNjZXNzIn0.Ng4ipvL9LxxT67gvRrzjwhtBQnvAY6tmt0qyUgv-XHnRM1hnbfvFya6As2abd543xhyBkzmy2Oc-4bHogszf3UYcNmheyup6Dlk-JBb2wvgNJTuYpm_rA_ziCUkJoQGu8nuD09E-HvFgbq0qAoAOv7QtAdV8kJuFnoluNxsvncsGDsw2CvKH_IcETxDZRosuJvFphYxDphaRB8UyAxsJQjN-QUjdoEueFhnpk43H8xpXWOiaj0eH71i3_cgpIsNmLTy21ElQKzmeYgRixNeE-FPTmMe9fiqevZZu8U5beeUHFWFmsdLbjpw0PSSpX7hDKQaguAtd5De9i-O83CgZRw"}

chatbot = Chatbot(config=auth_config)


def chat(prompt):
    response = ""
    for data in chatbot.ask(prompt):
        response = data["message"]
    return response


chat("你好\n你是谁")
