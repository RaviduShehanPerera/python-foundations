print("==To-Do List==")

todos =[]

while True:
    command = input ("choose one of the following commands: add,remove,show,quit: ")
    command = command.lower()

    if command =='quit':
        break 

    elif command =='add':
        task =input("What do you want to add? ")
        todos.append(task)
        print(f"Added todos: {task}")

    elif command =='remove':
        task = input("what do you want to remove? ")
        todos.remove(task)
        print(f"Removed todos: {task}")

    elif command == "show":
        for index , task in enumerate(todos):
            print(f"{index + 1}. {task}")

print ("Goodbye")

