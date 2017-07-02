from datetime import datetime
import datetime

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

#Write all
def listWriteAll():
    listWr = open('list.txt', 'w')
    for line in todoList:
        listWr.write(line + '\n')
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
    #Get list of dates
    print("SortDESC")
    global todoList
    dates = []
    for line in todoList:
        tempdate = line.split('|')[-1]
        tempdate = tempdate.strip()
        dates.append(tempdate)
    #Sort Dates
    dates = sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%d/%m/%y'))
    tempList = []
    #Pair Dates w/ tasks
    for date in dates:
        for line in todoList:
            tempdate = line.split('|')[-1]
            tempdate = tempdate.strip()
            if date == tempdate:
                tempList.append(line)
                remItem(line)
                break;
    #Set New list
    todoList = tempList
    print(todoList)
    #Write New list
    listWriteAll()

#Sort by DESC
def sortDESC():
    global todoList
    #Sort ascending, and then reverse
    sortASC()
    todoList.reverse()
    print(todoList)
    listWriteAll()

createList("list.txt")
listRead()
listWrite("Aye | Wednesday | 01/05/17")
listWrite("V2 | Friday | 01/02/17")
#remItem('Aye | Wednesday | 01/01/2017')
sortASC()
sortDESC()
#createList("1")
