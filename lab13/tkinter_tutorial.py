import tkinter as tk

root = tk.Tk()

root.geometry("800x500") # create window with dimensions 800x500 pixels
root.title("My GUI") # set the title in the top

label = tk.Label(root, text="Hello world", font=("Arial", 18)) # create text on screen contained by root, text is "Hello world" and Arial 18pt font
label.pack(padx=20, pady=20) # show label on screen with padding surrounding the text

textbox = tk.Text(root, height=3, font=("Arial", 16)) # create multi-linx textfield that user can enter data in
textbox.pack()

textfield = tk.Entry(root) # create single-line textfield
textfield.pack()

button = tk.Button(root, text="Click me", font=("Arial", 18)) # create clickable button
button.pack()

button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1) # want buttons to stretch to fill the x-axis
button_frame.columnconfigure(1, weight=1) 
button_frame.columnconfigure(2, weight=1) 

mp_btn = tk.Button(button_frame, text=1, font=("Arial", 18))
mp_btn.grid(row=0, column=0, sticky=tk.W+tk.E)

mp_btn = tk.Button(button_frame, text=2, font=("Arial", 18))
mp_btn.grid(row=0, column=1, sticky=tk.W+tk.E)

mp_btn = tk.Button(button_frame, text=3, font=("Arial", 18))
mp_btn.grid(row=0, column=2, sticky=tk.W+tk.E)

mp_btn = tk.Button(button_frame, text=4, font=("Arial", 18))
mp_btn.grid(row=1, column=0, sticky=tk.W+tk.E)

mp_btn = tk.Button(button_frame, text=5, font=("Arial", 18))
mp_btn.grid(row=1, column=1, sticky=tk.W+tk.E)

mp_btn = tk.Button(button_frame, text=6, font=("Arial", 18))
mp_btn.grid(row=1, column=2, sticky=tk.W+tk.E)

button_frame.pack(fill="x", pady=20) # will pack all children

root.mainloop() # start the application