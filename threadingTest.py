import threading
import time

# def threadTest1():
#     for i in range(10):
#         print("陳跑了",i,"次")
#         time.sleep(1)

# def threadTest2():
#     for i in range(10):
#         print("水跑了",i,"次")
#         time.sleep(3)

#建立執行續 
# t1 = threading.Thread(target= threadTest1)
# t2 = threading.Thread(target= threadTest2)

#執行續啟用 
# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("結束了")

# 使用class去定義thread

class threadTeat1(object):
    def __init__(self):
        self.threadJob()

    def job(self, name):
        print("我是" + name)

    def threadJob(self):
        self.threads = []
        t = threading.Thread(target=self.job, args=("Raymond",))
        self.threads.append(t)

    def threadStart(self):
        for t in self.threads:
            t.start()

        for t in self.threads:
            t.join()

        self.threadJob()

test1 = threadTeat1()
test1.threadStart()