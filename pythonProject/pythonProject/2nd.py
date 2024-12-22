mylist = ["hello", "hey"]
mylist1 = mylist * 2
print(mylist1)
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1
list1 = ["world", "hi"]
list2 = []
for i in range(0, len(list1)):
    if "w" in list1[i]:
        list2.append(list1[i])
print(list2)
#list sorting
list = ["CApital", "cat", "banana", "Apple", "apple"]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list4 = [1, 2, "saurabh"]
print(list4)
#tuple
tuple = ("saurabh", 1, "upreti")
tuple1 = ("hey", 1)
tuple1 = tuple + tuple1
print(tuple1.count(1))
#set
set1 = {"saurabh", "upreti", "saurabh"}  #cannot support duplicate values
print(set1)
#file_handling
x = open("file_handling.txt", "r")
print(x.read(5))
x.close()
'''y = open("file_handling.txt", "w")
z = "hello brother"
y.write(z)
y.close()'''
b = open("file_handling.txt")
print(b.read())
b.close()
c=open("file_handling.txt")
d=c.read()
if "hello" in d :
    print("yes")
else:
    print("no")