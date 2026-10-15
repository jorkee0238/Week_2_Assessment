#Jordan Keeler-Williams 10/14/2026
#This program lets a user enter a number to attempt to guess what right number is

name = input("Please enter your name: ")
studentID = input("Please enter your student ID: ")
answer = 4
tries = 1
loop = 1
guess = 0


print(f"Hello {name}! Would you like to guess the number I am thinking of?")

while guess != answer:

    guess = int(input("Please enter your guess: "))
    
    if guess == answer:
       print(f"Yes {name}! The answer was {answer}! Good job you got in {tries} attempts!\n")

    else:
        if guess > answer:
            print("Your guess is too high!")
        else: 
            print("Your guess is too low!")
    tries += 1

print("Output using a 'while' loop")
while loop != 6:
    print(f"{answer} incremeted by {loop} is {answer + loop}")
    loop += 1

print("\nOutput using a 'for' loop")
for counter in range(1, 6):
    print(f"{answer} incremeted by {counter} is {answer + counter}")
