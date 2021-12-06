import PySimpleGUI as sg
import pickle

#ToDo: Load Function
### Opens the Stored File and Loads it into the Interface.

input = [sg.Input()]

layout = [[sg.Text("Type your Input Here:")], input, [sg.Button("Add To List")], [sg.Button("Randomize Task")], [sg.Button("Exit")]]
window = sg.Window("To-Do-List-Randomizer", layout)

while True:
    event, values = window.read()
    if event == "Randomize Task":
        pass #ToDo: randomize function
    if event == "Add To List":
        pass #ToDo: addToList function
    if event == "Exit" or event == sg.WIN_CLOSED:
        break #ToDo: Save function 


window.close()