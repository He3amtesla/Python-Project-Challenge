import random


def validate_input(input_user):
    if not input_user.isdigit():
        print("add vared konid: ")
        return False

    input_user = int(input_user)
    if input_user > 100 or input_user < 0:
        print("Enter a number between 0 and 100 ")
        return False
    
    return True


def main():
    randnum = random.randint(0, 100)
    score = 10
    while True:
        input_user = input("Guess from 1 to 100 numbers: ")
        if input_user == 'q':
            print("don't you love me, bye T_T")
            break
        
        if not validate_input(input_user):
            continue
        
        input_user = int(input_user)
        
        if randnum < input_user:
            print("The number you considered is higher than that number")
            score -=1
            continue
        elif randnum > input_user:
            print("The number you considered is less than this number")
            score -=1
            continue
        
        score = max(score, 0)

        print ("Well done, you guessed right, Your score: ", score)
        qusstion_user = input(
            "Do you want to play again? (yes --type-> y ,no --type->  n): "
                              )
        if qusstion_user == 'y':
            score = 10
            randnum = random.randint(0, 100)

            continue
        break


if __name__ == "__main__":
    main()
