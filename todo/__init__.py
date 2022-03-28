__version__ = '0.1.0'

tasks = []

choice_prompt = '''\
[0] Exit the program
[1] Create a task
[2] Complete a task
[3] Display all the ongoing tasks
[4] Display all the completed tasks
[5] Delete a task
Select your choice: '''

while True:
    choice = int(input(choice_prompt))

    if choice == 0:  # Exit the program
        break

    elif choice == 1:  # Create a task
        name = input("Name of the task to create: ")
        task = {
            "name": name,
            "complete": False
        }
        tasks.append(task)

    elif choice == 2:  # Complete a task
        name = input("Name of the task to complete: ")
        for task in tasks:
            if task['name'] == name:
                task['complete'] = True

    elif choice == 3:  # Display all the ongoing tasks
        for task in tasks:
            if task['complete'] == False:
                print(task)
    elif choice == 4:  # Display all the completed tasks
        for task in tasks:
            if task['complete'] == True:
                print(task)
    elif choice == 5:  # Delete a task
        name = input("Name of the task to delete: ")
        filtered_tasks = []
        for task in tasks:
            if task['name'] != name:
                filtered_tasks.append(task)
        tasks = filtered_tasks
    print()
