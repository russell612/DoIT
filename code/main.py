### Current Version: v0.3.0
### Patch Notes: Tweaked GUI, moved to version 0.3.0 as most features are complete
import PySimpleGUI as sg
import pickle
import random

from PySimpleGUI.PySimpleGUI import Window

#Global Variables
task_list = ''
saved_file=pickle.load(open('tasklist.txt','rb'))
task_list+=saved_file
empty_list= ''
specific_task = ''
sg.theme('SystemDefaultForReal')
index = 1

#ToDo: Load Function
### Opens the Stored File and Loads it into the Interface.

layout = \
    [[sg.Text("Current Tasks:")],
    [sg.Text(key = "_output_")],
    [sg.Text("Your Randomized Task is:")],
    [sg.Text(key="_random_")],
    [sg.Button("Randomize Task"), sg.Button("Complete Task",visible = False, key= '_complete_')],
    [sg.Text("Type your Input Here:")], 
    [sg.Input(key = "_input_", do_not_clear=False)], 
    [sg.Button("Add To List")], 
    [sg.Button("Clear")],
    [sg.Button("Exit")]]
window = sg.Window("To-Do-List-Randomizer", layout, finalize=True)

# def add_to_list(task_list, index):
#     input = "{} ".format(index) + values["input"] + "\n"
#     task_list += input
#     index += 1
#     window["output"].update(task_list)


def randomize(string_list):
    hash = random.getrandbits(64)
    list_to_randomize = string_list.splitlines()
    while hash % 47 != 0:
        hash = random.getrandbits(64)
        random.shuffle(list_to_randomize)

    return list_to_randomize

def task_random(string_list):
    randomized_list = randomize(string_list)
    specific_task = randomized_list.pop(0)
    task_list = empty_list
    # for task in randomized_list:
    #     task_list += "{} ".format(task) + '\n'
    window["_random_"].update(specific_task)
    # window["_output_"].update(task_list)

    return task_list
    

print(task_list)
window["_output_"].update(task_list)
while True:

    event, values = window.read()  
    window["_output_"].update(task_list)


    if event =="Clear":
        filehandler = open('tasklist.txt','wb') 
        task_list=empty_list
        pickle.dump(task_list,filehandler) 
        filehandler.close() #closes the file
        window["_output_"].update(task_list)     


    if event == "Randomize Task":
        window['_complete_'].update(visible = True)
        task_random(task_list)


    if event == "Add To List":
        input = "{} ".format(values["_input_"]) + "\n" # Gives an index with the values from the input text and adds \n to create a new line
        task_list += input # Concatenates it into the task_list string
        window["_output_"].update(task_list)     


    if event == "Exit" or event == sg.WIN_CLOSED:
        filehandler = open('tasklist.txt','wb') #opens tasklist file to save the tasks inputted
        pickle.dump(task_list,filehandler) #saves the the tasks inputted into the tasklist file
        filehandler.close() #closes the file
        break #application stops


window.close()