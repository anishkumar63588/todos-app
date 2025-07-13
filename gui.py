import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do item")
input_box = sg.InputText(tooltip="Enter item")
add_button = sg.Button("Add")

window = sg.Window('My to-do App!', layout=[[label], [input_box, add_button]])
window.read()
window.close()