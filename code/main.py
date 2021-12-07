### Current Version: v0.2.3
### Patch Notes: Added task_list integration into the GUI, which causes dynamic addition of the tasks


import PySimpleGUI as sg
import pickle

#Global Variables
task_list = ''
sg.theme('SystemDefaultForReal')
index = 1

#ToDo: Load Function
### Opens the Stored File and Loads it into the Interface.

layout = [[sg.Text("Current Tasks:")],[sg.Text(key = "output")],[sg.Text("Type your Input Here:")], [sg.Input(key = "input")], [sg.Button("Add To List"), sg.Button("Randomize Task"), sg.Button("Exit")]]
window = sg.Window("To-Do-List-Randomizer", layout)

while True:
    event, values = window.read()
    if event == "Randomize Task":
        pass #ToDo: randomize function 
            #randomize tasks based on the file given
    if event == "Add To List":
        input = "{}. ".format(index) + values["input"] + "\n"
        task_list += input
        index += 1
        window["output"].update(task_list)       
    if event == "Exit" or event == sg.WIN_CLOSED:
        filehandler = open('tasklist.txt','wb')
        pickle.dump(task_list,filehandler)
        filehandler.close()
        break #ToDo: Save function 


window.close()