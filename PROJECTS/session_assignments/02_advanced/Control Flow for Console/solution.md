
### Simple Solution

```bash
import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Milestone 5: keep track of your score
    your_score = 0

    # Milestone 4: Play multiple rounds
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        # Milestone 1: Generate the random numbers and print them out
        computer_num: int = random.randint(1, 100)
        your_num: int = random.randint(1, 100)
        print("Your number is", your_num)

        # Milestone 2: Get user input for their choice
        choice: str = input("Do you think your number is higher or lower than the computer's?: ")

        # Milestone 3: Map out all the ways to win the round
        higher_and_correct: bool = choice == "higher" and your_num > computer_num
        lower_and_correct: bool = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_num)
            # Milestone 5: keep track of your score
            your_score += 1 
        else: 
            print("Aww, that's incorrect. The computer's number was", computer_num)

        # Milestone 5: keep track of your score
        print("Your score is now", your_score)
        print()

    print("Thanks for playing!")

if __name__ == "__main__":
    main()

```

### Solution (with extensions):

```bash
import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Milestone 5: keep track of your score
    your_score = 0

    # Milestone 4: Play multiple rounds
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        # Milestone 1: Generate the random numbers and print them out
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print("Your number is", your_num)

        # Milestone 2: Get user input for their choice
        choice = input("Do you think your number is higher or lower than the computer's?: ")

        # Extension 1: Make sure the player inputs a valid choice (higher or lower)
        while choice != "higher" and choice != "lower":
            choice = input("Please enter either higher or lower: ")

        # Milestone 3: Map out all the ways to win the round
        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_num)
            # Milestone 5: keep track of your score
            your_score += 1 
        else: 
            print("Aww, that's incorrect. The computer's number was", computer_num)

        # Milestone 5: keep track of your score
        print("Your score is now", your_score)
        print()
    
    # Extension 2: Conditional ending messages based on performance
    print("Your final score is", your_score)

    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()

```