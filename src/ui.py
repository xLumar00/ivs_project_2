import customtkinter as ctk
import math_lib

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('green')

def can_add_operator():
    text = display.get()

    if text == "":
        return False
    
    forbidden_suffixes = ("+", "-", "*", "/", ".", "^", "sq", "sqrt", "rt", "1/x")
       
    if text.endswith(forbidden_suffixes):
        return False
    
    return True

def auto_compute():
    text = display.get()
    forbidden_suffixes = ("+", "-", "*", "/", ".", "^", "sq", "sqrt", "rt", "1/x")
    if text.endswith(forbidden_suffixes):
        return
    
    text_to_check = text[1:] if text.startswith("-") else text

    for op in ["+", "-", "*", "/", "^", "sq", "rt", "1/x", "!"]:
        if op in text_to_check:
            button_equals()
            break


app = ctk.CTk()
app.title("Calculator")
app.geometry("650x1000")
app.resizable(True, True)


display = ctk.CTkEntry(app, placeholder_text="0", justify="right", state="readonly")
display.grid(row=0, column=0, columnspan=4, rowspan=1, padx=10, pady=10, sticky="nsew")

def button_equals():
    expression = display.get()
    try:
        if "+" in expression:
            numbers = expression.split("+")
            result = math_lib.add(float(numbers[0]), float(numbers[1]))

        elif "-" in expression:
            numbers = expression.split("-")
            result = math_lib.sub(float(numbers[0]), float(numbers[1]))

        elif "*" in expression:
            numbers = expression.split("*")
            result = math_lib.mul(float(numbers[0]), float(numbers[1]))

        elif "!" in expression:
            numbers = expression.split("!")
            result = math_lib.factorial(int(numbers[0]))

        elif "^2" in expression:
            numbers = expression.split("^2")
            result = math_lib.square(float(numbers[0]))

        elif "^" in expression:
            numbers = expression.split("^")
            result = math_lib.power(int(numbers[0]), int(numbers[1]))

        elif "rt" in expression:
            numbers = expression.split("rt")
            result = math_lib.root(float(numbers[0]), float(numbers[1]))

        elif "sq" in expression:
            numbers = expression.split("sq")
            result = math_lib.sqrt(int(numbers[0]))

        elif "1/x" in expression:
            numbers = expression.split("1/x")
            result = math_lib.inverse(float(numbers[0]))

        elif "/" in expression:
            numbers = expression.split("/")
            result = math_lib.div(float(numbers[0]), float(numbers[1]))
        
        display.configure(state="normal")
        display.delete(0, "end")
        display.insert("end", str(result))
        display.configure(state="readonly")

    except Exception:
        display.configure(state="normal")
        display.delete(0,"end")
        display.insert("end", "Error")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="=", command=button_equals)
button.grid(row=6, column=3, padx=10, pady=10, sticky="nsew")


def button_inverse():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "1/x")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="1/x", command=button_inverse)
button.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")


def button_sq():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "sq")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="sq", command=button_sq)
button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")


def button_square():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "^2")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="^2", command=button_square)
button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")


def button_root():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "rt")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="rt", command=button_root)
button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")


def button_power():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "^")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="^", command=button_power)
button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


def button_add():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "+")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="+", command=button_add)
button.grid(row=5, column=3, padx=10, pady=10, sticky="nsew")


def button_sub():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "-")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="-", command=button_sub)
button.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")


def button_rm():
    current_text = display.get()
    if len(current_text) > 0:
        display.configure(state="normal")
   
    display.delete(len(current_text) - 1, "end")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="RM", command=button_rm)
button.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")


def button_div():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "/")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="/", command=button_div)
button.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")


def button_mul():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "*")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="*", command=button_mul)
button.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")


def button_ac():
    display.configure(state="normal")
    display.delete(0, "end")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="AC", command=button_ac)
button.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")


def button_factorial():
    text = display.get()
    if text == "":
        return
    
    last_number = text
    for operator in ["+", "-", "*", "/", "^", "rt"]:
        if operator in last_number:
            last_number = last_number.split(operator)[-1]

    if last_number != "":
        try:
            number = int(float(last_number))
            result = math_lib.factorial(number)

            new_text = text[:-len(last_number)] + str(result)

            display.configure(state="normal")
            display.delete(0, "end")
            display.insert("end", new_text)
            display.configure(state="readonly")
        except Exception:
            pass

button = ctk.CTkButton(app, text="!", command=button_factorial)
button.grid(row=6, column=0, padx=10, pady=10, sticky="nsew")


def button_point():
    current_text = display.get()
    last_number = current_text
    for operator in ["+", "-", "*", "/"]:
        if operator in last_number:
            last_number = last_number.split(operator)[-1]
    
    if "." not in last_number:
        display.configure(state="normal")

        if last_number == "":
            display.insert("end", "0.")
        else:
            display.insert("end", ".")

    display.configure(state="readonly")

button = ctk.CTkButton(app, text=".", command=button_point)
button.grid(row=6, column=2, padx=10, pady=10, sticky="nsew")


def button0():
    display.configure(state="normal")
    display.insert("end", "0")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="0", command=button0)
button.grid(row=6, column=1, padx=10, pady=10)


def button1():
    display.configure(state="normal")
    display.insert("end", "1")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="1", command=button1)
button.grid(row=5, column=0, padx=10, pady=10)


def button2():
    display.configure(state="normal")
    display.insert("end", "2")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="2", command=button2)
button.grid(row=5, column=1, padx=10, pady=10)


def button3():
    display.configure(state="normal")
    display.insert("end", "3")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="3", command=button3)
button.grid(row=5, column=2, padx=10, pady=10)


def button4():
    display.configure(state="normal")
    display.insert("end", "4")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="4", command=button4)
button.grid(row=4, column=0, padx=10, pady=10)


def button5():
    display.configure(state="normal")
    display.insert("end", "5")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="5", command=button5)
button.grid(row=4, column=1, padx=10, pady=10)


def button6():
    display.configure(state="normal")
    display.insert("end", "6")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="6", command=button6)
button.grid(row=4, column=2, padx=10, pady=10)


def button7():
    display.configure(state="normal")
    display.insert("end", "7")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="7", command=button7)
button.grid(row=3, column=0, padx=10, pady=10)


def button8():
    display.configure(state="normal")
    display.insert("end", "8")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="8", command=button8)
button.grid(row=3, column=1, padx=10, pady=10)


def button9():
    display.configure(state="normal")
    display.insert("end", "9")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="9", command=button9)
button.grid(row=3, column=2, padx=10, pady=10)

app.mainloop()