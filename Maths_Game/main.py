import random

MIN = 1
MAX = 10
NB_QUESTION = 4


def ask_math():
    a = random.randint(MIN, MAX)
    b = random.randint(MIN, MAX)
    operator = random.randint(0, 1)
    if operator == 0:
        result = a + b
        user = int(input(f"{a} + {b} = "))
    else:
        result = a * b
        user = int(input(f"{a} x {b} = "))
    if user == result:
        return True
    return False


i = 0
score = 0
while i < NB_QUESTION:
    print(f"Question n°{i+1} sur {NB_QUESTION}: ")
    if ask_math():
        print("Correct")
        score += 1
    else:
        print(f"Wrong")
    i += 1
    print()

print(f"Your Score is {score}/{NB_QUESTION}")


