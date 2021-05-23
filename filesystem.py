from arrays import DynamicArray
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

def touch(name):
    # Create a file
    global cur
    if name in cur.file:
        return 'There is a file with the same name, the new file failed!'
    cur.file.append(name)
    return


def mkdir(name):
    # Create a directory
    global cur, path
    if name in cur.folder:
        return f"mkdir: cannot create directory '{name}': File exists"
    folder = Folder(parent=cur, name=name)
    cur.folder.append(folder)
    return 


def cd(name):
    # Change the current directory
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
        print(' ', i, end=' ')
    for i in cur.folder:
        print(' ', i.name, end=' ')
    print()


if __name__ == '__main__':
    while True:
        print(path, end=': ')
        command = input().split(' ')
        if command[0] == 'touch':
            for i in range(1,len(command)):
                try:
                    print(touch(command[i]))
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