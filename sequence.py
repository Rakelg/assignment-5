
n = int(input("Enter the length of the sequence: ")) # Do not change this line

counter = 0 

for i in range(1,n+1): 
    sequence = i + (i+1)
    counter += 1
    print(sequence)

