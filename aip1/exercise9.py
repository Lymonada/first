import re
import sys

def normalize_data(filename):
    with open(filename) as file:
        data = file.read()

    pattern = r'([a-zA-Z]+),\s*([-\d\s]+),\s*(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)'
    entries = re.split(r'(?<=kr)\s', data)

    students = []
    for entry in entries:
        match = re.search(pattern, entry)
        if match:
            name, phone, email = match.groups()
            name = name.strip()
            phone = phone.replace(" ", "").replace("-", "")
            students.append((name, phone, email))

    students.sort()

    for student in students:
        print(f"{student[0]},{student[1]},{student[2]}")


filename = sys.argv[1]
normalize_data(filename)
