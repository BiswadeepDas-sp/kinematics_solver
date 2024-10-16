 This code solves for the five kinematic variables of motion: 
# Initial Velocity (i_vel), Final Velocity (f_vel), Acceleration (acc), 
# Distance (dis) and Time (time). 

# The user is prompted to enter values for four of the variables.
# The program will then attempt to solve for the missing variable.
# If more than two variables are unknown, the program will indicate that it cannot solve the problem.
#
# Here's a breakdown of the functions:
#
# 1. input_params():
#    - Takes user input for the five kinematic variables.
#    - Returns a list of the entered values.
#
# 2. solvable():
#    - Checks if the number of unknown variables is less than or equal to 2.
#    - If solvable, returns False.
#    - If not solvable, returns True and sets the not_solvable variable to True. 
#
# 3. to_find():
#    - Identifies the unknown variables from the user input.
#    - Returns a list of the unknown variables.
#
# 4. cannot_solve():
#    - Prints a message indicating the problem cannot be solved.
#
# 5. solve_i_vel() to solve_time():
#    - These functions are used to solve for each individual variable 
#      based on the known values.
#    - Each function includes multiple try-except blocks to handle various 
#      combinations of known variables.
#
# 6. solve(param_values):
#    - Solves for the unknown variable using the appropriate solve function.
#    - Updates the param_values list with the solved values.
#    - Returns the updated list.
#
# 7. main():
#    - Calls the necessary functions to gather user input, check solvability, 
#      solve for the missing variable, and print the results.
#    - If the problem is unsolvable, prints an error message. 
#
# Usage:
# 1. Run the code.
# 2. Enter values for the four known variables.
# 3. The code will output the calculated value for the missing variable.
# 4. If more than two variables are unknown, the code will display an error message.
