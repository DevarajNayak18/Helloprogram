'''
--Methods are the function that are called on values
--the index() list methos returns the index of an item in the list
--the append() list method adds a value to the end of the list
--the insert() list method add a vlaue anywhere in the list
--the remove() list method removes an item, specified by the value, from a list
-- the sort () list method sorts the item in list.
--the sort methods reverse=True keyword argument can sort in reverse order
--sorting happens in ASCII-BETICAL order, to sort normally, pass key=str.lower.
--these list methods operate on the list "in place", rather than returning a new list value.


#Index method
list=["dev","raj","nayak",'hanuma','kiran']
print(list.index("dev"))  #the index value is 0
print(list.index("nayak"))  #the index value is 2
print(list.index("kiran"))  #the index value is 4

#append ()method
list=['dev','hanuma','kiran']
list.append('rajahuli')
print(list)

#insert() method
list=['dev','hanuma','kiran']
list.insert(0,'ayyappa') #inserting ayyappa at index 0
print(list)

list=['dev','hanuma','kiran']
list.insert(3,'john') #inserting ayyappa at index 0
print(list)

#sort() Methos

spam=[1,2,-7,-5,10]
spam.sort()
print(spam)


list1=[1,2,3,10,0,5]
list2=sorted(list1)
print(list2)

list1=[11,0,20,21]
list1.sort()
print(list1)

#remove() Method
list3=["apple","orrange","mango","chiku"]
list3.remove('mango')
print(list3)

#Reverse of list

food=["rice","biriyani","fruitbol","roll"]
food.reverse()
print(food)

food=["aint","biriyani","fruit","cat","dog"]
food.sort(reverse=True)
print(food)

name='devaraj'
print(len(name))
print(name[-2:-5:-1])

#cant sort int and string in the list-- Error:TypeError: '<' not supported between instances of 'str' and 'int'
food=[1,2,3,"rice","biriyani","fruitbol","roll"]
food.sort()
print(food)



#sort
l=['z','a','Z','A']
l.sort()
print(l)
'''
#sort using key=str.lower case
l=['A','Z','a','z']
l.sort(key=str.lower)
print(l)


#sort using key=str.lower case
l=['A','Z','a','z']
l.sort(key=str.upper)
print(l)

