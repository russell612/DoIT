### Current Version: v0.2.9
### Patch Notes: Changed Layout into multiple lines for easy visibility

import PySimpleGUI as sg
import pickle

from PySimpleGUI.PySimpleGUI import Window

#Global Variables
task_list = ''
saved_file=pickle.load(open('tasklist.txt','rb'))
task_list+=saved_file
empty_list=''
sg.theme('SystemDefaultForReal')
index = 1

#ToDo: Load Function
### Opens the Stored File and Loads it into the Interface.

layout = \
    [[sg.Text("Current Tasks:")],
    [sg.Text(key = "_output_")],
    [sg.Text("Type your Input Here:")], 
    [sg.Input(key = "_input_", do_not_clear=False)], 
    [sg.Button("Add To List"), sg.Button("Randomize Task")], 
    [sg.Button("Complete Task",visible = False, key= '_complete_')],
    [sg.Button("Refresh")],
    [sg.Button("Clear")],
    [sg.Button("Exit")]]
window = sg.Window("To-Do-List-Randomizer", layout)

def add_to_list(task_list, index):
    input = "{} ".format(index) + values["input"] + "\n"
    task_list += input
    index += 1
    window["output"].update(task_list)

print(task_list)

while True:

    event, values = window.read()  
    window["_output_"].update(task_list)


    if event =="Clear":
        filehandler = open('tasklist.txt','wb') 
        task_list=empty_list
        pickle.dump(task_list,filehandler) 
        filehandler.close() #closes the file
        window["_output_"].update(task_list)

    if event =="Refresh":
        window["_output_"].update(task_list)      

    if event == "Randomize Task":
        window['_complete_'].update(visible = True)
        pass #ToDo: randomize function 
            #randomize tasks based on the file given

    if event == "Add To List":
        input = "{} ".format(values["_input_"]) + "\n" # Gives an index with the values from the input text and adds \n to create a new line
        task_list += input # Concatenates it into the task_list string
        index += 1
        window["_output_"].update(task_list)     

    if event == "Exit" or event == sg.WIN_CLOSED:
        filehandler = open('tasklist.txt','wb') #opens tasklist file to save the tasks inputted
        pickle.dump(task_list,filehandler) #saves the the tasks inputted into the tasklist file
        filehandler.close() #closes the file
        break #application stops



window.close()