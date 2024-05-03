def checkArray():
    # Get the number of elements in the array
    no_of_elements = int(input("Enter the number of elements in the array: "))

    # Initialize an empty list to store the array
    my_list = []

    # Get the elements from the user
    for i in range(no_of_elements):
        num = int(input("Enter a number in the array: "))
        my_list.append(num)

    # Check if the array is sorted
    if my_list == sorted(my_list):
        return True
    else:
        return False

# Call the function and print the result


result = checkArray()
print(f"Is the array sorted? {result}")
