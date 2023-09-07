message = "加载预设 "
if message.startswith("加载预设 "):
    action = message[5:]
    if action is None:
        print('1')
    elif action == '':
        print('2')

