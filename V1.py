#File paths: printf(r'C:\User\....'')

#print the direction
print("File path: " + r'C:\Users\Deffo\Source\Repos\To-Do-List\list.txt')

#open the File
with open("list.txt") as listf:
    todoList = [line.rstrip('\n') for line in listf]
print (todoList)

#close the file
listf.close()
#write to the File
listWr = open('list.txt', 'w')
for line in todoList:
    listWr.write(line + "\n")
listWr.write("Finish V1 | Friday")

listWr.close()

with open('list.txt') as listCh:
    newContents = [line.rstrip('\n') for line in listCh]
print(newContents)

listCh.close()
