### Current Version: v0.2.8
### Patch Notes: Added Comments

import PySimpleGUI as sg
import pickle

from PySimpleGUI.PySimpleGUI import Window

#Global Variables
task_list = ''
sg.theme('SystemDefaultForReal')
index = 1

#ToDo: Load Function
### Opens the Stored File and Loads it into the Interface.

layout = [[sg.Text("Current Tasks:")],[sg.Text(key = "output")],[sg.Text("Type your Input Here:")], [sg.Input(key = "input", do_not_clear=False)], [sg.Button("Add To List"), sg.Button("Randomize Task")], [sg.Button("Complete Task",visible = False, key= '_complete_')],[sg.Button("Exit")]]
window = sg.Window("To-Do-List-Randomizer", layout)

def add_to_list(task_list, index):
    input = "{}. ".format(index) + values["input"] + "\n"
    task_list += input
    index += 1
    window["output"].update(task_list)

while True:
    event, values = window.read()  
    if event == "Randomize Task":
        window['_complete_'].update(visible = True)
        pass #ToDo: randomize function 
            #randomize tasks based on the file given
    if event == "Add To List":
        input = "{}. ".format(index) + values["input"] + "\n" # Gives an index with the values from the input text and adds \n to create a new line
        task_list += input # Concatenates it into the task_list string
        index += 1
        window["output"].update(task_list)     
    if event == "Exit" or event == sg.WIN_CLOSED:
        filehandler = open('tasklist.txt','wb') #opens tasklist file to save the tasks inputted
        pickle.dump(task_list,filehandler) #saves the the tasks inputted into the tasklist file
        filehandler.close() #closes the file
        break #application stops


window.close()