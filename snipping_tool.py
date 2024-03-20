from tkinter import *
from tkinter import ttk
import pyautogui
import datetime
import os


def take_screenshot():
    
    if not os.path.exists('snippet'):
        os.makedirs('snippet')
    
    try:
        screenshot = pyautogui.screenshot()
        file_name = datetime.datetime.now().strftime("%f")
        screenshot.save("snippet/" + file_name + ".png")
    except pyautogui.FailSafeException as error:
        print("Failed to take a screenshot:", error)

class Snipping_Tool:
    def __init__(self):
        self.root = Tk()
        self.root.title("Snipping Tool")
        
        self.mainframe = ttk.Frame(self.root, padding="10 10 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N,W,S,E))
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0, weight=1)
        
        ttk.Label(self.mainframe, text="Click to Screenshot").grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Button(self.mainframe, text="Screenshot", command=take_screenshot).grid(column=0, row=1, sticky=(N, W, E, S))

        self.mainframe.grid_configure(padx=10, pady=10)

        self.root.mainloop()
    
if __name__ =='__main__':
    app = Snipping_Tool()