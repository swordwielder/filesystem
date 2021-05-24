from arrays import DynamicArray
# from lilist import LinkedList
import sys
from termcolor import colored


class WrappedList:
    def __init__(self, lst):
         self._lst = lst
    def __getitem__(self, item):
        return self._lst[item]

class Folder:
    def __init__(self, parent, name):
        '''
        :param parent: parent directory
                 :param name: directory name
        '''
        self.parent = parent
        self.name = name
        # directory list
        self.folder = []
        # document list
        self.file = []

root = Folder(parent=None, name='home')
cur = root
path = 'home'

# Create a file
def touch(name):
    
    global cur

    #just to inform the error, doesn't exists in file
    if name in cur.file:
        # print(name)
        return print(f"touch: cannot create file '{name}': File exists")
    cur.file.append(name)
    return ''


# Create a directory
def mkdir(name):
    global cur, path
    
    for i in cur.folder:
        #Check if the name of directory already exists
        if name ==i.name:
            return print(f"mkdir: cannot create directory '{name}': File exists")

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
        return print(f'bash: cd: {name}: No such file or directory')


# List all files and directories
def ls():
    global cur
    for i in cur.file:
        print(i, end=' ')
    
    for i in cur.folder:
        print( colored(i.name,'blue'), end=' ' )
    print()

#main method to run the program
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