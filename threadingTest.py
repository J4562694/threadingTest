import threading
import time

def threadTest1():
    for i in range(10):
        print("陳跑了",i,"次")
        time.sleep(1)

def threadTest2():
    for i in range(10):
        print("水跑了",i,"次")
        time.sleep(3)

#建立執行續 
t1 = threading.Thread(target= threadTest1)
t2 = threading.Thread(target= threadTest2)

#執行續啟用 
t1.start()
t2.start()

t1.join()
t2.join()

print("結束了")
