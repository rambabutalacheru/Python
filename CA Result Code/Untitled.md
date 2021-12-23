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

CAresult(62,40,56,42,38,56,72)
    

