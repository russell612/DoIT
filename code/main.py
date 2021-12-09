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
<<<<<<< HEAD
    [[sg.Text("Current Tasks:")],
    [sg.Listbox(values=task_list, size=(40, 10), key="items"), sg.Button('Delete'), sg.Button('Edit')],
    [sg.Text("Your Randomized Task is:")],
    [sg.Text(key="_random_")],
    [sg.Button("Randomize Task"), sg.Button("Complete Task")],
    [sg.Text("Type your Input Here:")], 
    [sg.Input(key = "_input_", do_not_clear=False)], 
    [sg.Button(button_text='Add', key="Add To List"), sg.Button("Clear"), sg.Button("Exit")]]
=======
    [[sg.Text("Current Tasks:",font=fontt)],
    [sg.Text(key = "_output_",font=fontt)],
    [sg.Text("Your Randomized Task is:",font=fontt)],
    [sg.Text(key="_random_",font=fontt)],
    [sg.Button("Randomize Task",button_color=('black','grey80')), sg.Button("Complete Task",button_color=('black','grey80'))],
    [sg.Text("Type your Input Here:",font=fontt)], 
    [sg.Input(key = "_input_", do_not_clear=False)], 
    [sg.Button("Add To List",button_color=('black','grey80')), sg.Button("Clear",button_color=('black','grey80')), sg.Button("Exit",button_color=('black','grey80'))]]
>>>>>>> cd7159ecae4844faa6aaba3d748d15955a9a4f65
window = sg.Window("To-Do-List-Randomizer", layout, finalize=True)
window["_input_"].bind("<Return>", "enter")


def chgstr(s): 
    str1 = ""    
    for ele in s: 
        str1 += ele +"\n"  
    return str1 
        
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
<<<<<<< HEAD
    window["items"].update(task_list.splitlines())
    window["_random_"].update(specific_task + " : DONE")
=======
    window["_output_"].update(task_list)
    window["_random_"].update(specific_task + " : DONE :)")
>>>>>>> cd7159ecae4844faa6aaba3d748d15955a9a4f65
    



window["items"].update(task_list.splitlines())
while True:

    event, values = window.read()  
    window["items"].update(task_list.splitlines())


    if event =="Clear":
        filehandler = open('tasklist.txt','wb') 
        task_list=empty_list
        pickle.dump(task_list,filehandler) 
        filehandler.close() #closes the file
        is_clear = True
        window["_random_"].update("")
        window["items"].update(task_list)    
        

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
<<<<<<< HEAD
        window["items"].update("Congratulations, you have completed all your task_list!")
=======
        window["_output_"].update("Congratulations, you have completed all your tasks! *confetti*")
>>>>>>> cd7159ecae4844faa6aaba3d748d15955a9a4f65
        
        
    if event == "Add To List" or event == "_input_" + "enter":
        input = "{}".format(values["_input_"])+ "\n"  # Gives an index with the values from the input text and adds \n to create a new line
        if len(input.strip().strip('\n')) != 0:
            if input.strip() in task_list.splitlines():
                sg.popup("Task already exists (x.x)",title='',font=fontt)
            else:
                task_list += input # Concatenates it into the task_list string
                program_counter += 1
                is_clear = False
                window["items"].update(task_list.split())  
        else:
<<<<<<< HEAD
            sg.popup("Please input a valid task!")  
        window.find_element('Add To List').Update("Add")
        
    elif event == "Delete" and len(task_list) > 0:


        splitted=task_list.splitlines()
        splitted.remove(values["items"][0])
        window.find_element('items').Update(values=splitted)
        task_list=chgstr(splitted)


    elif event == "Edit" and len(task_list) > 0:
        edit_val = values["items"][0]
        splitted=task_list.splitlines()
        splitted.remove(values["items"][0])
        window.find_element('items').Update(values=splitted)
        window.find_element('_input_').Update(value=edit_val)
        window.find_element('Add To List').Update("Save")
        task_list=chgstr(splitted)

=======
            sg.popup("Please input a valid task!",title='',button_color=('black','grey80'),font=fontt)  
>>>>>>> cd7159ecae4844faa6aaba3d748d15955a9a4f65


    if event == "Exit" or event == sg.WIN_CLOSED: 
        filehandler = open('tasklist.txt','wb') #opens tasklist file to save the task_list inputted
        pickle.dump(task_list,filehandler) #saves the the task_list inputted into the tasklist file
        filehandler.close() #closes the file
        break #application stops


    if program_counter != 0 and len(task_list) == 0 and is_clear != True:
<<<<<<< HEAD
        window["_random_"].update("Congratulations, you have completed all your task_list!")
=======
        window["_output_"].update("Congratulations, you have completed all your tasks! \(0^0)/")
>>>>>>> cd7159ecae4844faa6aaba3d748d15955a9a4f65

    
    if program_counter != 0 and len(task_list) == 0 and is_clear == True:
        window["_random_"].update("You have cleared all task_list. Please input task_list.")



window.close()