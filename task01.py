#!python3
# Create a user interface to have the user enter in data for a teacher
# Use the menu options below to help navigate your program:
# User input has been encloded by _ _
"""
1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 1_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 0

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _0_
Enter in the scores for 10 students for Assignment 1:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_
Complete.

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _1_
Enter the assignment name: _Assignment 2_
Enter in Assignment Value: _10_
Your assignment has been assigned ID 1

1. Create an Assignment
2. Enter in Assignment Scores
3. Write your data to file

Enter in your choice: _2_
Enter in the assignment ID: _1_

Enter in the scores for 10 students for Assignment 2:
1: _8_
2: _7_
3: _7_
4: _6_
5: _9.5_
6: _10_
7: _10_
8: _9_
9: _11_
10: _12_

"""


class task1:
    def __init__(self):
        self.part2()

    def part1(self):
        choice = input("Enter your choice")
        value = input("Enter in the assignment ID:")
        print("Enter in the scores for the 10 students for Assignment 2:")

    def part2(self):
        import json
        choice = input("Enter your choice")
        id = input("Enter in the assignment ID:")
        print("Enter in the scores for the 10 students for Assignment 2:")

        score = {}
        score["Assignment Value"] = id
        score["Assignment Name"] = name
        print(score)

        for i in range(1,11):
            score[i] = input(f"{i}: ")
        print(score)
            
            
        print("Complete.")

        encoded = json.dumps(score)
        data = open(f"{name}.txt","w")
        data.write(f"{encoded}")
        data.close()
    

task1()
