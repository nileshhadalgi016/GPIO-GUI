import RPi.GPIO as GPIO
import tkinter as tk
import time

# window

def RPi_program():
    GPIO.setwarnings(False)
    times = time_entry.get()
    times = int(times)
    delays = delay_entry.get()
    delays = int(delays)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    while(times > 0):

        GPIO.output(18,True)
        time.sleep(delays)
        GPIO.output(18,False)
        time.sleep(delays)
        times = times-1
        print(times)
        if (times == 1):
            tk.Label(root,text = "Done",font= "times 20",fg = "green").grid(row = 4, column = 0, columnspan=2)
    GPIO.cleanup()  



root = tk.Tk()
root.title("RPi GPIO controlling GUI")
root.geometry("600x250")
tk.Label(root,text="GUI based RPi GPIO control system", font = 'Times 30').grid(row = 0 ,column = 0, columnspan = 2)
tk.Label(root,text = "Enter the number of blinks:",font = 'Times 20' ).grid(row = 1 ,column = 0,sticky='E')
tk.Label(root,text = "Enter the time delay:",font = 'Times 20' ).grid(row = 2 ,column = 0,sticky='E')

time_entry = tk.Entry(root)
time_entry.grid(row = 1 ,column = 1,sticky='W')
delay_entry = tk.Entry(root)
delay_entry.grid(row = 2 ,column = 1,sticky='W')
tk.Button(root , text= "Play", font = "Times 20",width = "20", height = "1", command = RPi_program ).grid(row = 3 ,column = 0, columnspan = 2)


root.mainloop()

