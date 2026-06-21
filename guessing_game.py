import random 

print ("===Number Guessing Game===")
print ("I am thinking of a number between 1 and 100")

number = random.randint(1,100)
attempts = 0

while True:
    guess = input("what is your guess? ")
    guess = int(guess)
    attempts += 1

    if guess == number:
       break 
    elif guess > number:

        print (f"Guess ={guess}")
        print ("Too high!")

    elif guess < number:
        print (f"Guess : {guess}")
        print ("Too low!")    

print(f"correct!, you got it in {attempts} attempts! ")    

if attempts <= 5:
    print ("Amazing!")
elif attempts  <=10:
    print("Good job!")
else:
    print("You got there eventually!")    
