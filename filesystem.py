from arrays import DynamicArray
from lilist import LinkedList
import sys

class Folder:
    def __init__(self, parent, name):
        '''
        :param parent: parent directory
                 :param name: directory name
        '''
        self.parent = parent
        self.name = name
        # directory list
        # self.folder = DynamicArray()
        self.folder = []
        # document list
        # self.file = DynamicArray()
        self.file = []

root = Folder(parent=None, name='home')
cur = root
path = 'home'

# Create a file
def touch(name):
    
    global cur
    # print('the current file is')
    # print(cur.file)

    #just to inform the error, doesn't exists in file system.
    if name in cur.file:
        # print(name)
        return print(f"There is a file with the same name as {name}, overwritten")
    cur.file.append(name)
    return ''


# Create a directory
def mkdir(name):
    global cur, path
    # print('the name is')
    # print(name)
    # print('the current file is')
    # print(cur.folder)
    # for i in cur.folder:
    #     print('the i is')
    #     print(i)
    for i in cur.folder:
        if name ==i.name:
            return print(f"mkdir: cannot create directory '{name}': File exists")
    # if name in cur.folder:
    #     return print("shit already exists")
    folder = Folder(parent=cur, name=name)
    cur.folder.append(folder)
    return ''

# Change the current directory
def cd(name):
    global cur, path
    if name == '..':
        if cur.parent != None:
            path = path[:(len(path)-len(cur.name))-1]
            cur = cur.parent
    else:
        for i in cur.folder:
            if i.name == name:
                cur = i
                path = path + '/' + name
                return
        return print('Cannot find the specified folder!')


# List all files and directories
def ls():
    global cur
    for i in cur.file:
        print(i, end=' ')
    for i in cur.folder:
        print(i.name, end=' ')
    print()


if __name__ == '__main__':
    while True:
        print(path, end=':$ ')
        command = input().split(' ')
        if command[0] == 'touch':
            for i in range(1,len(command)):
                try:
                    touch(command[i])
                except:
                    print('Command error')

        elif command[0] == 'mkdir':
            for i in range(1, len(command)):
                try:
                    mkdir(command[i])
                except:
                    print('Command error')

        elif command[0] == 'cd':
            try:
                cd(command[1])
            except:
                print('Command error')
        elif command[0] == 'ls':
            ls()
        elif command[0] == 'exit':
            sys.exit('Exited python file system')
        else:
            print('No such command')