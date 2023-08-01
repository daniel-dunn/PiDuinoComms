from threading import Thread
import serial

import tkinter as tk
from tkinter import ttk



class SerialReaderThread(Thread):
    def __init__(self) -> None:
        super().__init__()
        self.serialValue = None
        
    def run(self) -> None:
            ser = serial.Serial("/dev/ttyACM0", 9600)
            while True:
                bytesToRead = ser.inWaiting()
                input = ser.read(bytesToRead)
                self.serialValue = (input.decode("utf-8"))
            

            
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("display rotary")
        
        
    def handle_serial
        serial_Thread = SerialReaderThread()
        serial_Thread.start()
        
        
def main() -> None:
    
    
    
if __name__ == '__main__':
    main()
        