from project import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("Welcome to to-do app!")
print("It is ", now)

while True:
    user_action = input("Type 'add', 'edit', 'show', 'complete', and 'exit': ").lower().strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1} - {item.capitalize().strip()}")

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

    elif user_action == "exit":
        break

    else:
        print("Wrong command, try again!")

print("Bye!")