import PySimpleGUI as sg
import time
import pyautogui

#autoclicking part of the program
def clicker():
    layout = [  [sg.Text('Enter the time between clicks(in seconds):'), sg.InputText('', size=(10,1), key='in1')],
                [sg.Text('Enter the amount of clicks you want the program to click(leave blank to click until the program is closed): '), sg.InputText('', size=(10,1), key='in2')],
                [sg.Button('Start Clicking!'), sg.Button('Close')]] 

    window = sg.Window('Autoclicker', layout).Finalize()

    # backend clicking part
    while True:
        event, values = window.read()
        if event == 'Close': 
            break
        if event == 'Start Clicking!': 
            a = int(values['in1'])
            b = values['in2']
            c = 0
            while True:
                time.sleep(a)
                pyautogui.click()
                # the part below is very messy,
                # but it was the only way i could make it click forever if left blank
                c = c + 1
                d = str(c)
                if d == b:
                    break
            
    window.close()

#text spamming part of the program
def txtspam():
    layout = [  [sg.Text('Enter name of the file with the script you want to spam (not including extension, extension must be .txt):'), sg.InputText('', size=(10,1), key='in1')],
                [sg.Text('Delay between messages (in seconds, must be decimal number (ex. 0.4, 1.0, etc.)):'), sg.InputText('', size=(10,1), key='in2')],
                [sg.Text('Time to select the chatbox you want the bot to spam in before the bot start spamming (in seconds, must be a full number (ex. 3, 5, etc.)):'), sg.InputText('', size=(10,1), key='in3')],
                [sg.Button('Start Spamming!'), sg.Button('Close')]] 

    window = sg.Window('Text Spammer', layout).Finalize()

    # backend spamming part
    while True:
        event, values = window.read()
        if event == 'Close': 
            break
        if event == 'Start Spamming!':
            fname = values['in1']
            dtime = float(values['in2'])
            wtime = int(values['in3'])
            time.sleep(wtime)
            f = open(fname + ".txt", "r")
            for word in f:
                pyautogui.typewrite(word)
                pyautogui.press("enter")
                time.sleep(dtime)

    window.close()

# program color theme
sg.theme('Black')

# main menu
layout = [[sg.Text("Pick what you want to use:")], [sg.Button("Autoclicker")], [sg.Button("Text Spammer")], [sg.Button("Close")]]

window = sg.Window("ClickNSpam", layout)

while True:
    event, values = window.read()
    if event == "Close" or event == sg.WIN_CLOSED:
        break
    if event == "Autoclicker":
        clicker()
    if event == "Text Spammer":
        txtspam()

window.close()
