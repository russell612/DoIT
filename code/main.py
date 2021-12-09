### Current Version: v0.4.7
### Patch Notes: Improved clear function 

import PySimpleGUI as sg
import pickle
import random

#Global Variables
task_list = ''
saved_file=pickle.load(open('tasklist.txt','rb'))
task_list+=saved_file
empty_list= ''
specific_task = ''
is_done = True
is_clear = True
program_counter = 0

#window design
fontt = ('Lato',11)
sg.theme_background_color('grey15')
sg.theme_text_color('white')
sg.theme_button_color('grey80')
sg.theme_text_element_background_color('grey15')

layout = \
    [[sg.Text("Current Tasks:",font=fontt)],
    [sg.Text(key = "_output_",font=fontt)],
    [sg.Text("Your Randomized Task is:",font=fontt)],
    [sg.Text(key="_random_",font=fontt)],
    [sg.Button("Randomize Task",button_color=('black','grey80')), sg.Button("Complete Task",button_color=('black','grey80'))],
    [sg.Text("Type your Input Here:",font=fontt)], 
    [sg.Input(key = "_input_", do_not_clear=False)], 
    [sg.Button("Add To List",button_color=('black','grey80')), sg.Button("Clear",button_color=('black','grey80')), sg.Button("Exit",button_color=('black','grey80'))]]
window = sg.Window("To-Do-List-Randomizer", layout, finalize=True)
window["_input_"].bind("<Return>", "enter")


def randomize(string_list):
    hash = random.getrandbits(64)
    list_to_randomize = string_list.splitlines()
    while hash % 47 != 0:
        hash = random.getrandbits(64)
        random.shuffle(list_to_randomize)
    return list_to_randomize


def task_random(string_list):
    global specific_task
    randomized_list = randomize(string_list)
    specific_task = randomized_list[0]
    window["_random_"].update(specific_task)


def clear_task_after_done(string_list):
    global task_list
    temp_list = string_list.splitlines()
    for task in temp_list:
        if task == specific_task:
            temp_list.remove(task)
    task_list = empty_list
    for leftover in temp_list:
        task_list += "{}".format(leftover) + '\n'
    window["_output_"].update(task_list)
    window["_random_"].update(specific_task + " : DONE :)")
    



window["_output_"].update(task_list)
while True:

    event, values = window.read()  
    window["_output_"].update(task_list)


    if event =="Clear":
        filehandler = open('tasklist.txt','wb') 
        task_list=empty_list
        pickle.dump(task_list,filehandler) 
        filehandler.close() #closes the file
        is_clear = True
        window["_random_"].update("")
        window["_output_"].update(task_list)    
        

    if event == "Randomize Task" and len(task_list) != 0:
        if is_done == True:
            task = task_random(task_list)
            is_done = False
        else:
            sg.popup("Please finish the current task first! No skipping! >:C",title='',button_color=('black','grey80'),font=fontt)
    elif event == "Randomize Task" and len(task_list) == 0:
        sg.popup("Please input a task! There are no current tasks left.",title='',button_color=('black','grey80'),font=fontt)


    if event == "Complete Task" and is_done == False and len(task_list) > 0:
        is_done = True
        clear_task_after_done(task_list)
    elif event == "Complete Task" and program_counter == 0:
       sg.popup("Please input and randomize tasks before completing.",title='',button_color=('black','grey80'),font=fontt)
    elif event == "Complete Task" and len(task_list) == 0:
        window["_output_"].update("Congratulations, you have completed all your tasks! *confetti*")
        
        
    if event == "Add To List" or event == "_input_" + "enter":
        input = "{}".format(values["_input_"]) + "\n" # Gives an index with the values from the input text and adds \n to create a new line
        if len(input.strip().strip('\n')) != 0:
            if input.strip() in task_list.splitlines():
                sg.popup("Task already exists (x.x)",title='',font=fontt)
            else:
                task_list += input # Concatenates it into the task_list string
                program_counter += 1
                is_clear = False
                window["_output_"].update(task_list)  
        else:
            sg.popup("Please input a valid task!",title='',button_color=('black','grey80'),font=fontt)  


    if event == "Exit" or event == sg.WIN_CLOSED: 
        filehandler = open('tasklist.txt','wb') #opens tasklist file to save the tasks inputted
        pickle.dump(task_list,filehandler) #saves the the tasks inputted into the tasklist file
        filehandler.close() #closes the file
        break #application stops


    if program_counter != 0 and len(task_list) == 0 and is_clear != True:
        window["_output_"].update("Congratulations, you have completed all your tasks! \(0^0)/")

    
    if program_counter != 0 and len(task_list) == 0 and is_clear == True:
        window["_output_"].update("You have cleared all tasks. Please input tasks.")



window.close()