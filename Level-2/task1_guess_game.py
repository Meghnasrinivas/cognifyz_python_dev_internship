import random

lower = int(input("Enter the lower bound of the range: "))
upper = int(input("Enter the upper bound of the range: "))

number_to_guess=random.randint(lower,upper)
guess=None
attempt=0

print('Welcome to number guessing game!!!')
print(f'I am choosing between {lower} to {upper}')

while guess!=number_to_guess:
    guess=int(input('Enter your guess : '))
    attempt+=1

    if guess<number_to_guess:
        print('Too low. Try again')
    elif guess>number_to_guess:
        print('Too high. Try again')
    else:
        print(f'You guessed it in {attempt} attempts. Congratulations!!!!!!')