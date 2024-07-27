## Problem Statement

Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high)
  """
  Returns True if n is between low and high, inclusive. 
  high is guaranteed to be greater than low.
  """

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
def in_range(n, low, high):
  """
  Returns True if n is between low and high, inclusive. 
  high is guaranteed to be greater than low.
  """
    if n >= low and n <= high:
	return True

    # we could have also included an else statement, but since we are returning, it's fine without!
    return False
```