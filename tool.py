import time


def countdown(seconds):
    while seconds > 0:  # 循环直到秒数为0
        print(seconds, end='')  # 打印秒数，并将光标移动到行首
        time.sleep(1)  # 暂停1秒
        print(end="\r")
        seconds -= 1  # 秒数减1
