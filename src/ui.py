import customtkinter as ctk


ctk.set_appearance_mode('system')
ctk.set_default_color_theme('green')

app = ctk.CTk()
app.title("Calculator")
app.geometry("500x1000")
app.resizable(width=True, height=True)

display = ctk.CTkEntry(app, placeholder_text="0", justify="right", state="readonly")
display.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

def button0():
 
 display.configure(state="normal")
 display.insert("end", "0")
 display.configure(state="readonly")

button = ctk.CTkButton(app, text="0", command=button0)
button.grid(row=4, column=1, padx=10, pady=10)

def button1():
 
 display.configure(state="normal")
 display.insert("end", "1")
 display.configure(state="readonly")

button = ctk.CTkButton(app, text="1", command=button1)
button.grid(row=3, column=0, padx=10, pady=10)

def button2():
 
 display.configure(state="normal")
 display.insert("end", "2")
 display.configure(state="readonly")

button = ctk.CTkButton(app, text="2", command=button2)
button.grid(row=3, column=1, padx=10, pady=10)

def button3():
 
 display.configure(state="normal")
 display.insert("end", "3")
 display.configure(state="readonly")

button = ctk.CTkButton(app, text="3", command=button3)
button.grid(row=3, column=2, padx=10, pady=10)

def button4():
 
 display.configure(state="normal")
 display.insert("end", "4")
 display.configure(state="readonly")

button = ctk.CTkButton(app, text="4", command=button4)
button.grid(row=2, column=0, padx=10, pady=10)

def button5():
 
 display.configure(state="normal")
 display.insert("end", "5")
 display.configure(state="readonly")

button = ctk.CTkButton(app, text="5", command=button5)
button.grid(row=2, column=1, padx=10, pady=10)

def button6():
 
 display.configure(state="normal")
 display.insert("end", "6")
 display.configure(state="readonly")

button = ctk.CTkButton(app, text="6", command=button6)
button.grid(row=2, column=2, padx=10, pady=10)

def button7():
 
 display.configure(state="normal")
 display.insert("end", "7")
 display.configure(state="readonly")

button = ctk.CTkButton(app, text="7", command=button7)
button.grid(row=1, column=0, padx=10, pady=10)

def button8():
 
 display.configure(state="normal")
 display.insert("end", "8")
 display.configure(state="readonly")

button = ctk.CTkButton(app, text="8", command=button8)
button.grid(row=1, column=1, padx=10, pady=10)

def button9():
 
 display.configure(state="normal")
 display.insert("end", "9")
 display.configure(state="readonly")

button = ctk.CTkButton(app, text="9", command=button9)
button.grid(row=1, column=2, padx=10, pady=10)

app.mainloop()