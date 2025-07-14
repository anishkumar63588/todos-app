import functions
import FreeSimpleGUI as sg
import time

sg.theme("NeonYellow1")
clock = sg.Text("", key="clock")
label_add = sg.Text("Type in a to-do item")
input_box = sg.InputText(tooltip="Enter item", key="todo")
add_button = sg.Button("Add", size=5)
list_box = sg.Listbox(values=functions.get_todos(),
                      key= "todos",
                      size=(45, 10),
                      enable_events=True)
edit_button = sg.Button("Edit", size=6)
complete_button = sg.Button("Complete", size=10)
exit_button = sg.Button("Exit", size=6)

window = sg.Window(title='Welcome to to-do App',
                   layout=[[clock],
                           [label_add],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo

                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                index = todos.index(todo_to_complete)
                todos.pop(index)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])

print("Thanks for using To-Do App")
window.close()

