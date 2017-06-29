#global variables
todoList = []

#read function
def listRead():
    print("File path: " + r'\Users\jeremydefossett\Source\Repos\To-Do-List\list.txt')
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
    listRead()

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
    listRead()

#create list function
def createList(name):
    f = open(name, 'w')
    f.write('')
    f.close()

#Sort by ASC
def sortASC():
    #FINISH
    listWr = open('list.txt', 'w')
    listWr.close()

#Sort by DESC
def sortDESC():
    #FINISH
    listWr = open('list.txt', 'w')
    listWr.close()

createList("list.txt")
listRead()
listWrite("Aye | Wednesday | 01/02/2017")
listWrite("V2 | Friday | 01/05/2017")
remItem('Aye | Wednesday | 01/01/2017')
#createList("1")
