# def saurabh():
#     yield "saurabh"
#     yield "Upreti"
#     yield 1
#     yield 2
# c=saurabh()
# print(next(c))
# print(next(c))
# print(next(c))
# ctrl+/ to comment out things
def fibo(n):
    if(n==0 or n==1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("enter till you want fibo series"))
for i in range(n):
    print(fibo(i))

set ={1,2,2,3,4}
print(set)
even={i for i in set if i%2==0}
print(even)
print("finshed")
#lambda function just for practice
x=lambda a,b,c:a*b-c
print (x(1,5,3))
