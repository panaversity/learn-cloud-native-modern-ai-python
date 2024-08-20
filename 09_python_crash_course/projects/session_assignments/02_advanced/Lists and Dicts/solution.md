# Index Game Solution
```bash
def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."

def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_element(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst, start, end))
    else:
        print("Invalid operation.")

index_game()

```

# List Practice Solution

def main():
    # Create a list called `fruit_list` that contains the following fruits: 'apple', 'banana', 'orange', 'grape', 'pineapple'.
    fruit_lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list.
    lst_length = len(fruit_lst)
    print(lst_length)

    # Add 'mango' at the end of the list. 
    fruit_lst.append('mango')

    # Print the updated list.
    for fruit in fruit_lst:
        print(fruit)

if __name__ == '__main__':
    main()

