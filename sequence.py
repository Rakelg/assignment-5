
n = int(input("Enter the length of the sequence: ")) # Do not change this line
# algorithm : curr_num in the sequence is the sum of last 3 numbers
# the program needs to go 3 numbers back and find the sum. 
# if 1,2 or 3 is entered the program program prints the first 1-3 numbers of the sequence. 


for i in range(1, n+1): 
    if i == 1: 
        curr_num = first = i
    elif i == 2: 
        curr_num = second = i 
    elif i == 3: 
        curr_num = third = i 
    else : 
        curr_num = first + second + third
        first, second, third = second,third,curr_num
    print(curr_num)
    
