'''
#Example 1: Print the first 10 natural numbers using for loop.
print("The first 10 natural number are : ")
for i in range(1,11):
    print(i)

#Example 2: Python program to print all the even numbers within the given range.
for i in range(1,10):
    if i%2==0:
        print("the even number : ",i)
for i in range(1,10):
    if i%2!=0:
        print("the odd number : ",i)

#Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
sum=0
for i in range(1,11):
    sum=sum+i
print("the sum of all : ",sum)


#Example 4: Python program to calculate the sum of all the odd numbers within the given range.
sum=0
for i in range(1,11):
    if i%2!=0:
        sum=sum+i
print(sum)

#Example 5: Python program to print a multiplication table of a given number

num=5
for i in range(1,11):
    print(num,"x",i,"=",num*i)


#Example 6: Python program to display numbers from a list using a for loop.
list=[1,2,3,5,56]
for i in list:
    print(i)


#Example 7: Python program to count the total number of digits in a number.
number=int(input("enter digit number : "))
count=0
while number!=0:
    number//=10
    count+=1
print("the number of digit in this integer: ",count)


#Example 8: Python program to check if the given string is a palindrome.

my_str=input("enter the string : ")#MaDam
my_str=my_str.casefold() #change into lower order madam
rev_str=reversed(my_str) #reverse it madam
if list (my_str)==list (rev_str): #compare it
    print("palindrome")
else:
    print("not palindrome")


#Example 9: Python program that accepts a word from the user and reverses it.
word=input("enter a word : ") #dev
rev=""  #"ved "
count=0
for i in word:
    rev=i+rev
    count=count+1
print(rev)



#Example 10:Python program to check if the number is an Armstrong number or not
#153=1*1*1+5*5*5+3*3*3
num=int(input("enter number : "))
sum=0
temp=num
while  temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if num==sum:
    print("the given number is amstrong")
else:
    print("the given number is not amstrong")

#Example 11: Python program to count the number of even and odd numbers from a series of numbers.
list=[1,2,4,5,7,8,12,15]
even_count,odd_count=0,0
for i in list:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("even number ",even_count)
print("odd number ",odd_count)

list1 = [10, 21, 4, 45, 66, 93, 1]
even_count, odd_count = 0, 0
# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)

'''







































