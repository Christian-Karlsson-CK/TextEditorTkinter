from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter import messagebox
from reportlab.pdfgen import canvas

import os

filePath = None

copiedText = None
words = 0
letters = 0


def newFile():
    global filePath
    global words
    global letters
    textBox.delete("1.0", END)
    root.title("TextEditor Deluxe - New File")
    infoBar.config(text=f"New File | Unsaved  | words: {words} | letters: {letters}")
    filePath = None
    countWordsAndLetters()

def openFile():
    global filePath
    global words
    global letters
    textBox.delete("1.0", END)

    filePath = filedialog.askopenfilename(title="Open File", initialdir=filePath, filetypes=(("Text Files", "*.txt"), ("All files", "*.*")))
    filename = os.path.basename(filePath)
    root.title(f"TextEditor Deluxe - {filename}")

    fileStream = open(filePath, 'r')
    text = fileStream.read()
    textBox.insert(1.0, text)
    fileStream.close()

    addProgrammingForeground()
    countWordsAndLetters()
    infoBar.config(text=f"{filePath} | Saved  | words: {words} | letters: {letters}")

def saveFile():
    global filePath
    global words
    global letters
    if filePath != None:
        filename = os.path.basename(filePath)
        root.title(f"TextEditor Deluxe - {filename}")
        infoBar.config(text=f"{filePath} | Saved  | words: {words} | letters: {letters}")
        fileStream = open(filePath, 'w')
        fileStream.write(textBox.get(1.0, END))
        fileStream.close()
    else:
        saveAsFile()

def saveAsFile():
    global filePath
    global words
    global letters
    if filePath != None:
        dir = os.path.dirname(filePath)
        newFilePath = filedialog.asksaveasfilename(defaultextension=".*", initialdir=dir, title="Save File")
    else:
        newFilePath = filedialog.asksaveasfilename(defaultextension=".*", title="Save File")

    if newFilePath:
        filePath = newFilePath
        filename = os.path.basename(newFilePath)
        root.title(f"TextEditor Deluxe - {filename}")
        infoBar.config(text=f"{newFilePath} | Saved  | {words} | letters: {letters}")

        fileStream = open(newFilePath, 'w')
        fileStream.write(textBox.get(1.0, END))

        fileStream.close()

def convertToPDF():
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if filename:
        c = canvas.Canvas(filename)
        text = textBox.get(1.0, "end-1c")  # end-1c removes newlines after last letter.
        c.drawString(50, 700, text)  # Draw the text on the PDF canvas
        c.save()

def convertToBinary(string):
    binary_string = ''
    for char in string:
        if char == '\n':
            binary_string += '\n'
        else:
            binary_string += format(ord(char), '08b') + ' '
    return binary_string.strip()

def saveAsBinaryFile():

    binaryFilePath = filedialog.asksaveasfilename(defaultextension=".*", title="Save File")

    if binaryFilePath:
        text = textBox.get(1.0, END)
        fileStream = open(binaryFilePath, 'w')
        fileStream.write(convertToBinary(text))

        fileStream.close()

def ShowAboutPopup():
    messagebox.showinfo("About", "TextEditor Deluxe\nVersion 1.0\n\nThis is a simple text editor application.")

def cutText(event=None):
    global copiedText

    if event:
        copiedText = root.clipboard_get()
    
    else:
        if textBox.selection_get():
            copiedText = textBox.selection_get()
            root.clipboard_clear()
            root.clipboard_append(copiedText)
            textBox.delete("sel.first", "sel.last")

def copyText(event=None):
    global copiedText

    if event:
        copiedText = root.clipboard_get()

    else:
        if textBox.selection_get():
            root.clipboard_clear()
            root.clipboard_append(copiedText)
            copiedText = textBox.selection_get()

def pasteText(event=None):
    global copiedText

    if event:
        copiedText = root.clipboard_get()

    else:
        if copiedText != None: 
            cursor = textBox.index(INSERT)
            textBox.insert(cursor, copiedText)

def applyBoldToSelected():
    boldFont = font.Font(textBox, textBox.cget("font"))
    boldFont.configure(weight="bold")

    textBox.tag_configure("bold", font=boldFont)
    curTags = textBox.tag_names("sel.first")

    if "bold" in curTags:
        textBox.tag_remove("bold", "sel.first", "sel.last")
    else:
        textBox.tag_add("bold", "sel.first", "sel.last")

def applyItalicsToSelected():
    italicsFont = font.Font(textBox, textBox.cget("font"))
    italicsFont.configure(slant="italic")

    textBox.tag_configure("italic", font=italicsFont)
    curTags = textBox.tag_names("sel.first")

    if "italic" in curTags:
        textBox.tag_remove("italic", "sel.first", "sel.last")
    else:
        textBox.tag_add("italic", "sel.first", "sel.last")

def applyColorToSelected():

    choosenColor = colorchooser.askcolor()[1]
    
    if choosenColor:
        colorFont = font.Font(textBox, textBox.cget("font"))

        textBox.tag_configure("colored", font=colorFont, foreground=choosenColor)
        curTags = textBox.tag_names("sel.first")

        if "colored" in curTags:
            textBox.tag_remove("colored", "sel.first", "sel.last")
        else:
            textBox.tag_add("colored", "sel.first", "sel.last")

def countWordsAndLetters(event=None):
    global filePath
    global words
    global letters
    text = textBox.get("1.0", "end-1c")
    words = len(text.split())
    letters = len(text.replace(" ", "").replace("\n", ""))
    infoBar.config(text=f"{filePath} | Unsaved | words: {words} | letters: {letters}")

def addProgrammingForeground(event=None):
    purpleKeywords = ["for", "while", "if", "else", "in", "{","}", "from", "import", "break"]
    blueKeywords = ["False","True","not","def","class","global","None", "lambda"]
    yellowKeywords = ["[", "]"]
    redKeywords = ["(", ")"]

    # Remove previous highlighting
    textBox.tag_remove("purpleKeywords", "1.0", "end")
    textBox.tag_remove("blueKeywords", "1.0", "end")
    textBox.tag_remove("yellowKeywords", "1.0", "end")
    textBox.tag_remove("redKeywords", "1.0", "end")

    for word in purpleKeywords:

        start = "1.0"
        while True:
            # Search for the next occurrence of the keyword
            start = textBox.search(word, start, stopindex="end", nocase=True)
            if not start:
                break
            end = f"{start}+{len(word)}c"
            textBox.tag_add("purpleKeywords", start, end)
            start = end

    for word in blueKeywords:
        start = "1.0"
        while True:
            # Search for the next occurrence of the keyword
            start = textBox.search(word, start, stopindex="end", nocase=True)
            if not start:
                break
            end = f"{start}+{len(word)}c"
            textBox.tag_add("blueKeywords", start, end)
            start = end
        
    for word in yellowKeywords:
        start = "1.0"
        while True:
            # Search for the next occurrence of the keyword
            start = textBox.search(word, start, stopindex="end", nocase=True)
            if not start:
                break
            end = f"{start}+{len(word)}c"
            textBox.tag_add("yellowKeywords", start, end)
            start = end
    
    for word in redKeywords:
        start = "1.0"
        while True:
            # Search for the next occurrence of the keyword
            start = textBox.search(word, start, stopindex="end", nocase=True)
            if not start:
                break
            end = f"{start}+{len(word)}c"
            textBox.tag_add("redKeywords", start, end)
            start = end

    # Configure the tag to have a different color
    textBox.tag_configure("purpleKeywords", foreground="purple")
    textBox.tag_configure("blueKeywords", foreground="blue")
    textBox.tag_configure("yellowKeywords", foreground="yellow")
    textBox.tag_configure("redKeywords", foreground="red")


root = Tk()

root.bind('<Control-x>', cutText)
root.bind('<Control-c>', copyText)
root.bind('<Control-v>', pasteText)

root.title("TextEditor Deluxe")
#root.iconbitmap("encoolbild.jpg")
root.geometry("1175x660")

toolbar = Frame(root)
toolbar.pack(fill=X)

mainFrame = Frame(root)
mainFrame.pack(pady=3)

textScroll = Scrollbar(mainFrame)
textScroll.pack(side=RIGHT, fill=Y)

consolasFont = font.Font(family="Consolas", size=16)

textBox = Text(mainFrame, width=95, height=25, font=(consolasFont), selectbackground="#63B6EC", 
               selectforeground="black", undo=True, yscrollcommand=textScroll.set)
textBox.bind("<KeyRelease>", lambda event: (countWordsAndLetters(event), addProgrammingForeground(event)))
textBox.pack()

textScroll.config(command=textBox.yview)

topMenu = Menu(root)
root.config(menu=topMenu)


fileCascade = Menu(topMenu, tearoff=False)
topMenu.add_cascade(label="File", menu=fileCascade)
fileCascade.add_command(label="New", command=newFile)
fileCascade.add_command(label="Open", command=openFile)
fileCascade.add_command(label="Save", command=saveFile)
fileCascade.add_command(label="Save as", command=saveAsFile)
fileCascade.add_command(label="Exit", command=root.quit) #NYI Add to save or not if file is unsaved

editCascade = Menu(topMenu, tearoff=False)
topMenu.add_cascade(label="Edit", menu=editCascade)
editCascade.add_command(label="Cut", command=cutText)
editCascade.add_command(label="Copy", command=copyText)
editCascade.add_command(label="Paste", command=pasteText)

exportCascade = Menu(topMenu, tearoff=False)
topMenu.add_cascade(label="Export", menu=exportCascade)
exportCascade.add_command(label="PDF", command=convertToPDF)

convertCascade = Menu(topMenu, tearoff=False)
topMenu.add_cascade(label="Convert", menu=convertCascade)
convertCascade.add_command(label="To Binary", command=saveAsBinaryFile)


aboutCascade = Menu(topMenu, tearoff=False)
topMenu.add_cascade(label="About", menu=aboutCascade)
aboutCascade.add_command(label="About", command=ShowAboutPopup)


boldButton = Button(toolbar, text="Bold", command=applyBoldToSelected)
boldButton.grid(row=0, column=0, sticky=W, padx=4)
italicsButton = Button(toolbar, text="Italics", command=applyItalicsToSelected)
italicsButton.grid(row=0, column=1, sticky=W, padx=4)

colorButton = Button(toolbar, text="Text Color", command=applyColorToSelected)
colorButton.grid(row=0, column=2, sticky=W, padx=4)

infoBar = Label(root, text="New File | Unsaved | words: 0 - letters: 0", anchor=E)

infoBar.pack(fill=X,side=BOTTOM)












root.mainloop()










