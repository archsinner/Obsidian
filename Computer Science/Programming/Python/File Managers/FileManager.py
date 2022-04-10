# Create a simple gui file manager using tkinter


import tkinter as tk


class FileManager(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("File Manager")
        self.pack(fill=tk.BOTH, expand=1)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = tk.Label(self, text="File:")
        lbl.grid(sticky=tk.W, pady=4, padx=5)

        self.txt = tk.Entry(self)
        self.txt.grid(row=1, column=0, columnspan=2, sticky=tk.W + tk.E)

        self.txt.insert(tk.END, 'C:\\')

        lbl2 = tk.Label(self, text="Folder:")
        lbl2.grid(row=2, column=0, sticky=tk.W, pady=4, padx=5)

        self.txt2 = tk.Entry(self)
        self.txt2.grid(row=3, column=0, columnspan=2, sticky=tk.W + tk.E)

        self.txt2.insert(tk.END, 'C:\\')

        self.btn = tk.Button(self, text="Browse...")
        self.btn.grid(row=1, column=3)

        self.btn2 = tk.Button(self, text="Browse...")
        self.btn2.grid(row=3, column=3)

        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=5, column=0, columnspan=2, sticky=tk.N + tk.S + tk.E + tk.W)

        self.listbox.insert(tk.END, "Item 1")
        self
        self.listbox.insert(tk.END, "Item 2")
        self.listbox.insert(tk.END, "Item 3")
        self.listbox.insert(tk.END, "Item 4")
        self.listbox.insert(tk.END, "Item 5")

        self.btn3 = tk.Button(self, text="Add")
        self.btn3.grid(row=4, column=0, padx=5)

        self.btn4 = tk.Button(self, text="Remove")
        self.btn4.grid(row=4, column=1, padx=5)

        self.btn5 = tk.Button(self, text="Close", command=self.quit)
        self.btn5.grid(row=4, column=3, pady=5)


def main():
    root = tk.Tk()
    app = FileManager(root)
    root.mainloop()


if __name__ == '__main__':
    main()
    