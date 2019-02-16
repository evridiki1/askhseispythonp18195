def maxDistance(L,y):
    ar=[]
    
    s=0
    max=0
    s1=0
    
    for x in L:
        
        s=s+int(x)
        
        if s>max:
            max=s
            s1=s1+max
            ar.append(max)
            
  
    if s>int(y):
        s=0
    
        
       
    print(s)








            
        
input_string=input("Enter a list element separated by space")
list=input_string.split()
print("Calculating sum of element of input list")
k=input("Δωσε εναν θετικο ακέραιο")
var=int(k)
maxDistance(list,k)
    
    
