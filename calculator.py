import tkinter
from turtle import back, window_width # GUI

# Structure of the calc
button_values = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "ok", "="]
]

right_symbols = ["+", "x", "-", "="]        #separate list to identify them later    
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)       # track of rows and columns
column_count = len(button_values[0]) #4

# colors
color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

#window setup
window = tkinter.Tk()       #create the window
window.title("Calculator")
window.resizable(False, False)      # width and height

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text ="0", font=("Arial", 45), background=color_black,
                     foreground=color_white)

label.grid(row=0, column=0)

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                window_width=column_count-1, heigth=1)

frame.pack() 

window.mainloop()

