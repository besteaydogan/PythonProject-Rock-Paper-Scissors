import random

def rock_paper_scissors_BESTE_AYDOGAN():
    # Welcome message and game instructions
    print("Welcome to Rock, Paper, Scissors!")
    print("Game Rules:")
    print("1. Choose rock, paper, or scissors.")
    print("2. Rock beats scissors, scissors beats paper, and paper beats rock.")
    print("3. If you want to quit the game at any time, just enter 'q'.")
    print("4. The first to win two rounds wins the game.")
    print("Let's get started!\n")

    def computer_choice():
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)
    
    def determine_winner(player, computer):
        if player == computer:
            return "It's a tie!", None
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            return "You win this round!", "player"
        else:
            return "Computer wins this round!", "computer"

    def computer_continue():
        return random.choice(["yes", "no"])

    while True:
        player_score = 0
        computer_score = 0

        # Inner loop for the rounds
        while player_score < 2 and computer_score < 2:
            player_choice = input("Choose rock, paper, or scissors. To quit, enter 'q': ").lower()
            if player_choice == "q":
                print("Game over.")
                return  # Exit the function to end the game
            elif player_choice not in ["rock", "paper", "scissors"]:
                print("Invalid choice. Try again.")
                continue

            pc_decision = computer_choice()
            print(f"The computer chose: {pc_decision}")

            result, winner = determine_winner(player_choice, pc_decision)
            print(result)

            if winner == "player":
                player_score += 1
            elif winner == "computer":
                computer_score += 1

            print(f"Score: You {player_score} - Computer {computer_score}")

        # Determine and display the overall game winner
        if player_score == 2:
            print("Congratulations! You are the overall winner of the game!")
        elif computer_score == 2:
            print("The computer is the overall winner of the game!")

        # Ask the player if they want to play another game
        player_continue = input("Do you want to play another game? (yes/no): ").lower()
        if player_continue != "yes":
            print("You chose not to continue. Game over.")
            break

        # Determine if the computer wants to continue
        computer_continue_decision = computer_continue()
        print(f"Computer's decision to continue: {computer_continue_decision}")

        if computer_continue_decision != "yes":
            print("The computer chose not to continue. Game over.")
            break

# Call the function to start the game
rock_paper_scissors_BESTE_AYDOGAN()
