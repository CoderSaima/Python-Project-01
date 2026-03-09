

# def add(n1, n2):
#     return n1 + n2
# def subtract(n1, n2):
#     return n1 - n2
# def multiply(n1, n2):
#     return n1 * n2
# def divide(n1, n2):
#     return n1 / n2
# def avg(n1, n2):
#     return (n1 + n2)/2


# print("Select the opreration:\n"
#       "1: Addition\n"
#       "2: Subtraction\n"
#       "3: Multiplication\n"
#       "4: Division\n"
#       "5: Average")
# Operation = int(input("Enter the number 1-5 for doing operation:\n"))

# User_input_01= int(input("Enter the first number for operation\n"))
# User_input_02= int(input("Enter the second number for operation\n"))

# try:
#     if Operation == 1:
#         addition = add(User_input_01, User_input_02)
#         print("The Addition is = ", addition)
#     elif Operation == 2:
#         subtract = subtract(User_input_01, User_input_02)
#         print("The Subtraction is = ", subtract)
#     elif Operation == 3:
#         multiply = multiply(User_input_01, User_input_02)
#         print("The Multipication is = ", multiply)
#     elif Operation == 4:
#         if User_input_01 >= 0 and User_input_02 <= 0:
#             print("Invalid Input n/0, This can't divided")
#         divide = divide(User_input_01, User_input_02)
#         print("The Division is = ", divide)
#     elif Operation == 5:
#         average = avg(User_input_01, User_input_02)
#         print("The Average is = ", average)
#     else:
#         print("Enter the valid input for operations")                    

# except:
#     print("Try Again...")



#.................................... GUI BASED CALCULATOR ....................................
# import tkinter as tk
# import tkinter.messagebox
# from tkinter.constants import SUNKEN

# win = tk.Tk()
# win.title('Calculator')

# frame = tk.Frame(win, bg="pink", padx=40)
# frame.pack()

# entry = tk.Entry(frame, relief=SUNKEN, borderwidth=3, width=30)
# entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

# def click(num):
#     entry.insert(tk.END, num)

# def equal():
#     try:
#         res = str(eval(entry.get()))
#         entry.delete(0, tk.END)
#         entry.insert(0, res)
#     except:
#         tk.messagebox.showinfo("Error", "Syntax Error")

# def clear():
#     entry.delete(0, tk.END)

# buttons = [
#     ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
#     ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
#     ('0', 4, 1), ('+', 5, 0), ('-', 5, 1),
#     ('*', 5, 2), ('/', 6, 0)
# ]

# for txt, r, c in buttons:
#     tk.Button(frame, text=txt, padx=15, pady=5, width=3, command=lambda t=txt: click(t)).grid(row=r, column=c, pady=2)

# tk.Button(frame, text="Clear", padx=15, pady=5, width=12, command=clear).grid(row=6, column=1, columnspan=2, pady=2)
# tk.Button(frame, text="=", padx=15, pady=5, width=9, command=equal).grid(row=7, column=0, columnspan=3, pady=2)

# win.mainloop()



import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

# win = tk.TK()
# win.title('Calculator')
win = tk.Tk()
win.title('Calculator')

frame =  tk.Frame(win, padx = "30px", bg="grey")
frame.pack()

entry = tk.Entry(frame, relief=SUNKEN, width=30, borderwidth=3)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

def click(num):
    entry.insert(tk.END, num) 

def equal():
    try:
        res = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, res)
    except:
        tk.messagebox.showinfo("SyntaxError", "Error")

def clear():
    entry.delete(0, tk.END)  


buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
    ('0', 4, 1), ('+', 4, 0), ('-', 4, 1),
    ('*', 4, 2), ('/', 5, 0)
]

for text, row, col in buttons:
    tk.Button(frame, text= text, padx=15, pady=5, width=3, command=lambda t=text: click(t)).grid(row = row, column = col, pady = 2)

tk.Button(frame, text = "Clear", pady=5, padx=15, command=clear).grid(row = 6, column = 0, columnspan = 1, pady = 0)
tk.Button(frame, text = "=", padx=15, pady=5, width=5, command=equal).grid(row = 6, column=1, columnspan=1, pady=0)

win.mainloop()