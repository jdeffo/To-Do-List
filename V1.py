#global variables
todoList = []

#read function
def listRead():
    print("File path: " + r'C:\Users\Deffo\Source\Repos\To-Do-List\list.txt')
    global todoList
    with open("list.txt") as listf:
        todoList = [line.rstrip('\n') for line in listf]
    print(todoList)
    listf.close()

def listWrite(item):
    listWr = open('list.txt', 'w')
    for line in todoList:
        listWr.write(line + "\n")
    listWr.write(item)
    listWr.close()

listRead()
listWrite("Aye | Wednesday")
listRead()
