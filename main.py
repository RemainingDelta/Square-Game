import math
import random
import time


squares = input("Enter number of squares in each row (put a space in between each number): ")

squares_array = []
binary_array = []

def squares_picture(number_string):
    
   # Split the string into individual numbers
   numbers = number_string.split()
  
   # Loop through each number and print the corresponding number of 'X's
   for number in numbers:
       count = int(number)  # Convert the string to an integer
       print('X' * count)   # Print 'X' repeated 'count' times
       squares_array.append(count)
       binary_array.append(int(bin(count)[2:]))
   print (squares_array)
   print (binary_array)

squares_picture(squares)

def xor(array):
    xor_value = 0
    for i in range(len(array)):
        xor_value = xor_value ^ array[i]
    return xor_value

xor_value = xor(binary_array)


def recommended_move():
    leftmost_1_index = math.floor(math.log(xor_value, 10))
    number = 0
    #print(leftmost_1_index)
    for i in range(len(binary_array)):
        #print ("Number at leftmost index 1: " + str(math.floor((binary_array[i]/(math.pow(10,leftmost_1_index))))%10))
        if (math.floor((binary_array[i]/(math.pow(10,leftmost_1_index))))%10) == 1:
            #print("Has left most 1: " + str(binary_array[i]))
            if ((binary_array[i]) ^ xor_value) < binary_array[i]:
                number = (binary_array[i])
                new_number = ((binary_array[i]) ^ xor_value)
                return ("Recommended: Take " + str((int(str(number),2)) - (int(str(new_number),2))) + " Square(s) from Row " + str(i+1))


while (any(squares_array)):
    if (xor_value != 0):
        print("\nPlayer Turn")
        print(recommended_move())
        row = input("What row would you like to take from? ")
        num_of_squares = input("How many squares from this row? ")
        new_list_string = ""
        for i in range(len(squares_array)):
            if (i != int(row) - 1):
                new_list_string = new_list_string + str(squares_array[i]) + " "
            else:
                new_list_string = new_list_string + str(squares_array[i]-int(num_of_squares)) + " "
        squares_array = []
        binary_array = []
        squares_picture(new_list_string)
        xor_value = xor(binary_array)
    else:
        print("\nComputer Turn")
        print("Thinking...")
        time.sleep(1)
        row = random.randint(1, len(squares_array))
        while squares_array[row - 1] == 0:
            row = random.randint(1, len(squares_array))  
        num_of_squares = random.randint(1, squares_array[row - 1])
        print("Took " + str(num_of_squares) + " Square(s) from Row " + str(row))
        new_list_string = ""
        for i in range(len(squares_array)):
            if (i != (row) - 1):
                new_list_string = new_list_string + str(squares_array[i]) + " "
            else:
                new_list_string = new_list_string + str(squares_array[i]-(num_of_squares)) + " "
        squares_array = []
        binary_array = []
        squares_picture(new_list_string)
        xor_value = xor(binary_array)

print("Player won")
