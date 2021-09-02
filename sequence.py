
n = int(input("Enter the length of the sequence: ")) # Do not change this line
# algorithm : next number in the sequence is the sum of last 3 numbers, the program needs to go 3 numbers back and find the sum. if 1,2 or 3 the program cant go 3 numbers back so that is hardcoded. 


for i in range(1, n+1):
    if i == 1:
        current = first = i
    elif i == 2:
        current = second = i
    elif i == 3:
        current = third = i
    else:
        current = first + second + third
        first, second, third = second, third, current
    print(current)
