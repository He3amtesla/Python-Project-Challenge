import random
num = random.randint(0,100)
print("Correct guessing game: In this game")
print(", I get a number between 0 and 100 in my mind and you have to guess which number it is")
print("and if you say wrong, your score will be deducted, your score in the game starts from 10.")
score = 10
T = True
T2 = True
while(T2):
    while(T) :  
        T = False
        #* Checking the input value
        try:
            input_value = int(input("Enter a number between 0 and 100 :"))
        except ValueError :
             print("!!!Please enter a number") ; T = True ; break
        if input_value == num:
            print("Well done, you guessed right") ; T2 = False
        #* Checking that the score is not lower than 0 and guiding the user to guess
        else:
            if score < 1:
                print("you lose:(, try next time")
                T2 = False
                break
            num2 = random.randint(0,num)
            num3 = random.randint(num,100)
            score -= 1
            print(f"Hint: The number between {num2} to {num3}, Your score {score}")
            T = True
            break
#by Mohammadhesam pourakbar