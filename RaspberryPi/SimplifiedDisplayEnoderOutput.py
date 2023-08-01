import tkinter as tk
from tkinter import ttk
import serial
import time
ser = serial.Serial("/dev/ttyACM0", 9600)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Display Serial Output From Arduino")
        self.geometry('600x300+100+100')
        self.label = ttk.Label(self, text='Default')
        self.label.pack()
        self.label.after(500,self.ReadSerial)
        
        
    def ReadSerial(self):
        input = ser.read()
        text = input.decode("utf-8")
        self.label['text'] = text
        self.label.pack()
        self.label.after(500, self.ReadSerial)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()