class Element:
	def __init__(self,x):
		self.data=x
		self.next=None  # will point at another Element


# class TeamIterator:
#    ''' Iterator class '''
#    def __init__(self, team):
#        # Team object reference
#        self._team = team
#        # member variable to keep track of current index
#        self._index = 0
#    def __next__(self):
#        ''''Returns the next value from team object's lists '''
#        if self._index < (len(self._team._juniorMembers) + len(self._team._seniorMembers)) :
#            if self._index < len(self._team._juniorMembers): # Check if junior members are fully iterated or not
#                result = (self._team._juniorMembers[self._index] , 'junior')
#            else:
#                result = (self._team._seniorMembers[self._index - len(self._team._juniorMembers)]   , 'senior')
#            self._index +=1
#            return result
#        # End of Iteration
#        raise StopIteration

	   
# class Team:
#    '''
#    Contains List of Junior and senior team members and also overrides the __iter__() function.
#    '''
#    def __init__(self):
#        self._juniorMembers = list()
#        self._seniorMembers = list()
#    def addJuniorMembers(self, members):
#        self._juniorMembers += members
#    def addSeniorMembers(self, members):
#        self._seniorMembers += members
#    def __iter__(self):
#        ''' Returns the Iterator object '''
#        return TeamIterator(self)


class LinkedList:
	def __init__(self):
		self.head=None
		self.tail=None
		self.length=0

	def append(self,x):
		# create a new Element
		e = Element(x)
		# special case: list is empty
		if self.head==None:
			self.head=e
			self.tail=e
		else:
			# keep head the same
			self.tail.next=e
			self.tail=e
		self.length+=1

	def __str__(self):
		s = ""
		walker=self.head
		while walker!=None:
			s = s + str(walker.data)
			walker = walker.next 
			if walker != None:
				s = s + ","
		return s	

	def __iter__(self):
		return (self.next.data for self.head in range(self.length))
		
llist = LinkedList()
llist.append('a')
llist.append('b')
llist.append('c')
llist.append('d')
llist.append('e')
llist.append('f')
iterable_obj = list(llist)

print(' the list')
print(llist)
print('the i')
for i in iterable_obj:
	print(i)
	# print(iterable_obj[i])

print('the items')
while True:
    try:
        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:
 
        # exception will happen when iteration will over
        break


