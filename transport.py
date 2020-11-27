from tkinter import Tk
import socket
PORT = 3872

SELF = "one-ip-here"
OTHER = "the-other-ip-here"

def send(IP):
    sender = socket.socket()
    sender.connect((IP,PORT))
    data = Tk().clipboard_get().encode()
    sender.send(data)
    sender.close()

def receive(IP):
    receiver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    receiver.bind((IP,PORT))
    receiver.listen()

    
    c, addr = receiver.accept()
    data = c.recv(100000)
    print(data)
    clip = data.decode()
    root = Tk()
    root.withdraw()
    root.clipboard_clear()
    root.clipboard_append(clip)
    print(addr)
    c.close()


import PySimpleGUI as sg

sg.theme("Dark")

layout=[
    [sg.Button("Send"), sg.Button("Receive"), sg.Button("Cancel")]
]

window = sg.Window("Share Clipboard", layout, size=(500,100), element_justification='c')

while True:
    event, values = window.read()
    if event == "Send":
        print("sending...")
        send(PC)
    if event == "Receive":
        print("receiving...")
        receive(LAPTOP)
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
        
window.close()

