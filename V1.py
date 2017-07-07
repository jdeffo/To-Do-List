#Import Statements
from datetime import datetime
import datetime

#Global Variables
to_do_list = []

#Read from list file stored on machine
def list_read():
    print("File path: " + r'\Users\jeremydefossett\Source\Repos\To-Do-List\list.txt')
    global to_do_list
    with open("list.txt") as _list_file:
        to_do_list = [line.rstrip('\n') for line in _list_file]
    print(to_do_list)
    _list_file.close()
#Write single item to list file
def list_write(item):
    _list_writer = open('list.txt', 'w')
    for line in to_do_list:
        _list_writer.write(line + "\n")
    _list_writer.write(item)
    _list_writer.close()
    list_read()
#Write all to_do_list items to list file
def list_write_all():
    _list_writer = open('list.txt', 'w')
    for line in to_do_list:
        _list_writer.write(line + '\n')
    _list_writer.close()
    list_read()
#Remove item from to_do_list and list file
def rem_item(item):
    name = item.partition('|')[0]
    global to_do_list
    for item in to_do_list:
        if item.partition('|')[0] == name:
            print("Removed task: " + name)
            to_do_list.remove(item)
    list_write_all()
#Create new list
def create_list(name):
    _f = open(name, 'w')
    _f.close()
#Sort list by ASC
def sort_asc():
    #Get list of dates
    print("sort_desc")
    global to_do_list
    dates = []
    for item in to_do_list:
        tempDate = item.split('|')[-1]
        tempDate = tempDate.strip()
        dates.append(tempDate)
    #Sort Dates
    dates = sorted(dates, key=lambda x: datetime.datetime.strptime(x, '%d/%m/%y'))
    temp_list = []
    #Pair Dates w/ tasks
    for date in dates:
        for item in to_do_list:
            tempDate = item.split('|')[-1]
            tempDate = tempDate.strip()
            if date == tempDate:
                temp_list.append(item)
                rem_item(item)
                break;
    #Set New list
    to_do_list = temp_list
    print(to_do_list)
    #Write New list
    list_write_all()

#Sort by DESC
def sort_desc():
    global to_do_list
    #Sort ascending, and then reverse
    sort_asc()
    to_do_list.reverse()
    print(to_do_list)
    list_write_all()

create_list("list.txt")
list_read()
list_write("1 | Wednesday | 01/02/17")
list_write("2 | Friday | 01/05/17")
list_write("4 | Sunday | 01/07/17")
list_write("3 | Saturday | 01/06/17")
#rem_item('Aye | Wednesday | 01/01/2017')
sort_asc()
sort_desc()
#create_list("1")
