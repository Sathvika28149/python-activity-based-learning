# University Scholarship Allocation System

students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")

    m1 = float(input("Enter marks in Subject 1: "))
    m2 = float(input("Enter marks in Subject 2: "))
    m3 = float(input("Enter marks in Subject 3: "))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    aggregate = (m1 + m2 + m3) / 3

    if (aggregate >= 75 and
        m1 >= 60 and m2 >= 60 and m3 >= 60 and
        attendance >= 75 and income <= 250000):

        students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

# Sort by aggregate, attendance, and income
students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"]
    )
)

# Display results
if students:
    print("\n--- Eligible Students ---")

    for rank, s in enumerate(students, start=1):
        print("\nRank:", rank)
        print("Name:", s["name"])
        print("Aggregate:", round(s["aggregate"], 2), "%")
        print("Attendance:", s["attendance"], "%")
        print("Family Income: Rs.", s["income"])
else:
    print("\nNo students are eligible for the scholarship.")
