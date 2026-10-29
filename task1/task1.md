# Problem Statement
To develop a Python program for a University Scholarship Allocation System that evaluates students based on aggregate marks, subject-wise minimum marks, attendance percentage, and family annual income. The system identifies eligible students, ranks them according to their academic performance, and resolves ties using predefined rules.
# Algorithm
1. Start the program.
2. Read the number of students.
3. For each student, enter their name, subject marks, attendance percentage, and annual family income.
4. Calculate the aggregate percentage of marks.
5. Check whether the student satisfies all the eligibility criteria:
   - Aggregate percentage must be at least 75%.
   - Each subject mark must be at least 60%.
   - Attendance must be at least 75%.
   - Annual family income must not exceed ₹2,50,000.
6. If all conditions are satisfied, mark the student as eligible.
7. Rank eligible students according to aggregate percentage in descending order.
8. If two students have the same aggregate percentage, give priority to the student with higher attendance. If attendance is also equal, give priority to the student with lower family income.
9. Display the eligible students, their marks, and their ranks.
10. Display a message if no students are eligible.
11. Stop the program.
Note: The eligibility limits and tie-breaking rules above are example rules for this project. Actual scholarship policies may use different criteria
```mermaid flowchart
flowchart TD
    A([Start]) --> B[/Enter number of students/]
    B --> C[/Enter student details and marks/]
    C --> D[Calculate aggregate percentage]
    D --> E{All eligibility conditions satisfied?}
    E -- Yes --> F[Add student to eligible list]
    E -- No --> G[Mark student as not eligible]
    F --> H{More students?}
    G --> H
    H -- Yes --> C
    H -- No --> I[Sort eligible students by marks, attendance and income]
    I --> J{Any eligible students?}
    J -- Yes --> K[Display ranked eligible students]
    J -- No --> L[Display No eligible students]
    K --> M([Stop])
    L --> M
```
# Sample Input
For example, enter the following details when running the program.
Enter number of students: 2

Enter details of Student 1
Enter student name: Ravi
Enter marks in Subject 1: 85
Enter marks in Subject 2: 80
Enter marks in Subject 3: 90
Enter attendance percentage: 90
Enter annual family income: 200000

Enter details of Student 2
Enter student name: Priya
Enter marks in Subject 1: 90
Enter marks in Subject 2: 85
Enter marks in Subject 3: 95
Enter attendance percentage: 95
Enter annual family income: 180000

# Expected Output
--- Eligible Students ---

Rank: 1
Name: Priya
Aggregate: 90.0 %
Attendance: 95.0 %
Family Income: Rs. 180000.0

Rank: 2
Name: Ravi
Aggregate: 85.0 %
Attendance: 90.0 %
Family Income: Rs. 200000.0
