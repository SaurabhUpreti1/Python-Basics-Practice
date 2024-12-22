import time
import multiprocessing


def square(numbers):
    for i in numbers:
        print(f"{i * i} is square of {i}, ")
        time.sleep(5)


def cube(numbers):
    for i in numbers:
        print(f"{i ** 3} is cube of {i}, ")


if __name__ == '__main__':
    array = [1, 2, 34, 5]
    t1 = multiprocessing.Process(target=square, args=(array,))
    t2 = multiprocessing.Process(target=cube, args=(array,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("program ends")
