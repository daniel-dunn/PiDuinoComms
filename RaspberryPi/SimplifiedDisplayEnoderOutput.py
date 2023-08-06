import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import serial
ser = serial.Serial("/dev/ttyACM0", 9600)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Display Serial Output From Arduino")
        self.geometry('600x300+100+100')
        self.textbox = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.textbox.pack()
        self.textbox.after(100, self.ReadSerial)

    def ReadSerial(self):
        if(ser.in_waiting > 0):
            input = ser.readline()
            text = input.decode('utf-8').rstrip()
            self.textbox.insert(tk.INSERT, text + ',')
            self.textbox.pack()
        self.textbox.after(100, self.ReadSerial)


if __name__ == "__main__":
    app = App()
    app.mainloop()