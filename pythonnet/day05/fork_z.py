import os
from time import sleep

pid = os.fork()

if pid == 0:
    print("Child PID:",os.getpid())
    os._exit(0)

else:
    print("Parent proocess,长点心吧....")
    while True:
        pass