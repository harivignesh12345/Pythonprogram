Dr. John Wesley maintains a spreadsheet with student records for academic evaluation. The spreadsheet contains various data fields including student IDs, marks, class names, and student names. The goal is to develop a system that can calculate the average marks of all students listed in the spreadsheet.



Problem Statement:

Create a Python-based solution that can parse input data representing a list of students with their respective marks and other details, and compute the average marks. The input may present these details in any order, so the solution must be adaptable to this variability.



Input Format:



The first line contains an integer N, the total number of students.

The second line lists column names in any order (ID, NAME, MARKS, CLASS).

The next N lines provide student data corresponding to the column headers.

Output Format:



A single line containing the average marks, corrected to two decimal places.

Constraints:



1≤N≤100

Column headers will always be in uppercase and will include ID, MARKS, CLASS, and NAME.

Marks will be non-negative integers.



For example:

Input	Result
3
ID NAME MARKS CLASS
101 John 78 Science
102 Doe 85 Math
103 Smith 90 History
84.33
3
MARKS CLASS NAME ID
78 Science John 101
85 Math Doe 102
90 History Smith 103
84.33

N = int(input().strip())

# Read the column headers and find the index of 'MARKS'
headers = input().strip().split()
marks_index = headers.index('MARKS')

# Initialize a variable to store the sum of marks
total_marks = 0

# Read each student's data
for _ in range(N):
    # Split the data into columns
    data = input().strip().split()
    # Add the marks to the total sum
    total_marks += int(data[marks_index])

# Calculate the average marks
average_marks = total_marks / N

# Print the average marks corrected to two decimal places
print(f"{average_marks:.2f}")
Input	Expected	Got	
3
ID NAME MARKS CLASS
101 John 78 Science
102 Doe 85 Math
103 Smith 90 History
84.33
84.33
