import time
import array

curr_time = time.strftime("%H:%M", time.localtime())

print("Current Time is :", curr_time)


R = 4
C = 3

R = int(input("Enter the number of medications:"))
# Initialize matrix
matrix = []

# For user input
for i in range(R):          # A for loop for row entries
    a =[]
    print("Enter Medication for container " + str(i+1) + ":")
    for j in range(C):      # A for loop for column entries
        if j == 1:
            print("Enter time for container " + str(i+1) + ":")
        elif j == 2:
            print("Enter dosage for container " + str(i+1) + ":")      
        a.append((input()))
    matrix.append(a)
  
# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()
times = []
for i in range(R):
    times.append(matrix[i][1])
print(str(times))

while True:
    for i in range(R):
        if matrix[i][1] == curr_time:
            print("Time matches" + matrix[i][0])
    


