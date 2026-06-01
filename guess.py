import random

gameOn = True


randomNumber = random.randint(1,10)
while True:
  userInput = input("guess a number")
  convert = int(userInput)
 
  
  
  if(convert == randomNumber):
    print("your guess is superb")
    break
  else:
    print("your guess is not correct")
    break

print("computer number is",randomNumber,"and your number is",convert)
