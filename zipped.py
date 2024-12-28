# Input the number of students (n) and subjects (m)
n, m = map(int, input().split())

# Read the marks for each subject
marks = [list(map(float, input().split())) for _ in range(m)]

# Use zip to transpose the marks to group them by student
students_marks = zip(*marks)

# Calculate and print the average marks for each student
for student in students_marks:
    print(f"{sum(student) / m:.1f}")
