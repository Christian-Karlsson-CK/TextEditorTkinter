from tkinter import *
from tkinter import filedialog
from tkinter import font


root = Tk()

root.title("TextEditor Deluxe")
#root.iconbitmap("coolbild.jpg")
root.geometry("1175x630")

mainFrame = Frame(root)
mainFrame.pack(pady=3)

textScroll = Scrollbar(mainFrame)
textScroll.pack(side=RIGHT, fill=Y)

consolasFont = font.Font(family="Consolas", size=16)

textBox = Text(mainFrame, width=95, height=25, font=(consolasFont), selectbackground="#63B6EC", selectforeground="black", undo=True, yscrollcommand=textScroll.set)
textBox.pack()

textScroll.config(command=textBox.yview)

topMenu = Menu(root)
root.config(menu=topMenu)

#NYI functionality for the file dropdown items
fileCascade = Menu(topMenu, tearoff=False)
topMenu.add_cascade(label="File", menu=fileCascade)
fileCascade.add_command(label="New")
fileCascade.add_command(label="Open")
fileCascade.add_command(label="Save")
fileCascade.add_command(label="Save as")
fileCascade.add_command(label="Exit")

#NYI functionality for the edit dropdown items
editCascade = Menu(topMenu, tearoff=False)
topMenu.add_cascade(label="Edit", menu=editCascade)
editCascade.add_command(label="Cut")
editCascade.add_command(label="Copy")
editCascade.add_command(label="Paste")

#NYI functionality for the export function
exportCascade = Menu(topMenu, tearoff=False)
topMenu.add_cascade(label="Export", menu=exportCascade)
exportCascade.add_command(label="PDF")

#NYI functionality for the conversion item
convertCascade = Menu(topMenu, tearoff=False)
topMenu.add_cascade(label="Convert", menu=convertCascade)
convertCascade.add_command(label="Binary")


#NYI add a popupwindow for a about message!
aboutCascade = Menu(topMenu, tearoff=False)
topMenu.add_cascade(label="About", menu=aboutCascade)
aboutCascade.add_command(label="About")

#NYI add functionality for a word counter and letter counter.
infoBar = Label(root, text="words: NYI, letters: NYI", anchor=E)

infoBar.pack(fill=X,side=BOTTOM)











root.mainloop()










