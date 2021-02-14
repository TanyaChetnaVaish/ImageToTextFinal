#%%
from tkinter import *
from tkinter import filedialog
import main as bg


def get_file_path():
    global file_path
    # Open and return file path
    file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("type1", "*.png"), ("type2", "*.jpg")))
    l1 = Label(window, text = "File path: " + file_path).pack()

def submit():
    bg.background(file_path)
    window.destroy()


window = Tk()
# Creating a button to search the file
b1 = Button(window, text = "Open File", command = get_file_path).pack()
b2 = Button(window, text= "Submit", command= submit).pack()

window.mainloop()


