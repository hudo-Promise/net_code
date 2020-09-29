import os

print("---------------")  # 只打印一条

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    print("Child process")
else:
    print("Parent process")
