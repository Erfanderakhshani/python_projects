import random
# Computer choose number and you have to guess
def guess(x):
    rand_num = random.randint(1, x)
    user_guess = 0
    guess_count = 0
    is_true = False
    while is_true == False and guess_count <= 10:
        user_guess = int(input(f"Please guess number between 1 to {x} : "))
        if user_guess == rand_num:
            print(f"congratulation!! you guess the number {rand_num}")
            is_true = True
        elif user_guess < rand_num:
            guess_count += 1
            print("Your guess was too low")
            print(f"Please guess again, you have {10 - guess_count } guesses!")
        elif user_guess > rand_num:
            guess_count += 1
            print("Your guess was too high")
            print(f"Please guess again, you have {10 - guess_count } guesses!")
    if is_true == False:
        print("You lose!!!!! ")

guess(100)