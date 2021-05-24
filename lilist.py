class Element:
	def __init__(self,x):
		self.data=x
		self.next=None  # will point at another Element


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
				s = s + " "
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
print(llist)


# obj = iter(llist)
# print(obj)
# print(' the list')
# print(llist)
# print('the i')



# for i in iterable_obj:
# 	print(i)
# 	# print(iterable_obj[i])

# print('the items')
# while True:
#     try:
#         # Iterate by calling next
#         item = next(iterable_obj)
#         print(item)
#     except StopIteration:
 
#         # exception will happen when iteration will over
#         break


