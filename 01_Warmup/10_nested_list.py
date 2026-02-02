# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta
# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.




if __name__ == '__main__':
    # PEHLE LIST DEFINE KARO (Ye missing tha)
    students = []
    
    # 1. Input lene ka loop
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # Data ko list mein bharo
        students.append([name, score])

    # 2. Saare unique scores nikal kar sort karo
    scores = sorted(list(set([s[1] for s in students])))
    
    # 3. Second lowest score pakdo
    second_lowest = scores[1]
    
    # 4. Un students ke naam dhoondo jinka score match kare
    low_scorers = []
    for s in students:
        if s[1] == second_lowest:
            low_scorers.append(s[0])
            
    # 5. Alphabetical order mein sort karke print karo
    low_scorers.sort()
    for name in low_scorers:
        print(name)