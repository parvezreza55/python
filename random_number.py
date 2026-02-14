from random import*

guess = randint(1,5)
print(guess)



for i in range(1,10):
     guess_number = int(input("enter the number between 1 and 100"))
     random_number = int(random() * 100)
     print(random_number)
     if random_number == guess_number:
         print("You won")
     else :
        print("You lost")
        print("The number was",random_number)
