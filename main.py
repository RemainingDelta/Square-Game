import math
import random
import time


# squares_array will be used to store the number of squares in each row
squares_array = []

# binary_array will be used to store the number of squares in each row in base 2 
binary_array = []

# turn : determines the turn; true if players turn and false if computer turn
turn = True 

# squares_picture() turns a string of numbers into a picture with "X"s to signify the squares in each row
def squares_picture(number_string):  
   numbers = number_string.split() # Split the string into individual numbers
   for number in numbers: # Loop through each number and print the corresponding number of 'X's
       count = int(number)  # Convert the string to an integer
       print('X' * count)   # Print 'X' repeated 'count' times
       squares_array.append(count) # Add number to squares_array
       binary_array.append(int(bin(count)[2:])) # Add number in base 2 to binary_list


# Determines the xor value of a binary array
def xor(array):
    xor_value = 0 
    for i in range(len(array)):
        xor_value = xor_value ^ array[i] # xor each value of the array with the xor_value of the previous values
    return xor_value # Return xor_value 

# If the xor_value is not 0, then give recommended move
def recommended_move():
    leftmost_1_index = math.floor(math.log(xor_value, 10)) # Finds the index with the leftmost 1
    number_to_change = 0
    for i in range(len(binary_array)): # Loop through each element of binary_element
        if (math.floor ((binary_array[i] / (math.pow (10,leftmost_1_index)))) % 10) == 1: # Looking for the first element in binary_element that has a 1 in the leftmost_1_index
            number_to_change = (binary_array[i]) # Set number_to_change to that number
            new_number = (number_to_change ^ xor_value) # Set new_number to the number_to_change xor xor_value
            return ("Recommended: Take " + str((int(str(number_to_change),2)) - (int(str(new_number),2))) + " Square(s) from Row " + str(i+1)) # Recommend move based on the number_to_change and new_number

# Ensures user picks valid row
def pick_row():
    row = int(input("What row would you like to take from? "))
    while (row > len(squares_array) or squares_array[row - 1] == 0):
        row = int(input("No squares left in this row or invalid row, pick again: "))
    return row

# Ensures user picks valid number of squares to remove
def pick_num_of_squares(row):
    num_of_squares = int(input("How many squares from this row? "))
    while (squares_array[row - 1] < num_of_squares):
        num_of_squares = int(input("Not enough squares left in this row, pick again: "))
    return num_of_squares

# Plays the square game
def squares_game():
    global squares_array, binary_array, turn, xor_value # Finds theses variables in the global score to use
    while (any(squares_array)): # While there is anything other than 0 in squares_array 
        if (turn): # If it is the players turn
            print("\nPlayer Turn")
            if (xor_value != 0): # If xor_value is not 0, then print(recommended_move()) 
                print(recommended_move())
            else:                # Else print "No Recommended Move at This Point"
                print("No Recommended Move at This Point")
            row = pick_row() # row is equal to a valid row that the user picks
            num_of_squares = pick_num_of_squares(row) # num_of_squares is equal to a valid number of squares to remove that the user picks
            new_string_of_numbers = "" # Empty string
            for i in range(len(squares_array)): # Loop through squares_array
                if (i != row - 1): # If i is not equal to row - 1 then add the value in squares_array[i] to new_string_of_numbers
                    new_string_of_numbers = new_string_of_numbers + str(squares_array[i]) + " "
                else:              # If i is equal to row - 1 then add the value in squares_array[i] - num_of_squares to new_string_of_numbers
                    new_string_of_numbers = new_string_of_numbers + str(squares_array[i] - num_of_squares) + " "
            squares_array = [] # Reset squares_array
            binary_array = [] # Reset binary_array
            squares_picture(new_string_of_numbers) # Make new picture by calling squares_picture on new_string_of_numbers
            xor_value = xor(binary_array) # Update xor_value on new binary_array
            turn = False # Change turn to false because user turn is over
            if not(any(squares_array)): # If squares_array has only 0s left, print "Player Won" because game is over and player won
                print("Player Wins!")
        else:
            print("\nComputer Turn\nThinking...")
            time.sleep(1) 
            row = random.randint(1, len(squares_array)) # Set row to random row
            while squares_array[row - 1] == 0:  # While the row in square_array is 0, continue choosing a random row until it finds one that isn't 0
                row = random.randint(1, len(squares_array))  
            num_of_squares = random.randint(1, squares_array[row - 1]) # Set num_of_squares to a random number of squares in from this row
            print("Took " + str(num_of_squares) + " Square(s) from Row " + str(row)) # Print Computer's move
            new_string_of_numbers = ""
            for i in range(len(squares_array)): # Loop through squares_array
                if (i != row - 1): # If i is not equal to row - 1 then add the value in squares_array[i] to new_string_of_numbers
                    new_string_of_numbers = new_string_of_numbers + str(squares_array[i]) + " "
                else:              # If i is equal to row - 1 then add the value in squares_array[i] - num_of_squares to new_string_of_numbers
                    new_string_of_numbers = new_string_of_numbers + str(squares_array[i] - num_of_squares) + " "
            squares_array = [] # Reset squares_array
            binary_array = [] # Reset binary_array
            squares_picture(new_string_of_numbers) # Make new picture by calling squares_picture on new_string_of_numbers
            xor_value = xor(binary_array) # Update xor_value on new binary_array
            turn = True # Change turn to True because user turn is over
            if not(any(squares_array)): # If squares_array has only 0s left, print "Computer Won" because game is over and computer won
                print("Computer Wins!")

# Ask user for the number of squares in each row to generate a picture for the game
squares_picture(input("Enter number of squares in each row (put a space in between each number): "))

# xor value of the binary array
xor_value = xor(binary_array)

# calls squares_game() to start the game
squares_game()