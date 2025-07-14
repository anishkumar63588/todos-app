import functions
import PySimpleGUI as sg

label_add = sg.Text("Type in a to-do item")
input_box = sg.InputText(tooltip="Enter item", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key= "todos",
                      size=(45, 10),
                      enable_events=True)
edit_button = sg.Button("Edit")


window = sg.Window(title='Welcome to to-do App',
                   layout=[[label_add],
                           [input_box, add_button],
                           [list_box, edit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()

