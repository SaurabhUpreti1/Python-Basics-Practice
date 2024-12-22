import random
def game():
    score=random.randint(1, 100)
    with open("High_Score.txt") as a:
        high=a.read()
        if(high!=""):
            high=int(high)
        else:
            high=0

    print("Game starts...")
    print(f"your score is : {score}")
    if(score>high):
        with open("High_Score.txt","w") as a:
            a.write(str(score))
    return score
game()

