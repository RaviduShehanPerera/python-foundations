print ("===Expense Tracker===")
expenses =[]

while True:

    command = input("Add, Show, Summary, Quit ? ")
    command = command.lower()

    if command == "quit":
        break
    elif command =="add":
        category = input("category? ")

        amount = input("amount ?")
        amount = float(amount) 

        description = input("description?")

        expense = {"category" : category, "amount" : amount, "description": description}

        expenses.append(expense)

    elif command == "show":
        for key,value in enumerate(expenses):
            print (f"{key+1} . {value['category']} : {value['amount']}-{value['description']}")

    elif command == "summary":

        totals = {}
        category_counts = {}

        for expense in expenses:
            cat = expense["category"]

            if cat in totals:
                category_counts[cat] += 1
                totals[cat] += expense["amount"]

            else:

                category_counts[cat] = 1
                totals[cat] = expense["amount"]

        print ("spending by category : ")
        for cat in totals:
            print(f"{cat}: ${totals[cat]:.2f} ({category_counts[cat]} expenses)")
                
        total = sum(totals.values())
        print(f'total spent: ${total:.2f}')
 
print("Goodbye!")                








