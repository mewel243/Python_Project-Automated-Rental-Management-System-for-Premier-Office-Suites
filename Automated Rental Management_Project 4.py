'''
NAME: Mewel Mbalanda
Date: 06 OCT 24
PROJ: Four
DESC: Automated Rental Management System for Premier Office Suites 
'''




# This prints out a header row
print("     Floor Unit Month Rent")

# Example of a for loop


# import the operating system package
import os
# clear the screen
os.system ('cls')  # For Windows # For macOS and and Linux ... os. system('clear)

# loop 
for floor in range(1, 16):  # this will account for each floor
    # this prints out a header row
    print("       Floor Unit  Month Rent")
    for room in range (1, 5):  # this will account for each room
        for month in range (1,  13): # go through each month 
            rent = (500 + (floor * 100) - 100)
            if (room == 1 or room == 4):
                rent += 200         # same as: rent = rent + 200
            print(f"{floor:>6.0f}", f"{room:>6.0f}", \
                  f"{month:>6.0f}", f"{rent:>6.0f}")
        print("----------------")
    print("")