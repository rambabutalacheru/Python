#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print ('test')


# In[ ]:


x=1.25*0.2
p = 500*x
print (p)


# In[ ]:


p


# In[ ]:


print("The total profit earned is $", p)


# In[ ]:


tesla_car = 100
is_tesla_car_expensive = tesla_car>=99
print("is tesl car expensive?", is_tesla_car_expensive)
a=1
b=2
c=3
d=1
a==2
c<=a
b>=c
b<=c
a==d


# In[ ]:


temperature = 102
is_temperature_high = temperature>=79
print("is temperature high?", is_temperature_high)


# In[ ]:


not (a>=2 or c>=1)


# In[ ]:


not a==1


# In[ ]:


# CA result 
a=86
b=40
c=48
d=52
e=50
f=40
g=46

total = a+b+c+d+e+f+g
total1 = a+b+c+d
total2 = e+f+g

student_pass = total>=350 and a>=40 and b>=40 and c>=40 and d>=40 and e>=40 and f>=40 and g>=40

group1_clear = total1>=200 and a>=40 and b>=40 and c>=40 and d>=40

group2_clear = total2>=150 and e>=40 and f>=40 and g>=40

exemptions = a>=60 or b>=60 or c>=60 or d>=60 or e>=60 or f>=60 or g>=60 

print ("Group1=",total1,"Group2=", total2, "Total",total)


print ("is student passed?", student_pass)

print ("is group1 cleared?", group1_clear)

print ("is group2 cleared?", group2_clear)

print("any exemptions?", exemptions)
type(a)
type(exemptions)
if student_pass == True:
    print("pass and the total is {}" .format(total))
    
else: print("Fail")
    


# In[ ]:


price = 5>8
price


# In[ ]:


x = "I LOVE YOU"
x[7]
"LOVE" in x
"  " in x
LONE = x.replace("V", "N")
LONE
weekdays = "sun, mon, tue, wed, thu, fri, sat"
weekdays.split(",")


# In[ ]:


Question = ("It takes {} hours to learn python, {} hours to learn Java and {} hours to learn SAP FICO")
p = 100
q = 200
r = "YES"
Answer = Question.format(p,q,r)
Answer
Both = Question + ".  " +  Answer + "  " +str(p)
Both


# In[ ]:


List1 = ("Ram", "Sow", "Vijay")
type(List1)
List2 = ('Ram', 'Sow', 'Vijay', "Dee")
type(List2)
len(List1)
print("length of" , List1, List2, "end is", len(List2))
List3 = ["Ram", "Sow", "Vijay"]
type(List3)
List4 = ['python', 'java', 'javascript']
len(List4)
type(List4)
List4[0:3]
List4[-1]

List6 = [1,2,3,4,5]
List6[-1]
List6[1] = 1
List6

List6.insert (1,"Ram")
List6
List6.append('Sow')
List6.remove(5)
List6.pop(1)
"Sow" in List6

if "Dee" in List2 == True:
    
    print("Dee is in List2")
    
else: print("No")

"Dee" in List2
    

for letters in "INDEPENDENCE" :
    print("Letter",letters)
    
List99 = ("Ram", "Raj", "Ravi", "Suji")

print(List99)

for Names in List99:
    print(Names)
    
for i in range(len(List1),1):
    print(i, List1[1,2])
    

    
    


# In[ ]:


student1 = {"Name" : "Ram", "Age" : 30, "IQ Levels" : "High", "Married?" : "No"}
student1
len(student1)
student1["Married?"] = "Yes"
student1.items()


# In[ ]:


a=6

if a<10:
    print("this is the number {} less than 10". format(a))

print (a)


# In[ ]:


List1 = ("Ram", "Sow", "Vijay")
type(List1)

for Names in List1 :
    print (Names)
    
    


# In[ ]:


a1 = 1
a2 = 2
a3 = 3
a4 = 4

if a1 == a2 or a4 == 2:
    print("yes")
    
else: print ("no")


# In[ ]:


number = 1
i =1
while i<=10:
   
    number = number *i

    i = i+1

print(number)


# In[145]:


a,b,c,d,e,f,g = 60, 62, 86,38, 46, 57, 58
h =a+b+c+d+e+f+g
i = a+b+c+d
j = e+f+g

print("Group - 1")
if a>=60:
    print(str(a)+" E")
    
else:
    print(a)
    
if b>=60:
    print(str(b)+" E")
    
else:
    print(b)
    
if c>=60:
    print(str(c)+" E")
    
else:
    print(c)
    
if d>=60:
    print(str(d)+" E")
    
else:
    print(d)
    
    
print("Group - 2")

if e>=60:
    print(str(e)+" E")
    
else:
    print(e)
    
if f>=60:
    print(str(f)+" E")
    
else:
    print(f)
    
if g>=60:
    print(str(g)+" E")
    
else:
    print(g)

print ("Toatl= {},".format(h),"Group1= {},". format(i), "Group2= {}".format(j))

tvalue = h>=350 and a>=40 and b>=40 and c>=40 and d>=40 and e>=40 and f>=40 and g >=40

g1value = i>=200 and a>=40 and b>=40 and c>=40 and d>=40

g2value = j>=150 and e>=40 and f>=40 and g >=40

if tvalue == True:
    
    print("Result = Pass")
    
elif g1value == True:
    
    print ("Result = Group1 pass")
    
elif g2value == True:
    
    print ("Result = Group2 pass")
    
elif a >=60 or b>=60 or c>=60 or d>=60 or e>=60 or f>=60 or g>=60:

    print("Result = Exemption")
    
elif  tvalue != True:
    print("Result = Fail")



# In[ ]:


weekdays = ["sunday", "monday","tuesday","wednesday","thursday","friday", "saturday"]


"sunday" in weekdays

variable = "friday" in weekdays

weekdays.remove("friday")
weekdays.insert(2,"anotherday")
weekdays[0:2]

50*101
for char in "RAMBABU":
    print(char)
    
for letters in "INDIA":
    print ("Vertical order of letters in India is", letters)

 


# In[ ]:


x = 1
y = 1

while y<=99:
    
    y =y+1
    x = x+y
print(x)

student = { "name" : "ram",
        "age" : 30,
        "nationality": "india",
        "collage":"kent"}
student
student.keys()
student.items()
student.values()



    
for i in range(21):
    print(i)
    
def greet(name):
    print("Hi {}! Welcome to the Land of humans! How can we help you today?" .format(name))
greet(x)


# In[ ]:


x= "hi"
test_list =[1,2]
test_list
test_list.append(x)
test_list


# In[ ]:




        


def iseven(even_list):
    number_list = []
    for number in even_list:
        if number % 2 == 0:
            number_list.append(number)
            
    return number_list

newlist = iseven([1,2,3,4,5,6,7,8])
newlist
    


# In[ ]:


def EMI(p,r,n,d=0):
    try:
        amount = ( (p-d)  *  (r*(0.01/12) * (1+(r*(0.01/12))**(n*12) )/  (((1+(r*0.01/12))**(n*12))-1)
    except ZeroDivisionError:
        amount = None
    amount = math.ceil(amount)
    return(amount)


# In[ ]:


emi1 = EMI(1260000,10,8,300000)
emi1


# In[ ]:


emi2 = EMI(1260000,8,10)
emi2


# In[ ]:


if emi1<emi2 :
    print("Option-1 has lower EMI {} compared to Option-2 {}".format(emi1,emi2))
else:  print("Option-2 has lower EMI {} compared to Option-1 {}".format(emi2,emi1))


# In[ ]:


loanemi1 = EMI(800000,7,6,200000)
loanemi2 = EMI(60000,12,1)

print("Toatal EMI paid per month = ${}".format(loanemi1+loanemi2))


# In[ ]:


EMI


# In[ ]:


interest = ((EMI(100000,9,10))*12*10)-100000
print("Total interest paid = {}".format(interest))


# In[ ]:


interest1 = EMI(100000,9,10)
interest2 = EMI(100000,0,10)
print("Total interest paid = {}".format(interest1-interest2))


# In[ ]:


EMI


# In[ ]:


EMI(100000,10,2,10000)


# In[ ]:


def x(a,b):
    try : c = a/b
        except ZeroDevisionError:
        return(0)
            
            
            
        


# In[ ]:


def trip_cost(f,h,n,c,w):
    cost = f+(h*n)+(w*c)
    return(cost)
    
paris = trip_cost(200,20,7,200,1)
london = trip_cost(250,30,7,120,1)
dubai = trip_cost(370,15,7,80,1)
mumbai = trip_cost(450,10,7,70,1)

compare = [paris,london,dubai,mumbai]
(max(compare))
test = [1,2,3,4]

for items in zip(compare,test):
    print ("item",items)
for p,q in zip(test,compare):
    print(p)
    print(q)


# In[ ]:


cost = { 
    
    
"paris" : trip_cost(200,20,4,200,1),
"london" : trip_cost(250,30,4,120,1),
"dubai" : trip_cost(370,15,4,80,1),
"mumbai" : trip_cost(450,10,4,70,1) }

cost


# In[ ]:


marks = [80,90,56,80]
weights = [0.25,0.5,0.125,0.125]

def total(subject,weight):
    
    resultsw = 0
    for t,u in zip(subject,weight):
        resultsw += t*u
    return(resultsw)

total(marks,weights)


# In[ ]:


get_ipython().system('pip install numpy')
import numpy as np


# In[ ]:


array2array1 = np.array([10,10,10,10,10,10])
array2 = np.array([1,2,3,4,5,6])

array3 = np.array([1,1,1,1,1,1])
array4 = np.array([1,2,3,4,5,6])

dotproduct1 = np.dot(array1,array2) 
(array1*array2).max()


# In[6]:


arr1 = list(range(1000000))
arr2 = list(range(1000000,2000000))


# In[7]:


get_ipython().run_cell_magic('time', '', 'result = 0\nfor x,y in zip(arr1,arr2):\n    result += x*y\n    \nresult')


# In[8]:


get_ipython().run_cell_magic('time', '', 'np.dot(arr1,arr2)')


# In[18]:


import numpy as np
arr1_np = np.array(arr1)
arr2_np = np.array(arr2)
arr1_np
arr2_np


# In[28]:


get_ipython().run_cell_magic('time', '', '(arr1_np*arr2_np).sum()')


# In[43]:


s1 = [90,70,86,93]
s2 = [85,56,79,59]
s3 = [78,95,46,92]
s4 = [49,56,78,89]
s5 = [45,86,85,96]

w1 = [0.25,0.5,0.125,0.125]

s1_np = np.array([s1,s2,s3,s4,s5])
s1_np1 = np.dot(s1_np,w1)
s1_np1
s1_np2 = s1_np@w1
s1_np2.dtype
s1_np3 = np.matmul(s1_np,w1)
s1_np3


# In[56]:


import urllib.request

urllib.request.urlretrieve(
    'C:/Users/ramne/Downloads/climate', 
    'climates.txt')


# In[67]:


climate_data = np.genfromtxt("climate.txt", delimiter= ",", skip_header=1)
climate_data.dtype

weights= np.array([0.3,0.2,0.5])

yields = climate_data@weights
yields.shape
new_results = np.concatenate((climate_data,yields.reshape(10000,1)), axis=1)

climate_data.shape
new_results.shape


# In[136]:


lis1 = np.array([[[1,2,3],[2,5,4]],
                [[5,6,7],[1,8,6]],
                [[8,9,10],[5,7,9]]])
lis1.shape
lis2 = np.array ([[1,2,3], [1,2,1]])

lis3 = np.array([[1,3,2],[2,1,4],[2,3,1]])
lis2.shape

lis2[1,0]
lis1[0:2,0:1,0:2]


# In[143]:


EMI


# In[150]:


def CAresult(a,b,c,d,e,f,g):
    h =a+b+c+d+e+f+g
    i = a+b+c+d
    j = e+f+g

    print("Group - 1")
    if a>=60:
        print(str(a)+" E")
    
    else:
        print(a)
    
    if b>=60:
        print(str(b)+" E")
    
    else:
        print(b)
    
    if c>=60:
        print(str(c)+" E")
    
    else:
        print(c)
    
    if d>=60:
        print(str(d)+" E")
    
    else:
        print(d)
    
    
    print("Group - 2")

    if e>=60:
        print(str(e)+" E")
    
    else:
        print(e)
    
    if f>=60:
        print(str(f)+" E")
    
    else:
        print(f)
    
    if g>=60:
        print(str(g)+" E")
    
    else:
        print(g)

    print ("Toatl= {},".format(h),"Group1= {},". format(i), "Group2= {}".format(j))

    tvalue = h>=350 and a>=40 and b>=40 and c>=40 and d>=40 and e>=40 and f>=40 and g >=40

    g1value = i>=200 and a>=40 and b>=40 and c>=40 and d>=40

    g2value = j>=150 and e>=40 and f>=40 and g >=40

    if tvalue == True:
    
        print("Result = Pass")
    
    elif g1value == True:
    
        print ("Result = Group1 pass")
    
    elif g2value == True:
    
        print ("Result = Group2 pass")
    
    elif a >=60 or b>=60 or c>=60 or d>=60 or e>=60 or f>=60 or g>=60:

        print("Result = Exemption")
    
    elif  tvalue != True:
        print("Result = Fail")

CAresult(62,40,56,41,38,56,72)
    


# In[ ]:





# In[ ]:




