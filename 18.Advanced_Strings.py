''' string is character and its immutable
--String () can begin with  start and end with single quote(' ') and double quote(" ")
--escape character let you put quotes and other character that hard to type inside strings.
--raw strings will literally print any backslshesh in   the string  and ignore escape characters.
--multiline strings being and end with three quotes , and can span multiple lines.
--indexes, slices ,and the in and not in operators all work with strings.
print('Hello')
print("that is my car")

............................................
Escape character |   print as
............................................
\'                  single quote
\"                  double quote
\t                  tab
\n                  new line
\\                  back slash
........................................

#single quote \'
print('Hello my names\' devaraj nayak')

#double quotes \"
print("Hello my names\" devaraj\' nayak")

#new line \n
print("im working in good company\n gaining very\n good knowledge")

#tab line \t
print('kgf movie is\t awesome')

#back slash \\
print('kgf is the good movie\\ kgf2 is greatest\\ ever movie')

#The "that is royal\'s mech" string is regular , non raw string value.
print(r"that is royal\'s mech ")

#Multiline string
print(""" Dr. rajakumar is gratest singer\tand actor \nin the world!
he is legend of kannada film 
industry and never been like him""")


#Similarities btw list and strg, In strg is immuatble, but you can find index value but cant change,
spam='Hello devaraj!'
print(spam[1]) #you can find index value
#spam[0]='k'
#print(spam) #'str' object does not support item assignment
print("Hello "+"world ")

'''















































































































