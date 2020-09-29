'''
linux/unix/mac下运行

'''
import os

pid = os.fork()


if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("The new process")
else:
    print("The old process")

print("fork test over")
