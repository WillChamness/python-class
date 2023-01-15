import tkinter as tk
from tkinter import messagebox

class MyGUI:
    """
    Goal:
    have user enter in text. if a checkbox is checked, display the text as a pop-up when the user pushes
    a button. otherwise, change the text of the label
    """

    def __init__(self):
        self.root = tk.Tk()

        ARIAL_18 = ("Arial", 18)
        ARIAL_16 = ("Arial", 16)

        self.label = tk.Label(self.root, text="Your message", font=ARIAL_18)
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=ARIAL_16)
        self.textbox.bind("<KeyPress>", self.shortcut) # bind any keypress events to shortcut()
        self.textbox.pack(pady=10)

        self.check_state = tk.BooleanVar() # can be IntVar, DoubleVar, or StringVar
        self.check = tk.Checkbutton(self.root, text="Show messagebox", font=ARIAL_16, variable=self.check_state) # variable contains check state
        self.check.pack(pady=10)

        self.button = tk.Button(self.root, text="Show message", font=ARIAL_18, command=self.show_message)
        self.button.pack(pady=10)

        self.output = tk.Label(self.root, text="", font=ARIAL_18)
        self.output.pack(pady=10)

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0) # tearoff is for aesthetics
        self.filemenu.add_command(label="Print hello", command=self.print_hello)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close", command=exit)
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.root.config(menu=self.menubar)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) # define what to do when the user closes the application
        self.root.mainloop()


    def show_message(self):
        textbox_str = self.textbox.get("1.0", tk.END) # extract the string textbox[0:len(textbox)]
        if self.check_state.get():
            self.output.config(text="")
            tk.messagebox.showinfo(title="Message", message=textbox_str) # popup message
        else:
            self.output.config(text=textbox_str) # change the text of the output label


    def shortcut(self, event):
        print(event.keysym)
        print(event.state)

        if event.keysym == "Return" and event.state == 12:
            self.show_message()
            

    def on_closing(self):
        if tk.messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()            

    def print_hello(self):
        print("Hello world")


def main():
    MyGUI()


if __name__ == "__main__":
    main()