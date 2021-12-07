### Current Version: v0.1.5
### Patch Notes: Added Text for Current Tasks in the GUI


import PySimpleGUI as sg
import pickle

#Global Variables
task_list = []
sg.theme('SystemDefaultForReal')

#ToDo: Load Function
### Opens the Stored File and Loads it into the Interface.

layout = [[sg.Text("Current Tasks:")],[sg.Text("Type your Input Here:")], [sg.Input(key = "input")], [sg.Button("Add To List"), sg.Button("Randomize Task"), sg.Button("Exit")]]
window = sg.Window("To-Do-List-Randomizer", layout)

while True:
    event, values = window.read()
    if event == "Randomize Task":
        pass #ToDo: randomize function 
            #randomize tasks based on the file given
    if event == "Add To List":
        input = values("input")
        task_list.append(input)       
    if event == "Exit" or event == sg.WIN_CLOSED:
        break #ToDo: Save function 


window.close()