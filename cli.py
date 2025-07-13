# Building a todos app

# Importing necessary modules
import functions
import time

# Printing current time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("Welcome to to-do app!")
print("It is ", now)

# Creating a loop to ask user input repeatedly until user exits
while True:

    # Taking user input
    user_action = input("Type 'add', 'edit', 'show', 'complete', and 'exit': ").lower().strip()

    # Applying a condition to add to-do
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    # Applying a condition to show todos
    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1} - {item.capitalize().strip()}")

    # Applying a condition to edit to-do
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()
            new_todo = input("Enter the new to-do: ").lower().strip()

            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    # Applying a condition to remove the completed to-do
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = functions.get_todos()

            c_todo = todos.pop(number)

            functions.write_todos(todos)
            print(f"The task '{c_todo.strip()}' has been removed.")
        except IndexError:
            print("Wrong number of to-do!")

    # Applying a condition to exit the loop
    elif user_action == "exit":
        break

    else:
        print("Wrong command, try again!")  # This will be printed when user will enter wrong input

print("Thanks for using todos app!")