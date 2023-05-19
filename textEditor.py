from tkinter import *
from tkinter import filedialog
from tkinter import font
import os

filePath = None

def newFile():
    textBox.delete("1.0", END)
    root.title("TextEditor Deluxe - New File")
    infoBar.config(text="New File | Unsaved  | words: NYI | letters: NYI")
    filePath = None

def openFile():
    textBox.delete("1.0", END)

    filePath = filedialog.askopenfilename(title="Open File") #initialdir="C:\..." filetypes=((text files, "*.txt")("All files", "*.*""))
    filename = os.path.basename(filePath)
    root.title(f"TextEditor Deluxe - {filename}")
    infoBar.config(text=f"{filePath} | Saved  | words: NYI | letters: NYI")

    fileStream = open(filePath, 'r')
    text = fileStream.read()
    textBox.insert(1.0, text)
    fileStream.close()

def saveFile():
    if filePath != None:
        filename = os.path.basename(filePath)
        root.title(f"TextEditor Deluxe - {filename}")
        infoBar.config(text=f"{filePath} | Saved  | words: NYI | letters: NYI")
        fileStream = open(filePath, 'w')
        fileStream.write(textBox.get(1.0, END))
        fileStream.close()
    else:
        saveAsFile()




def saveAsFile():
    if filePath != None:
        dir = os.path.dirname(filePath)
        newFilePath = filedialog.asksaveasfilename(defaultextension=".*", initialdir=dir, title="Save File")
    else:
        newFilePath = filedialog.asksaveasfilename(defaultextension=".*", title="Save File")

    if newFilePath:
        filename = os.path.basename(newFilePath)
        root.title(f"TextEditor Deluxe - {filename}")
        infoBar.config(text=f"{newFilePath} | Saved  | words: NYI | letters: NYI")

        fileStream = open(newFilePath, 'w')
        fileStream.write(textBox.get(1.0, END))

        fileStream.close()



root = Tk()

root.title("TextEditor Deluxe")
#root.iconbitmap("encoolbild.jpg")
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
fileCascade.add_command(label="New", command=newFile)
fileCascade.add_command(label="Open", command=openFile)
fileCascade.add_command(label="Save", command=saveFile)
fileCascade.add_command(label="Save as", command=saveAsFile)
fileCascade.add_command(label="Exit", command=root.quit) #NYI Add to save or not if file is unsaved

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
infoBar = Label(root, text="words: NYI - letters: NYI", anchor=E)

infoBar.pack(fill=X,side=BOTTOM)












root.mainloop()










