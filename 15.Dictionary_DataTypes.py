'''#Note:
--Dictionaries contain key-value pairs, key are like a lists indexes.
--dictionaries are mutable .variable hold reference to dictionary values, not the dictionary value itself.
--Dictionaries are unordered, there is no "first" key value pair in a dictionary.
--the keys(), values(), and items() methods will return list like values of a dictionarys keys, values, and both keys values respectively.
--the get() method can return a default value if a key doesnt exist.
the setdefault() method can set a value if a key doesnt exist.
-- the pprint modules pprint() "pretty print" function can display a dictionary value cleanlyh. the pformat() function returns a string value of this output.

'''
'''# Dictionary acess key value
names={"name":"devaraj","age":"26","company":"TS"}
print(names["name"])


#String concatanation in using Dictionary
names={"name":"devaraj","age":"26","company":"TS"}
print("Hello, my name is " + names["name"]+' Working in Thundersoft')


#Dictionarys are unorder
names1={"name":"devaraj","age":"26","company":"TS"}
names2={"name":"devaraj","company":"TS","age":"26"}
print(names1==names2)


#in and not in operators
names={"name":"devaraj","age":"26","company":"TS"}
print('name' in names) #check key in the dictionary, out put is True
print('ravi' in names) #check key in the dictionary, out put is False
print('dev' not in names) #check key in the dictionary,out put is True

#The keys(),the values(),the items()--Dictionary method
spam={"animal":"elephant","bird":"dove","pant":"coconut"}
print(list(spam.keys()))#['animal', 'bird', 'pant']
print(spam.keys())#dict_keys(['animal', 'bird', 'pant'])
print(list(spam.items()))
print(list(spam.values()))


#Using for loop access The keys(),the values(),the items()--Dictionary method
spam={"animal":"elephant","bird":"dove","pant":"coconut"}
for i in spam.keys():
    print(i)
for j in spam.values():
    print(j)
for k in spam.items():
    print(k)

#dictionary using condition
spam={"animal":"elephant","bird":"dove","pant":"coconut"}
if 'animal' in spam:
    print(spam['animal'])

print(spam.get("pant",0))

#string concatanation
spam={"dress":5,"bottle":3}
print("im bringing " + str(spam.get(" napkin",0))+ " to the picnic")#add assignment

#change key value
dict={"name":"pavo","species":"peacock","age":"18"}
dict["age"]='19'
print(dict)

#add the new item in dictionary
dict={"name":"pavo","species":"peacock","age":"18"}
dict["nation"]='india'
print(dict)

#using if statment and add key &value
dict={"name":"pavo","species":"peacock","age":"18"}
if "colour" not in dict:
    dict["colour"]='blue'
    print(dict)


#using if statment and add key &value
dict={"name":"pavo","species":"peacock","age":"18"}
if "colour" not in dict:
    dict.setdefault("age",'blue')#by using detdefault fun you cant change exiting key value
    print(dict)

#character count
message='Python is very easy and important programming Langauge'
count={}
for letter in message:
    count.setdefault(letter,0)
    count[letter]=count[letter]+1
print(count)


#Upper Letter character count
message='ython is very easy and important programming Langauge'
count={}
for letter in message.lower():
    count.setdefault(letter,0)
    count[letter]=count[letter]+1
print(count)

#multi line letter count
# Note: 

''' message'''
message=
A Dynamic personality ready to have dedication towards betterment of organization through my technical and managerial skills owned by me and through my practical exposure towards the work to be done by me.
PROFESSIONAL SUMMARY Experience with C, C++, C#, and RTOS concepts.
Having good understanding on the Visual studio tools.
Knowledge on Perforce.
Knowledge on STLC.
Tools: QACT, JIRA, Git, Gerrit.
ACADEMIC DETAILS
B.E in Electronics and Communication Engineering in 2019 from Lovely Professional university, Jalandhar, Punjab with an aggregate of 7.04 CGPA.
Intermediate (+2) in 2015 from Narayana Junior College Nandyal, with an aggregate of 86.8%
SSC in 2013 from Good Shepherd English Medium School, Nandyal with an aggregate of 8.7 CGPA.
PROFESSIONAL SUMMARY
Software Trainee at ThunderSoft India Private Limited, Hyderabad (22 June 2019 - till date)
AWARDS AND ACHIEVEMENTS
Participated in multiple cultural activities throughout my schooling

count={}
for letter in message.upper():
    count.setdefault(letter,0)
    count[letter]=count[letter]+1
print(count)




























































