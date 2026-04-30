import customtkinter as ctk
import math_lib


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


def open_help():  
    help_window = ctk.CTkToplevel(app)
    help_window.title("Hint")
    help_window.geometry("400x500")
    help_window.attributes("-topmost", True)
    
    textbox = ctk.CTkTextbox(help_window, font=("Roboto", 15), wrap="word", fg_color="transparent")
    textbox.pack(fill="both", expand=True, padx=20, pady=20)
    
    help_text = """ WELCOME TO THE CALCULATOR

Buttons & Functions:
• xⁿ (Power): Enter the base, press xⁿ, and enter the exponent. (Example: 5 xⁿ 3 = 125)
• ⁿ√x (N-th Root): Enter the number, press ⁿ√x, and enter the degree of the root. (Example: 27 ⁿ√x 3 = 3)
• x² (Square): Immediately calculates the square of the current number.
• √x (Square Root): Immediately calculates the square root of the current number.
• ¹/x (Inverse): Calculates 1 divided by the current number.
• ! (Factorial): Calculates the product of all positive integers up to the given number.

Keyboard Shortcuts:
You can fully control the calculator using your keyboard.
• Enter / = : Calculates the result
• Backspace : Deletes the last character
• Esc : Clears the entire display (AC)
"""

    textbox.insert("0.0", help_text)
    textbox.configure(state="disabled")

app = ctk.CTk()
app.title("Calculator")
app.geometry("450x700")
app.resizable(True, True)
ctk.set_appearance_mode("dark")
app.configure(fg_color="#121212")

for i in range(4):
    app.grid_columnconfigure(i, weight=1, uniform="equal_cons")
for i in range (1, 7):
    app.grid_rowconfigure(i, weight=1, uniform="equal_rows")

font_display = ("Roboto", 55, "bold")
font_button = ("Roboto", 24,"bold")

theme_num = {"fg_color": "#2b2b2b", "hover_color": "#404040", "text_color": "white", "font": font_button}
theme_op = {"fg_color": "#D32F2F", "hover_color": "#F44336", "text_color": "white", "font": font_button}
theme_spec = {"fg_color": "#E0E0E0", "hover_color": "#FFFFFF", "text_color": "black", "font": font_button}


display = ctk.CTkEntry(app, placeholder_text="0", justify="right", state="readonly", font=font_display, height=90, fg_color="#1e1e1e", border_color="#D32F2F")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=(20, 20), sticky="nsew")


def key_pressed(event):
    char = event.char
    keysym = event.keysym

    if char == '1' : button1()
    elif char == '2' : button2()
    elif char == '3' : button3()
    elif char == '4' : button4()
    elif char == '5' : button5()
    elif char == '6' : button6()
    elif char == '7' : button7()
    elif char == '8' : button8()
    elif char == '9' : button9()
    elif char == '0' : button0()

    elif char == '+': button_add()
    elif char == '-': button_sub()
    elif char == '*': button_mul()
    elif char == '/': button_div()
    elif char == '!': button_factorial()
    elif char == '.' or char == ',': button_point()

    elif keysym == 'Return' or keysym == 'KP_Enter' or char == '=': button_equals()
    elif keysym == 'BackSpace': button_rm()
    elif keysym == 'Escape': button_ac()
    
app.bind('<Key>', key_pressed)


def button_equals():
    expression = display.get()

    forbidden_suffixes = ("+", "-", "*", "/", ".", "^", "rt")
    if expression.endswith(forbidden_suffixes):
        return
    
    try:
        expression = expression.replace("--", "+")
        expression = expression.replace("+-", "-")

        if "+" in expression:
            numbers = expression.split("+")
            result = math_lib.add(float(numbers[0]), float(numbers[1]))

        elif "*" in expression:
            numbers = expression.split("*")
            result = math_lib.mul(float(numbers[0]), float(numbers[1]))

        elif "ˇ2" in expression:
            numbers = expression.split("ˇ2")       
            result = math_lib.square(float(numbers[0]))

        elif "^" in expression:
            numbers = expression.split("^")
            result = math_lib.power(float(numbers[0]), float(numbers[1]))

        elif "rt" in expression:
            numbers = expression.split("rt")
            result = math_lib.root(float(numbers[1]), float(numbers[0]))

        elif "/" in expression:
            numbers = expression.split("/")
            result = math_lib.div(float(numbers[0]), float(numbers[1]))

        elif "-" in expression:
            numbers = expression.rsplit("-", 1)
            result = math_lib.sub(float(numbers[0]), float(numbers[1]))
        
        else:
            result = expression
        
        display.configure(state="normal")
        display.delete(0, "end")
        display.insert("end", str(result))
        display.configure(state="readonly")

    except Exception as e:
        display.configure(state="normal")
        display.delete(0,"end")

        error_msg = str(e)

        if error_msg == "":
            error_msg = type(e).__name__

        if len(error_msg) > 12:
            display.configure(font=("Roboto", 25, "bold"))
        elif len(error_msg) > 8:
            display.configure(font=("Roboto", 38, "bold"))
        else:
            display.configure(font=("Roboto", 55, "bold"))

        display.insert("end", error_msg)
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="=", command=button_equals, **theme_op)
button.grid(row=6, column=3, padx=5, pady=5, sticky="nsew")


def button_inverse():
    text = display.get()
    if text == "":
        return
    
    last_number = text
    for operator in ["+", "-", "*", "/", "^", "rt"]:
        if operator in last_number:
            last_number = last_number.split(operator)[-1]

    if last_number != "":
        try:
            number = float(last_number)
            result = math_lib.inverse(number)

            new_text = text[:-len(last_number)] + str(result)

            display.configure(state="normal")
            display.delete(0, "end")
            display.insert("end", new_text)
            display.configure(state="readonly")
        except Exception:
            pass

button = ctk.CTkButton(app, text="1/x", command=button_inverse, **theme_spec)
button.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")


def button_sq():
    text = display.get()
    if text == "":
        return
    
    last_number = text
    for operator in ["+", "-", "*", "/", "^", "rt"]:
        if operator in last_number:
            last_number = last_number.split(operator)[-1]

    if last_number != "":
        try:
            number = float(last_number)
            result = math_lib.sqrt(number)

            new_text = text[:-len(last_number)] + str(result)

            display.configure(state="normal")
            display.delete(0, "end")
            display.insert("end", new_text)
            display.configure(state="readonly")
        except Exception:
            pass

button = ctk.CTkButton(app, text="√x", command=button_sq, **theme_spec)
button.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")


def button_square():
    text = display.get()
    if text == "":
        return
    
    last_number = text
    for operator in ["+", "-", "*", "/", "^", "rt"]:
        if operator in last_number:
            last_number = last_number.split(operator)[-1]

    if last_number != "":
        try:
            number = float(last_number)
            result = math_lib.square(number)

            new_text = text[:-len(last_number)] + str(result)
            display.configure(state="normal")
            display.delete(0, "end")
            display.insert("end", new_text)
            display.configure(state="readonly")
        except Exception:
            pass

button = ctk.CTkButton(app, text="x²", command=button_square, **theme_spec)
button.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")


def button_root():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "rt")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="ⁿ√x", command=button_root, **theme_spec)
button.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")


def button_power():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "^")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="xⁿ", command=button_power, **theme_spec)
button.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")


def button_add():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "+")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="+", command=button_add, **theme_op)
button.grid(row=5, column=3, padx=5, pady=5, sticky="nsew")


def button_sub():
    auto_compute()
    text = display.get()

    if text == "":
        display.configure(state="normal")
        display.insert("end", "-")
        display.configure(state="readonly")
    
    elif text.endswith(("+", "-", "*", "/", "^", "rt", "sq", "sqrt", "1/x")):
        if not text.endswith("--"):
            display.configure(state="normal")
            display.insert("end", "-")
            display.configure(state="readonly")
    
    elif can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "-")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="-", command=button_sub, **theme_op)
button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")


def button_rm():
    current_text = display.get()
    if len(current_text) > 0:
        display.configure(state="normal")
   
    display.delete(len(current_text) - 1, "end")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="⌫", command=button_rm, **theme_spec)
button.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")


def button_div():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "/")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="÷", command=button_div, **theme_op)
button.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")


def button_mul():
    auto_compute()
    if can_add_operator() == True:
        display.configure(state="normal")
        display.insert("end", "*")
        display.configure(state="readonly")

button = ctk.CTkButton(app, text="×", command=button_mul, **theme_op)
button.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")


def button_ac():
    display.configure(state="normal")
    display.delete(0, "end")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="AC", command=button_ac, **theme_spec)
button.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")


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

button = ctk.CTkButton(app, text="!", command=button_factorial, **theme_spec)
button.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")


def button_point():
    current_text = display.get()
    last_number = current_text
    for operator in ["+", "-", "*", "/", "^", "rt"]:
        if operator in last_number:
            last_number = last_number.split(operator)[-1]
    
    if "." not in last_number:
        display.configure(state="normal")

        if last_number == "":
            display.insert("end", "0.")
        else:
            display.insert("end", ".")

    display.configure(state="readonly")

button = ctk.CTkButton(app, text=".", command=button_point, **theme_num)
button.grid(row=6, column=2, padx=5, pady=5, sticky="nsew")


def button0():
    display.configure(state="normal")
    display.insert("end", "0")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="0", command=button0, **theme_num)
button.grid(row=6, column=1, padx=5, pady=5, sticky="nsew")


def button1():
    display.configure(state="normal")
    display.insert("end", "1")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="1", command=button1, **theme_num)
button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")


def button2():
    display.configure(state="normal")
    display.insert("end", "2")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="2", command=button2, **theme_num)
button.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")


def button3():
    display.configure(state="normal")
    display.insert("end", "3")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="3", command=button3, **theme_num)
button.grid(row=5, column=2, padx=5, pady=5, sticky="nsew")


def button4():
    display.configure(state="normal")
    display.insert("end", "4")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="4", command=button4, **theme_num)
button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")


def button5():
    display.configure(state="normal")
    display.insert("end", "5")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="5", command=button5, **theme_num)
button.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")


def button6():
    display.configure(state="normal")
    display.insert("end", "6")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="6", command=button6, **theme_num)
button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")


def button7():
    display.configure(state="normal")
    display.insert("end", "7")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="7", command=button7, **theme_num)
button.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")


def button8():
    display.configure(state="normal")
    display.insert("end", "8")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="8", command=button8, **theme_num)
button.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")


def button9():
    display.configure(state="normal")
    display.insert("end", "9")
    display.configure(state="readonly")

button = ctk.CTkButton(app, text="9", command=button9, **theme_num)
button.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")


help_button = ctk.CTkButton(app, text="?", width=15, height=15, font=("Roboto", 14, "bold"), fg_color="#7a7a7a", hover_color="#333333", command=open_help)

help_button.place(x=20, y=30)

app.mainloop()