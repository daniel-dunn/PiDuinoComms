import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import tkinter
import serial
from tkinter import filedialog


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Display Serial Output From Arduino")
      


        self.save_button = Button(self,text = "Save", command = self.save_text)
        self.save_button.grid(row=0,column=0, sticky="nsew")
        self.clear_button = Button(self, text = "Clear", command = self.clear_text)
        self.clear_button.grid(row=0,column=1, sticky="nsew")
        
        
        self.textbox = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.textbox.grid(row=1, column = 0, columnspan = 2)


       

        try:
            ser = serial.Serial("/dev/ttyACM0", 9600)
            self.textbox.after(100, self.ReadSerial)
        except serial.SerialException:

            self.textbox.insert(tk.INSERT, "Serial unavailable")
            print("Serial unavailable")

    def ReadSerial(self):
        if(ser.in_waiting > 0):
            input = ser.readline()
            text = input.decode('utf-8').rstrip()
            self.textbox.insert(tk.INSERT, text + ',')
            self.textbox.update_idletasks
        self.textbox.after(100, self.ReadSerial)

    def save_text(self):
        print("save pressed")
        textBoxContents = self.textbox.get("1.0", tk.END)
        print(textBoxContents)
        file = filedialog.asksaveasfile(title = "Save File", defaultextension=".txt")

        if file:
            file.write(textBoxContents)
            file.close()

    def clear_text(self):
        print ("clear pressed")
        self.textbox.delete("1.0", tk.END)
        
        

if __name__ == "__main__":
    app = App()
    app.mainloop()