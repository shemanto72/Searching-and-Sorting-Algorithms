def main():
    print("Welcome! Please Choose Your Optoin")
    print("*************")
    print("1.Searching")
    print("2.Sorting")
    print("***************************")
    chosen = input()
    if chosen == "1":
        searching()
    elif chosen == "2":
        print("Sorting chosen")
    else:
        print("Invalid Input")

def searching():
    print("***************************")
    print("1.Binary Search")
    print("2.Linear Search")
    chosen = input("You have Chosen Searching! Now chose what algorithim you want to use: ")
    if chosen == "1":
        nums = list(map(int, input("***************************** \nYou have choose binary search, first enter the number list: ").split()))
        target = int(input("Enter the Targated value: "))
        result = binary_search(nums , target)
        if result == -1:
            print("Target not Found!")
        else:
            print(f'The index number of {target} is: {result}')
    elif chosen == "2":
        nums = list(map(int, input("***************************** \nYou have choose binary search, first enter the number list: ").split()))
        target = int(input("Enter The targated value: "))
        result = linear_search(nums , target)
        if result == -1:
            print("Target not found!")
        else:
            print(f'The index number of {target} is : {result}')
    else:
        print("Invalid Choise")

def sorting():
    chose = input("You have Chosen sorting! Now choose what algorithim you want to use: ")
    print("1.Bubble Sort")
    print("2.Selection Sort")

    if chose == "1":
        pass
    elif chose == "2":
        pass
    else:
        print("Invalid Choise")

def binary_search(nums, target):
    top = len(nums)
    low = 0
    print(nums)
    while low <= top:
        mid = (top+low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            top = mid - 1
    return -1

def linear_search(nums , target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1




main()





























