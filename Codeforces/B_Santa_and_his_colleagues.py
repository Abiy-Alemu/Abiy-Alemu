def func(guest,host,pile):

    dic={}
    
    for i in pile:
        temp=dic.get(i,0)
        dic[i]=temp+1
    
    for i in guest:
        temp=dic.get(i,0)
        if(temp==0):
            return False
        dic[i]=temp-1
    
    for i in host:
        temp=dic.get(i,0)
        if(temp==0):
            return False
        dic[i]=temp-1
        
    for i in dic.values():
        if(i>0):
            return False
    
    return True

guest=input()
host=input()
pile=input()  
result=func(guest,host,pile)

if(result):
    print('YES')
else:
    print('NO') 
	 	     	 			  	    							