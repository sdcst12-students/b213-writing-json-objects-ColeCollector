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
        while True:
            print("\n\n\n1. Create an Assignment")
            print("2. Enter in Assignment Scores")
            choice = input("\nEnter your choice: ")
            if choice == "1":
                self.choice1()
            elif choice == "2":
                self.choice2()
            else:
                print("That's not a valid choice")

    def choice1(self):
        import json
        name = input("Enter the assignment name:")
        value = input("Enter the assignment value:")
        line = open("data.csv","r").read().split("\n")
        info = json.dumps({"id":len(line)-1,"assignmentName" : name, "assignmentValue" : value})
        print(f"Your assignment has been assigned ID {len(line)-1}")
        data = open("data.csv","a")
        data.write(f"{info}\n")
        data.close()

    def choice2(self):
        import json
        id = int(input("Enter in the assignment ID:"))
        line = open("data.csv","r").read().split("\n")
        
        if len(line)-2 < id:
            print("ID is too high")
            exit()

        x = json.loads(line[id])
        name = x['assignmentName']
        
        print(f"Enter in the scores for the 10 students for {name}:")

        for i in range(1,11):
            grade = input(f"{i}: ")
            x[f"{i}"] = grade
    
        data = open("data.csv","w")
        for i in line:
            if line.index(i) == id:
                data.write(f"{x}\n")

            elif i!="":
                data.write(f"{i}\n")

        data.close()
        print("Complete.")

task1()