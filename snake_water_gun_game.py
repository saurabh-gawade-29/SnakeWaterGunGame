import random

def gameWin(comp, you):
    # if comp and your value is same
    if comp == you:
        return None

    # check all possibility when computer choose snake(s)
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True

    # Check all possibility when computer choose water(w)
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    # Check all possibility when computer choose gun(g)

    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True


print("comp turn: snake(s) water(w) gun(g)")

randomNo = random.randint(1, 3)
if randomNo == 1:
    comp = "s"
elif randomNo == 2:
    comp = "w"
elif randomNo == 3:
    comp = "g"

you = input("Your Turn: snake(s) water(w) gun(g): ")
a = gameWin(comp, you)

print(f"computer choose: {comp}")
print(f"you choose: {you}")
if a is None:
    print("The game is Tie")
elif a:
    print("You Win")
else:
    print("You Lose")
