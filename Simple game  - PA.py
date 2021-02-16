# Created by Peter Anastasopoulos

user_input1 = input("Let's do some math!!! Please type any 3 characters you like: ")
# First checking whether the condition of 3 characters has been met, a while loop will make sure this always happens
while len(user_input1) != 3:
    user_input1 = input("Please try again, only input 3 characters: ")
# Now testing the type of the input
try:
    # Seeing if it an integer
    user_input1 = int(user_input1)
    type1 = int(user_input1)
    print("Thanks, you typed the integer " + str(user_input1))
except ValueError:
    try:
        # Seeing it its a float
        type1 = float(user_input1)
        user_input1 = float(user_input1)
        print("Thanks, you typed the float " + str(user_input1))
    except ValueError:
        try:
            # Seeing if its a string
            type1 = str(user_input1)
        finally:
            # Ord values are counted one character at a time, hence splitting into 3 values
            user_input1 = ord(user_input1[0]) + ord(user_input1[1]) + ord(user_input1[2])
            print("Thanks, you typed a string, which has been converted to a number by adding its ORD values. "
                  "You will see later why this is done. This value is " + str(user_input1))

user_input2 = input("Now type an integer, this number will be multiplied to your first number: ")
# A while loop is used to repeat this test until a correct input is observed
# Note that a True condition is set as the type from the input of a "input" function is always a string
while True:
    try:
        type2 = int(user_input2)
# This except statement will work for anything that it not an integer
    except ValueError:
        user_input2 = input("That is unfortunately not an integer, please try again: ")
    else:
        # If there is no break, then it is not possible to leave the loop
        break

# Printing the final result
user_input2 = int(user_input2)
result = user_input1 * user_input2
print("Great, the result is " + str(result))
print("Now you know that " + str(user_input1) + " * " + str(user_input2) + ' = ' + str(result))
