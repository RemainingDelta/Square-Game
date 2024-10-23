squares = input("Enter number of squares in each row (put a space in between each number): ")
squares_array = []
binary_array = []


def squares_picture(number_string):
   # Split the string into individual numbers
   numbers = number_string.split()
  
   # Loop through each number and print the corresponding number of 'X's
   for number in numbers:
       count = int(number)  # Convert the string to an integer
       #print('X' * count)   # Print 'X' repeated 'count' times
       squares_array.append(count)
       binary_array.append(int(bin(count)[2:]))
   print (squares_array)
   print (binary_array)




squares_picture(squares)





