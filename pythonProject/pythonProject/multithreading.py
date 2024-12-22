import time
import threading
def square(numbers):
    for i in numbers:
        print(f"{i*i} is square of {i}, ")
        time.sleep(5)
def cube(numbers):
    for i in numbers:
        print(f"{i **3} is cube of {i}, ")
array=[1,2,34,5]
t1=threading.Thread(target=square,args=(array,))
t2=threading.Thread(target=cube,args=(array,))
t1.start()
t2.start()
t1.join()
t2.join()
print("program ends")
print("finished")
