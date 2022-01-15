# Test Exam Part 1

# Timecheck: Start 10:00 PM 


# A. Given an array A of N integers, write a function missing_int(A) that returns the smallest
# positive integer (greater than 0) that does not occur in A.
# ● A = [1, 3, 6, 4, 1, 2] should return 5
# ● A = [1, 2, 3] should return 4
# ● A = [-1, -1, -1, -5] should return 1
# ● A = [1, 3, 6, 4, 1, 7, 8, 10] should return 2

def missing_int(array, number):

    placeHolder = 0

    for i in range(number):
        if array[i] == 1:
            placeHolder = 1
            break
    
    if placeHolder == 0:
        return(1)

    for i in range(number):
        if array[i] <= 0 or array[i] > number:
            array[i] = 1

    for i in range(number):
        array[(array[i] - 1) % number] += number

    for i in range(number):
        if array[i] <= number:
            return(i + 1)

    return(number + 1)


list = []

user_input = int(input("Enter the number of integers in the list then enter the list of integers desired: "))

for i in range(0, user_input):
    elements = int(input())
    list.append(elements)

size_checker = len(list)

print("Given array is " + str(list) + " and the Missing Digit is " + str(missing_int(list, size_checker)))
    
# Timecheck End 10:30 PM