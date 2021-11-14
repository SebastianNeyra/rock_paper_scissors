import random # importing a library

def play(): # This is a function 
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer: 
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer): # This line will call is_win function below
        return 'You won!' # If is_win returns True then we will get a 'You won' message

    return 'You lost!' # If the function comes back as False then we will get a 'You lost!' message

def is_win(player, opponent): # This is a function
     # return true if player wins
     # r > s, s > p, p > r
     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
         return True

print(play()) # calling the function