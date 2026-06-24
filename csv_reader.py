import csv
count = 0

with open("employees.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
       row['salary'] = int(row['salary'])
       print(f"{row['name']} earns ${row['salary'] :,}")
       count += 1
    print(f"Total Employees: {count}")


