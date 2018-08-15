from tkinter import *
from tkinter import filedialog

def createWindow(columns):
    window = Tk()
    window.geometry("400x200")
    window.title("Loyal Hackers 2018 v.1")

    first_drop_down = StringVar(window)
    first_drop_down.set("First Attribute")
    option = OptionMenu(window, first_drop_down, *tuple(columns))
    option.pack()

    second_drop_down = StringVar(window)
    second_drop_down.set("Second Attribute")
    option = OptionMenu(window, second_drop_down, *tuple(columns))
    option.pack()

    def ok():
        print("value is", first_drop_down.get(), second_drop_down.get())
        window.destroy()

    button = Button(window, text="OK", command=ok)
    button.pack()

    window.mainloop()

    return first_drop_down.get(), second_drop_down.get()

def openFileDialogBox():
    window = Tk()
    window.geometry("200x400")
    window.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path

def showResultsOnGrid(clusterNum, attributeArray):
    colours = ['red', 'green', 'orange', 'white', 'yellow', 'blue']
    window = Tk()
    window.geometry("1024x300")
    print(attributeArray)
    print(clusterNum)
    Label(text="Cluster Id", relief=RIDGE, width=20).grid(row=0, column=0)
    Label(text="Mileage Percantage", relief=RIDGE, width=20).grid(row=0, column=1)
    Label(text="Customer Percantage", relief=RIDGE, width=20).grid(row=0, column=2)
    Label(text="Weight", relief=RIDGE, width=20).grid(row=0, column=3)
    Label(text="Services per Cluster", relief=RIDGE, width=20).grid(row=0, column=4)
    Label(text="Service Index", relief=RIDGE, width=20).grid(row=0, column=5)


    for i in range(0, clusterNum):
        Label(text=i+1, relief=RIDGE, width=20).grid(row=i+1, column=0)

        Label(text=round(attributeArray[0][i],4), relief=RIDGE, width=20).grid(row=i+1, column=1)
        Label(text=round(attributeArray[1][i],5), relief=RIDGE, width=20).grid(row=i+1, column=2)
        Label(text=round(attributeArray[2][i],5), relief=RIDGE, width=20).grid(row=i+1, column=3)
        Label(text=round(attributeArray[3][i],5), relief=RIDGE, width=20).grid(row=i+1, column=4)
        Label(text=round(attributeArray[4][i],5), relief=RIDGE, width=20).grid(row=i+1, column=5)

    window.mainloop()