import random

# 1-snake,2-water,3-gun
computer = random.choice([1, 2, 3])
user = input("enter your choice:")
dict = {1: "s", 2: "w", 3: "g"}
reverse_dict = {"s": 1, "w": 2, "g": 3}
you = reverse_dict[user]
print(f"computer chooses {dict[computer]} and you chooses {user}")
if (computer == you):
    print("its draw")
else:
    if (computer == 1 and you == 2):
        print("You Lose")
    elif (computer == 1 and you == 3):
        print("You Won")
    elif (computer == 2 and you == 1):
        print("You Won")
    elif (computer == 2 and you == 3):
        print("You Lose")
    elif (computer == 3 and you == 1):
        print("You Lose")
    elif (computer == 3 and you == 2):
        print("You Won")
