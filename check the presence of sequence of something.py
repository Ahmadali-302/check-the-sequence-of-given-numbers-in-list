def checkArray():
    noOfArray = int(input("Enter the no. of arrays that you want to check: "))
    myList = []
    for i in range(noOfArray):
        num = int(input("Enter the number in array: "))
        myList.append(num)
    # following line is map(str, myList) convert list into string then ''.join will make one string of all the list
    myList_str = ''.join(map(str, myList))

    if '123' in myList_str:
        return True

    else:
        return False


result = checkArray()

print(result)
