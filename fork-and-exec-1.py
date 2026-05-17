#!/usr/bin/python3
import os, sys

pid = os.fork()
if pid==0:
    print("자식 프로세스={}, 부모 프로세스={}".format(os.getpid(), os.getppid()))
    os.execve("/bin/echo", ["echo", "pid={}에서 안녕". format(os.getpid())],{})
    exit()
elif pid>0:
    print("부모 프로세스: pid={}, 자식 프로세스의 pid={}".format(os.getpid(), pid))
    exit()

sys.exit()
