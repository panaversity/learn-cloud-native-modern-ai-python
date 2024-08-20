## Problem Statement

Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may be able to help!

Here's a sample run of the program (user input is in blue):

Please type the following affirmation: I am capable of doing anything I put my mind to. 
Hmmm 
That was not the affirmation. 
Please type the following affirmation: I am capable of doing anything I put my mind to. 
I am capable of doing anything I put my mind to. 
That's right! :)

Note that you can call input() with no prompt and it will still wait for a user to type something!

## Starter Code

```bash
def main():
    print("Delete this line and write your code here! :)")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
```

## Solution
```bash
AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  # Get user's input
    while user_feedback != AFFIRMATION:  # While the user's input isn't the affirmation
        # Tell the user that they did not type the affirmation correctly
        print("That was not the affirmation.")

        # Ask the user to type the affirmation again!
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
```