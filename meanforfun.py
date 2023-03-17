def str_to_num(list,n):
    ch = "."
    mylist = []
    type_num = False
    messylist =""
    for i in range(n):
        messylist = messylist + (list[i])
    
    if ch in messylist:
        #convert to float.
        for i in range(n):
            print(i)
            #change into float or int...
            mylist.append(float(list[i]))    
    else:
        #convert to int.
        for i in range(n):
            print(i)
            #change into float or int...
            mylist.append(int(list[i]))
        type_num = True
    
    return mylist,type_num  #if is typenum True, it converted into int
