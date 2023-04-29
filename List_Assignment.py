'''1.#sum of all the element
list=[3,5,6,7,3,5,7,10]
sum=0
count=0
for i in list:
    sum=sum+i
    count+=1
print(sum)


#2.Within a list print duplicate and unique values
list=[1,2,3,2,5,10,11,5]
list1=set(list)
print("the with duplicate list ",list)
print("the duplicate removed list ",list1)
print([i for i in list if list.count(i)==1])

#3.Reverse List except Last Element using Slicing
l=[1,3,4,7,4,9,5]
print(l[:-1])


#Write a program to reverse strings in a given list of string values
def reverse_string(rev_str):
    result=[x[::-1] for x in rev_str]
    return result
l=['One','Two','Three']
print("Orginat List",l)
print("Reverse string List")
print(reverse_string(l))


#Print even an odd number in a list without using list comprehension
list=[1,3,8,10,4]
count=0
for i in list:
    if i%2==0:
        print("even number :",i)
        count+=1
for i in list:
    if i%2!=0:
        print("odd number : " ,i)

#program to count positive and negative numbers in a List
list=[1,-3,-8,4,10]
even_count,odd_count=0,0
for i in list:
    if i>=0:
        even_count+=1
    else:
        odd_count+=1
print("Positive numbers: ",even_count)
print("Negative numbers: ",odd_count)

#Write a program to find value 20 in the list, and if it is present, replace it with 200.
Only update the first occurrence of an item.

list1 = [5, 10, 15, 20, 25, 50, 20]
print("The original list: ",list1)
for i in list1:
    if i==20:
       index=list1.index(20)
       list1[index]=200
      # list1[6]=200
print("updated 200 index list ",list1)


my_list = [10, 20, 30, 20, 40, 50, 20]
while 20 in my_list:
    index = my_list.index(20)
    my_list[index] = 200
print(my_list)
'''






















#Expected output: [5, 10, 15, 200, 25, 50, 20]

















































