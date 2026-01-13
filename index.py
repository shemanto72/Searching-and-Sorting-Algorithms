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
        sorting()
    else:
        print("Invalid Input")

def searching():
    print("***************************")
    print("1.Binary Search")
    print("2.Linear Search")
    print("3.Interpolation Search")
    chosen = input("You have Chosen Searching! Now chose what algorithm you want to use: ")
    if chosen == "1":
        nums = list(map(int, input("***************************** \nYou have choose binary search, first enter the number list: ").split()))
        nums.sort()
        target = int(input("Enter the Targeted value: "))
        result = binary_search(nums , target)
        if result == -1:
            print("Target not Found!")
        else:
            print(f'The index number of {target} is: {result}')
    elif chosen == "2":
        nums = list(map(int, input("***************************** \nYou have choose binary search, first enter the number list: ").split()))
        target = int(input("Enter The targeted value: "))
        result = linear_search(nums , target)
        if result == -1:
            print("Target not found!")
        else:
            print(f'The index number of {target} is : {result}')
    elif chosen == "3":
        nums = list(map(int, input("***************************** \nYou have choose Interpolation search, first enter the number list: ").split()))
        nums.sort()
        target = int(input("Enter The targeted value: "))
        result = interpolation_search(nums , target)
        if result == -1:
            print("Target not found!")
        else:
            print(f'The index number of {target} is : {result}')
    else:
        print("Invalid Choice")

def sorting():
    print("1.Bubble Sort")
    print("2.Selection Sort")
    print("3.Merge Sort")
    chose = input("You have Chosen sorting! Now choose what algorithim you want to use: ").strip()

    if chose == "2":
        nums = list(map(int, input("***************************** \nYou have choose selection sort, first enter the number list: ").split()))
        selection_sort(nums)
        print(f'Sorted List: {nums}')
    elif chose == "1":
        nums = list(map(int, input("***************************** \nYou have choose bubble sort, first enter the number list: ").split()))
        bubble_sort(nums)
        print(f'Sorted List: {nums}')
    elif chose == "3":
        nums = list(map(int, input("***************************** \nYou have choose merge sort, first enter the number list: ").split()))
        print(f'Sorted List: {merge_sort(nums)}')
    else:
        print("Invalid Choice")

def binary_search(nums, target):
    top = len(nums) - 1
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


def interpolation_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high and nums[low] <= target <= nums[high]:
        if nums[high] == nums[low]:
            if nums[low] == target:
                return low
            else:
                break
        possible_index = low + (target - nums[low]) * (high - low) // (nums[high] - nums[low])
        if nums[possible_index] == target:
            return possible_index
        elif nums[possible_index] > target:
            high = possible_index - 1
        else:
            low = possible_index + 1
    return -1



def selection_sort(nums):
    for i in range(len(nums)):
        for j in range(i+1 , len(nums)):
            if nums[j] < nums[i]:
                nums[j] , nums[i] = nums[i] , nums[j]


def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]



def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

main()





























