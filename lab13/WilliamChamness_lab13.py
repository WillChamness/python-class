import tkinter as tk

class CelToFah:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Celcius to Fahrenheit")

        self._construct_window()

        self.root.mainloop()


    def _construct_window(self):
        self.header = tk.Label(self.root, text="Celcius to Fahrenheit", font=("Arial", 18))
        self.header.pack(pady=20)

        self.cel_container = tk.Frame(self.root)
        self.cel_container.columnconfigure(0, weight=1)
        self.cel_container.columnconfigure(1, weight=1)

        self.cel_text = tk.Label(self.cel_container, text="Enter degrees Celcius:")
        self.cel_text.grid(row=0, column=0)
        self.cel = tk.Entry(self.cel_container, font=("Arial", 24))
        self.cel.grid(row=1, column=0)
        self.cel_container.pack(pady=20)

        self.btn = tk.Button(self.root, text="Convert", font=("Arial", 18), command=self._convert)
        self.btn.pack(pady=20)    

        self.fah = tk.Label(self.root, text="", font=("Arial", 18))
        self.fah.pack(pady=20)


    def _convert(self):
        CONVERTER = lambda celcius : (9 * celcius / 5) + 32
        cel = float(self.cel.get())
        self.fah.config(text=f"{CONVERTER(cel)} degrees Fahrenheit")
        self.cel.config(textvariable="")


def main():
    CelToFah()


if __name__ == "__main__":
    main()
