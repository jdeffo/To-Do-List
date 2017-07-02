from Tkinter import *

#root
root = Tk()

#frames
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#topFrame buttons
addList = Button(topFrame, text='+', fg='green')
remList = Button(topFrame, text='X', fg='red')

#buttomFrame buttons
addTask = Button(bottomFrame, text='+', fg='green')
remTask = Button(bottomFrame, text='-', fg='red')

#topFrame labels
title = Label(topFrame, text='To-Do')

#display top buttons
addList.pack()
remList.pack()

#display bottom buttons
addTask.pack()
remTask.pack()

#display window
root.mainloop()
