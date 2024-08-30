import customtkinter

app = customtkinter.CTk()
app.title("STEGRYPT")
app.geometry("600x600")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue") 

def button_function():
    customtkinter.set_appearance_mode("light")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Light Mode", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.grid_columnconfigure(0, weight=1)
app.mainloop()