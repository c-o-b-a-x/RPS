import random

c_move = ""
p_move = ""
p_win = int(0)
c_win = int(0)
games = int(0)

def header():
    print("""
.-. .-. .-. . .     .-. .-. .-. .-. .-.     .-. .-. .-. .-. .-. .-. .-. .-. 
|(  | | |   |<      |-' |-| |-' |-  |(      `-. |    |  `-. `-. | | |(  `-. 
' ' `-' `-' ' ` ,   '   ` ' '   `-' ' ' ,   `-' `-' `-' `-' `-' `-' ' ' `-' 
    _______           _______               _______ 
---'   ____)      ---'   ____)____     ---'    ____)____ 
      (_____)               ______)               ______) 
      (_____)               _______)           __________) 
      (____)               _______)           (____) 
---.__(___)       ---.__________)      ---.__(___)
           """)

def player_move():
    while True:
        p_move = input("Rock, Paper, or Scissors ?: ").lower().strip()
        if p_move != "rock" and p_move != "paper" and p_move != "scissors":
            print("That's not a valid move ")
        else:
            return p_move

def computer_move():
    valid_moves = ["rock", "paper", "scissors"]
    c_move = random.choice(valid_moves)
    print(f"The computer played {c_move}")
    return c_move

def check_winner(games, p_move, c_move, p_win, c_win):
    if p_move == c_move:
        print("It's a Tie")
    else:
        if (p_move == "rock" and c_move == "scissors") or (p_move == "paper" and c_move == "rock") or (p_move == "scissors" and c_move == "paper"):
            print("Player Wins!!")
            p_win += 1
        else:
            print("Computer Wins !!!")
            c_win += 1
            
    games += 1
    print(f"Games played: {games}")
    
    if games == 5:
        series_winner(p_win, c_win)

    return games, p_win, c_win

def series_winner(p_win, c_win):
    if p_win > c_win:
        print("You won the series ")
    if c_win > p_win:
        print("The computer won the series ")
def data(c_win,p_win):
    print (f"the computer won {c_win} times")
    print (f"you won {p_win} times")
    print (f"your win percentage was {p_win /.050}")
def RPS(games, c_move, p_move, p_win, c_win):
    header()
    while games < 5:
        p_move = player_move()
        c_move = computer_move()
        games, p_win, c_win = check_winner(games, p_move, c_move, p_win, c_win)

    series_winner(p_win, c_win)
    data(c_win,p_win)
if __name__ == '__main__':
    RPS(games, c_move, p_move, p_win, c_win)
