import time

def gt():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

gt()