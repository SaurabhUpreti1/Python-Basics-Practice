def time_taken(fx):
    def mfx(*args,**kwargs):
        print("function starts")
        fx(*args,**kwargs)
        print("function ends")
    return mfx
@time_taken
def calc_square(numbers):
    square=[i*i for i in numbers]
    print (square)
@time_taken
def calc_cube(numbers):
    cube=[i**3 for i in numbers]
    print(cube)
@time_taken
def greet():
    print ("hello world")
array=range(1,6)
calc_square(array)
calc_cube(array)
greet()