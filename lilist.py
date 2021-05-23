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
		return self
		


# main
# llist = LinkedList()
# llist.append(5)
# llist.append(2)
# print (llist)
