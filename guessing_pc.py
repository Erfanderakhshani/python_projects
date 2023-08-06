import random
#  User choose number and Computer have to guess
def pc_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"If {guess} is correct enter (c) if it is low enter (l) and if it is high enter(h) :".lower())
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"congratulation!! the computer guess the number {guess}")

pc_guess(10)