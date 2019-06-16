from random import randint

def roll_dice(): #simulate the rolling of six-sided dice
    roll_1 = randint(1, 6)
    roll_2 = randint(1, 6)
    return  roll_1, roll_2

def get_response():
    response = str(input("Do you want to roll? "))
    while response != 'y' and response != 'n': #Accepts only ‘y’ or ‘n’ as a valid response
        response = str(input("Invalid response. Please enter y or n: "))
    return response

def main():
    computer_sum = 0
    user_sum = 0
    choice = get_response()
    while choice == 'y' and user_sum <= 21:
        computer_roll, user_roll = roll_dice()
        computer_sum += computer_roll
        user_sum += user_roll
        print("Points: ", user_sum)
        if user_sum <= 21:
            choice = get_response()

    print("User points: ", user_sum)
    print("Computer points: ", computer_sum)
    if(user_sum < 21 and computer_sum > 21):
        print("User Wins!")
    elif(user_sum > 21 and computer_sum < 21):
        print("Computer Wins!")
    else:
        print("Tie Game!")

main()
