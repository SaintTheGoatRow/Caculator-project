from tkinter import Tk, Button, Entry, END, Label
import math

# Tkinter configuration
root = Tk()
root.title("Calculator")
root.config(bg="black")
root.resizable(False, False)

# Output Screen Configuration 
e = Entry(root, font=("Ariel", 15), width= 24, borderwidth= 4, justify="right")
e.grid(row= 0, column= 0, columnspan= 4, pady= 20, ipady= 15)

memory_value = 0
calculation_history = []


# Button Functions and Math Operations 
def button_click(number):
    e.insert(END, str(number))

def button_clear():
    e.delete(0, END)

def test(a, b, c):    
     return a + b + c

def power():
    try:
        base = float(e.get())
        e.delete(0, END)
        e.insert(END, str(base) + "^")
    except ValueError:
        e.delete(0, END)
        e.insert(END, "Error")

def modulus():
    try:
        num1 = float(e.get())
        e.delete(0, END)
        e.insert(END, str(num1) + "%")
    except ValueError:
        e.delete(0, END)
        e.insert(END, "Error")

def button_equal():
    try:
        calculation = e.get()
        if "^" in calculation:
            base, exponent = map(float, calculation.split("^"))
            result = base ** exponent
        elif "%" in calculation:
            num1, num2 = map(float, calculation.split("%"))
            result = num1 % num2
        else:
            result = eval(calculation)
        calculation_history.append(calculation + " = " + str(result))
        e.delete(0, END)
        e.insert(END, str(result))
    except Exception as ex:
        e.delete(0, END)
        e.insert(END, "Error")

def button_backspace():
    current = e.get()
    e.delete(0, END)
    e.insert(END, current[:-1])

def memory_add():
    global memory_value
    try:
        memory_value += float(e.get())
    except ValueError:
        e.delete(0, END)
        e.insert(END, "Error")

def memory_subtract():
    global memory_value
    try:
        memory_value -= float(e.get())
    except ValueError:
        e.delete(0, END)
        e.insert(END, "Error")

def memory_recall():
    e.delete(0, END)
    e.insert(END, str(memory_value))

def memory_clear():
    global memory_value
    memory_value = 0
    e.delete(0, END)
    e.insert(END, "Memory Cleared")

def square():
    try:
        result = float(e.get()) ** 2
        e.delete(0, END)
        e.insert(END, str(result))
    except ValueError:
        e.delete(0, END)
        e.insert(END, "Error: Invalid input")
    except Exception as ex:
        e.delete(0, END)
        e.insert(END, "Error: " + str(ex))

def square_root():
    try:
        result = math.sqrt(float(e.get()))
        e.delete(0, END)
        e.insert(END, str(result))
    except ValueError:
        e.delete(0, END)
        e.insert(END, "Error")

def recall_history():
    e.history_window = Tk()
    e.history_window.title("Calculation History")
    history_text = ""
    for i, calculation in enumerate(calculation_history):
        history_text += calculation + "\n"
    Label(e.history_window, text=history_text).pack()

def clear_history():
    global calculation_history
    calculation_history = []
    history_window = Tk()
    history_window.title("Calculation History")
    Label(history_window, text="History Cleared").pack()


# Button configuration
button_memory_add = Button(root, text="M+", width=10, height=3, bg="purple", fg="green", command=memory_add)
button_memory_subtract = Button(root, text="M-", width=10, height=3, bg="purple", fg="green", command=memory_subtract)
button_memory_recall = Button(root, text="MR", width=10, height=3, bg="purple", fg="green", command=memory_recall)
button_memory_clear = Button(root, text="MC", width=10, height=3, bg="purple", fg="green", command=memory_clear)
button_square = Button(root, text="x^2", width=10, height=3, bg="purple", fg="green", command=square)
button_square_root = Button(root, text="sqrt", width=10, height=3, bg="purple", fg="green", command=square_root)
button_history = Button(root, text="History", width=10, height=3, bg="purple", fg="green", command=recall_history)
button_clear_history = Button(root, text="Clear History", width=10, bg="purple", fg="green", height=3, command=clear_history)
button_power = Button(root, text="x^y", width=10, height=3, bg="purple", fg="green", command=power)
button_modulus = Button(root, text="%", width=10, height=3, bg="purple", fg="green", command=modulus)

button_1 = Button(root, text="1", width=10, height=3, bg="purple", fg="green", command=lambda: button_click(1))
button_2 = Button(root, text="2", width=10, height=3, bg="purple", fg="green", command=lambda: button_click(2))
button_3 = Button(root, text="3", width=10, height=3, bg="purple", fg="green", command=lambda: button_click(3))
button_4 = Button(root, text="4", width=10, height=3, bg="purple", fg="green", command=lambda: button_click(4))
button_5 = Button(root, text="5", width=10, height=3, bg="purple", fg="green", command=lambda: button_click(5))
button_6 = Button(root, text="6", width=10, height=3, bg="purple", fg="green", command=lambda: button_click(6))
button_7 = Button(root, text="7", width=10, height=3, bg="purple", fg="green", command=lambda: button_click(7))
button_8 = Button(root, text="8", width=10, height=3, bg="purple", fg="green", command=lambda: button_click(8))
button_9 = Button(root, text="9", width=10, height=3, bg="purple", fg="green", command=lambda: button_click(9))
button_0 = Button(root, text="0", width=10, height=3, bg="purple", fg="green", command=lambda: button_click(0))
button_add = Button(root, text="+", width=10, height=3, bg="purple", fg="green", command=lambda: button_click("+"))
button_subtract = Button(root, text="-", width=10, height=3, bg="purple", fg="green", command=lambda: button_click("-"))
button_multiply = Button(root, text="*", width=10, height=3, bg="purple", fg="green", command=lambda: button_click("*"))
button_divide = Button(root, text="/", width=10, height=3, bg="purple", fg="green", command=lambda: button_click("/"))
button_equal = Button(root, text="=", width=10, height=3, bg="purple", fg="green", command=button_equal)
button_modulus = Button(root, text="%", width=10, height=3, bg="purple", fg="green", command=lambda: button_click("%"))
button_clear = Button(root, text="C", width=10, height=3, bg="purple", fg="green", command=button_clear)
button_backspace = Button(root, text="Backspace", width=10, bg="purple", fg="green", height=3, command=button_backspace)
button_decimal_place= Button(root, text=".", width=10, bg="purple", fg="green", height=3, command=lambda: button_click("."))


#Button alignment on the calculator.
button_7.grid(row=6, column=0)
button_8.grid(row=6, column=1)
button_9.grid(row=6, column=2)
button_divide.grid(row=6, column=3)

button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
button_multiply.grid(row=5, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_subtract.grid(row=7, column=0)

button_0.grid(row=7, column=1)
button_clear.grid(row=4, column=3, columnspan=2)
button_add.grid(row=7, column=2)
button_backspace.grid(row=8, column=2, columnspan=1)

button_equal.grid(row=8, column=3, columnspan=3)

button_memory_add.grid(row=1, column=0)
button_memory_subtract.grid(row=1, column=1)
button_memory_recall.grid(row=1, column=2)
button_memory_clear.grid(row=1, column=3)

button_square.grid(row=2, column=0)
button_square_root.grid(row=2, column=1)
button_history.grid(row=2, column=2)
button_clear_history.grid(row=2, column=3)

button_power.grid(row=7, column=3)
button_modulus.grid(row=8, column=0, columnspan=1)
button_decimal_place.grid(row=8, column=1, columnspan=1)
sumofthree=test(1,4,7)
print(sumofthree)
root.mainloop()
