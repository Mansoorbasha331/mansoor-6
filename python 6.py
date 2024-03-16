#s1= "hello world "
#fst=s1{0}. upper ()
#1st = s1 (-1) upper ()
#print (fst+s1[1: len(s1)-1]+1st)

s1 = input("enter the string: ")
fst = s1[0].upper()
lst = s1[-1].upper()

print(fst+s1[1:len(s1)-1]+lst)

#print(s1.replace('h', 'H'))
#print(s1.replace('d', "D"))
n=128
temp=n
f1=0
while n!=0:
    rem=n%10
    check=temp%rem
    if check!=0:
        f1=1
        n=n//10
        
    if f1==0:
        print("yes")
    else:
        print("no")
230 LEKKALA AKASH REDDY
10:24 AM
n = int(input(" enter number : "))
temp = n
f1 = 0
while n!= 0:
    rem = n%10
    check = temp%rem
    if check!=0:
        f1=1
    n=n// 10   
if f1==0:
    print("YES")
else:
    print("N0")
n = int(input(" enter number : "))
temp = n
f1 = 0
while n!= 0:
    rem = n%10
    check = temp%rem
    if check!=0:
        f1=1
    n=n// 10   
if f1==0:
    print("YES")
else:
    print("N0")
if f1==0:
    print("yes")
else:
    print("no")


n = 128
for i in str(n):
    print(i)


l1 = [8, 9, 0, 7]
l2 = [7, 6, 5, 4]
l3=[]
for val in range(len(l1)):
    ans = (l1[val]+l2[val])
    l3.append(ans)
print(l3)

#! -------> set

# ? charateristics of set
1.) set can be crated using {}
2.) the elements inside set are not indexed
3.)does not allow duplicate values
4.)it unordered
5.) heterogenous
6.) mutable or changable
''''

# Eg:1
s1 = {9, 9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
print(s1)

Eg:2
s2 = {5, 8, 98, [9, 0]}
print(s2) --> error

# * Eg:3
min(), ma(), len()

# *eg
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
# add()
s1.add(43)
print(s1)

# update()
s1.update(9, 0)
print(s2)
# *eg
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
# add()
s1.add(43)
print(s1)

# update()
s1.update(9, 0)
print(s1)

# ? to delete element inside set
s1 = {8, 78, 67, 'ui'}

# pop() # to dlete one element randonly
s1.pop()
print(s1)

remove()
s1.remove(978)
print(s1)

discard()
s1.discard(8967)
print(s1)

clear()l1 = []
l1 = {}
print(type(l1)) --> datatype is dict

s1 = set() # to create empty set
print(type(s1))

s1 = {8, 9, 0}
s1.clear()
print(s1)

del s1
print(s1)
'''
# * join the sets
s1 = {9, 0, 8}
s2 = {9.90, "card", 't', 56}
# union() --> to combin 2 sets
s3 = s1.union(s2)
print(s3)

# * intersection() --> to get common elements inside set
s1 = {4, 5, 6}
s2 = {5, 6, 7, 8}
print(s1.intersection(s2))

# * difference()
s1 = {4, 5, 6}
s2 = {5, 6, 7, 8}
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmtric_difference(s2))

# isdisjoit(), issubset(), issuperset()
#isdisjoint(), issubset, issuperset()

s1 = {8,9,0}
s2 = {6,7,5,8,9,0}

print(s1.issubset(s2))
print(s2.issuperset(s1))

s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}

#n1 = {1,2,3} #--->s1
for val in s1:
    if val in s2:
       print("its  jointset")

#? o/p ---> its a joinset
# ! ---> diction
# ? delete element from dictionary
d1 = {1:100, 2:200, 3:300, 4:400]
# popitem() # ---> to delete last key value pair in dict
d1.popitem()
print(d1)

pop()
d1.pop(2) # 2 is the key in dictionary
print(d1)

clear(), del

join 2 dictionary
d1 = {1:100, 2:200, 3:300, 4:400}
d2 = {"a":"apple", "b":"boy", "g":"game"}
d1.update(d2)
print(d1)

get() ----> used to get the value from a key
d1 = {1:100, 2:200, 3:300, 4:400}
print(d1[90])
print(d1.get(90))

to print all the keys()
print(d1.keys())
print(type(d1.keys()))

to print all the values
print(d1.values())

# * iterating dictionary
for val in d1: # to  iterate values alone
    print(val)
for val in d1.values(): # to iterate values alone
    print(val)

to get both key and values
for key, val in d1.items():
    print(key, val)
    
Return a set of elements present in Set A or B, but not both

set3 = set()
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50 ,60, 70}
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
       set3.add(val)

 
