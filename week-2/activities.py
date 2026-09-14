def game_outcome(your_score, opponent_score):
    if your_score > opponent_score:
        return "You win!"
    elif opponent_score > your_score:
        return "You lose!"
    else:
        return "Tie game!"

def main():
    your_score = int(input("Enter your score: "))
    opponent_score = int(input("Enter opponent's score: "))
    result = game_outcome(your_score, opponent_score)
    print(result)

main()