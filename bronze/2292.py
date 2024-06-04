n = int(input())

if n == 1:
    print(1)
else:
    layer = 1  
    cnt = 1 
    
    while cnt < n:
        cnt += 6 * layer  
        layer += 1
    
    print(layer)
 
 