## Problem Statement

There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!

We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an adult (in the United States). Fill out the is_adult(age) function, which returns True if the function takes an age that is greater than or equal to ADULT_AGE. If the function takes an age less than ADULT_AGE, return False instead.

Here are two sample runs of the program, one for each return option (user input in bold italics):

(Entered age is an adult age)

How old is this person?: 35

True

(Entered age is not an adult age)

How old is this person?: 7

False

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
ADULT_AGE : int = 18 # U.S. age 

def is_adult(age: int):
    if age >= ADULT_AGE:
        return True
    
    return False
    
########## No need to edit code beyond this point :) ##########

def main():
    age : str = int(input("How old is this person?: "))
    print(is_adult(age))
    

if __name__ == "__main__":
    main()
```