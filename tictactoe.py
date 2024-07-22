import random
import sys

gameboard = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def gameboard_display():
    global gameboard
    row = 3
    column = 3
    for i in range(row):
        print("\n+---+---+---+")
        print("|", end="")
        for j in range(column):
            print("", gameboard[i][j], "|", end="")
    print("\n+---+---+---+")

def modify_game(num, turn):
    num -= 1
    if num == 0:
        gameboard[0][0] = turn
    elif num == 1:
        gameboard[0][1] = turn
    elif num == 2:
        gameboard[0][2] = turn
    elif num == 3:
        gameboard[1][0] = turn
    elif num == 4:
        gameboard[1][1] = turn
    elif num == 5:
        gameboard[1][2] = turn
    elif num == 6:
        gameboard[2][0] = turn
    elif num == 7:
        gameboard[2][1] = turn
    elif num == 8:
        gameboard[2][2] = turn

def x_o():
    while True:
        user = input("Choose X or O: ").strip().upper()
        if user in ['X', 'O']:
            if user == 'X':
                comp = 'O'
            else:
                comp = 'X'
            print(f"user: {user} comp: {comp}")
            return user, comp
        else:
            print("Incorrect choice. Please choose X or O.")

def winner(user, comp, gameboard):
    if gameboard[0][0] == gameboard[0][1] == gameboard[0][2] == user:
        print("You Win!!")
        sys.exit()
    elif gameboard[1][0] == gameboard[1][1] == gameboard[1][2] == user:
        print("You Win!!")
        sys.exit()
    elif gameboard[2][0] == gameboard[2][1] == gameboard[2][2] == user:
        print("You Win!!")
        sys.exit()
    elif gameboard[0][0] == gameboard[1][0] == gameboard[2][0] == user:
        print("You Win!!")
        sys.exit()
    elif gameboard[0][1] == gameboard[1][1] == gameboard[2][1] == user:
        print("You Win!!")
        sys.exit()
    elif gameboard[0][2] == gameboard[1][2] == gameboard[2][2] == user:
        print("You Win!!")
        sys.exit()
    elif gameboard[0][0] == gameboard[1][1] == gameboard[2][2] == user:
        print("You Win!!")
        sys.exit()
    elif gameboard[0][2] == gameboard[1][1] == gameboard[2][1] == user:
        print("You Win!!")
        sys.exit()
    elif gameboard[0][0] == gameboard[0][1] == gameboard[0][2] == comp:
        print("You Lose!!")
        sys.exit()
    elif gameboard[1][0] == gameboard[1][1] == gameboard[1][2] == comp:
        print("You Lose!!")
        sys.exit()
    elif gameboard[2][0] == gameboard[2][1] == gameboard[2][2] == comp:
        print("You Lose!!")
        sys.exit()
    elif gameboard[0][0] == gameboard[1][0] == gameboard[2][0] == comp:
        print("You Lose!!")
        sys.exit()
    elif gameboard[0][1] == gameboard[1][1] == gameboard[2][1] == comp:
        print("You Lose!!")
        sys.exit()
    elif gameboard[0][2] == gameboard[1][2] == gameboard[2][2] == comp:
        print("You Lose!!")
        sys.exit()
    elif gameboard[0][0] == gameboard[1][1] == gameboard[2][2] == comp:
        print("You Lose!!")
        sys.exit()
    elif gameboard[0][2] == gameboard[1][1] == gameboard[2][1] == comp:
        print("You Lose!!")
        sys.exit()
    if all(cell != ' ' for row in gameboard for cell in row):
        print("It's a Tie!")
        sys.exit()



def main():
    user, comp = x_o()
    print("Each grid is assigned a number (1 to 9) starting horizontally.")
    leave = False
    gameboard_display()
    turn_choice = 1
    while leave is False:
        if turn_choice % 2 == 1:
            turn = user
            while True:
                num = int(input("Enter a number to choose the grid: "))
                if num in possible_numbers:
                    modify_game(num, turn)
                    possible_numbers.remove(num)
                    gameboard_display()
                    turn_choice += 1
                    break
                else:
                    print("Invalid choice. Grid already chosen or unavailable. Choose another grid.")
        else:
            turn = comp
            while True:
                if possible_numbers != []:
                    comp_choice = random.choice(possible_numbers)
                    print(f"comp choice: {comp_choice}")
                    if comp_choice in possible_numbers:
                        modify_game(comp_choice, turn)
                        possible_numbers.remove(comp_choice)
                        turn_choice += 1
                        gameboard_display()
                        break
                    else:
                        continue
                break
        winner(user, comp, gameboard)


if __name__ == "__main__":
    main()
