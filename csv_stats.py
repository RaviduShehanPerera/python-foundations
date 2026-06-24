import csv

salaries = []
names =[]
ages =[]
employees = 0

with open("employees.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        salaries.append(int(row['salary']))
        names.append(row['name'])
        ages.append(int(row['age']))
        employees += 1
                    
                    
    print ("===Employee Statistics===")



Total_salary = sum(salaries)
Ave_salary = sum(salaries)/(employees)


Average_age = sum(ages)/employees

highest_index = salaries.index(max(salaries))
lowest_index = salaries.index(min(salaries))

print (f"Total employees : {len(names)}")
print (f"Average salary: ${Ave_salary :,}")
print (f"Highest salary : ${max(salaries) :,} ({names[highest_index]})")
print (f"Lowest salary: $ {min(salaries) :,} ({names[lowest_index]})")
print(f"Average age: {Average_age:.2f}")
