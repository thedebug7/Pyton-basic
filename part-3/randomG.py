import random

secret_Number = random.randint(1,10);
user_number = None
while secret_Number != user_number:
    user_number = int(input("Enter your Number: "))
    if secret_Number == user_number:
        print("Congratulations! You guessed the number.")
        break
    elif secret_Number > user_number:
        print("Too low! Try again.")
    elif secret_Number < user_number:
        print("Too high! Try again.")
    elif user_number > 10 or user_number < 0 :
        print("Please enter a number between 0 and 10.")
        


