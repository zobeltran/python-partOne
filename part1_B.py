# Time Check Start: 10:30

# B. Write a function find_divisible(a, b, k) that accepts three integers: a, b and k, and returns
# the total count of the numbers between a and b (inclusive) that are divisible by k
# ● find_divisible(6,11,2) should return 3. 6, 8, and 10 are all divisible by 2.
# ● find_divisible(0,12,3) should return 5. 0, 3,6, 9, and 12 are all divisible by 3.

def find_divisible(a, b, k):

    counter = 0
    list = []

    for i in range(a, b):
        if(i % k == 0):
            counter = counter + 1
    
    for i in range(a, b):
        if(i % k == 0):
            list.append(i)

    convert_to_string= ", ".join(map(str, list))

    return str(counter) + ". " + convert_to_string + " are all divisible by " + str(k)

print(find_divisible(1, 11, 2))

# Timecheck End: 11:00