# Program: Rock, Paper, Scissors Game Logic

# Step 1: Take input from two players
player1 = input("Player 1 (rock/paper/scissors): ").lower()
player2 = input("Player 2 (rock/paper/scissors): ").lower()

# Step 2: Validate inputs
valid_choices = ["rock", "paper", "scissors"]

if player1 not in valid_choices or player2 not in valid_choices:
    print("Invalid input. Please choose rock, paper, or scissors.")

else:
    # Step 3: Check for tie condition
    if player1 == player2:
        print("It's a tie!")

    # Step 4: Check winning conditions for Player 1
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        print("Player 1 wins!")

    # Step 5: Otherwise, Player 2 wins
    else:
        print("Player 2 wins!")

# End of Program
