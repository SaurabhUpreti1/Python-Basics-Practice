"""x=open("demo.txt","x")
x.close()"""
x=open("demo.txt","w")
x.write("saurabh")
x.close()
y=open("demo.txt")
print(y.read())
y.close()
z=open("demo.txt","a")
z.write(" upreti")
with open("demo.txt","a") as o:
    o.write(" hey")