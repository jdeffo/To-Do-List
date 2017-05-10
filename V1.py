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

#write function
def listWrite(item):
    listWr = open('list.txt', 'w')
    for line in todoList:
        listWr.write(line + "\n")
    listWr.write(item)
    listWr.close()

#remove function
def remItem(item):
    name = item.partition('|')[0]
    listWr = open('list.txt', 'w')
    for line in todoList:
        if line.partition('|')[0] == name:
            print("Removed task: " + name)
        else:
            listWr.write(line + '\n')
    listWr.close()

#create list function
def createList(name):
    f = open(name, 'w')
    f.write('')
    f.close()

#listRead()
#listWrite("Aye | Wednesday")
#listRead()
#remItem('V1 | Friday')
#listRead()
#createList("1")
