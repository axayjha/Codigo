from math import *
m,n = input().split(' ')
m=int(m)
n=int(n)

def cbrt(x):
    if x<0:
        return -pow(abs(x), 1/3)
    else:
        return pow(x, 1/3)  



summ=0
counter =0

if m>n:
    i=m

    while i>=n:
        
        if abs( cbrt(i) - round(cbrt(i))) < 0.0000001:
            
            summ += i
            counter += 1
        i-=1    
        
            

    print("%.2f" % (summ/counter))

elif m<n:
    i=m

    while i<=n:
        if abs( cbrt(i) - round(cbrt(i))) < 0.0000001:
            
            summ += i
            counter += 1
        i+=1      
            
    print("%.2f" % (summ/counter))

else:
    if abs( cbrt(m) - round(cbrt(m))) < 0.00000001:
        print (m)
    else : print (0)    
