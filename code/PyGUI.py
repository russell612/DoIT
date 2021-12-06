import PySimpleGUI as sg
import pickle

input = [sg.Input()]

layout = [[sg.Text("Type your Input Here:")], input, [sg.Button("Add To List")], [sg.Button("Exit")]]
window = sg.Window("To-Do-List-Randomizer", layout)

while True:
    event, values = window.read()
    if event == "Add To List":
        pass #ToDo: addToList function
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()