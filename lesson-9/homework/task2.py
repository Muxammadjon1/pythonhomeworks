import csv
from collections import defaultdict

# Read the data from grades.csv
grades_data = []
with open('grades.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Grade"] = int(row["Grade"])  # Convert grade to integer
        grades_data.append(row)

# Calculate the average grade for each subject
subject_grades = defaultdict(list)

for row in grades_data:
    subject_grades[row["Subject"]].append(row["Grade"])

average_grades = {subject: sum(grades) / len(grades) for subject, grades in subject_grades.items()}

# Write the average grades to a new CSV file
with open('average_grades.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in average_grades.items():
        writer.writerow([subject, round(avg, 2)])

print("Average grades have been saved to 'average_grades.csv'.")