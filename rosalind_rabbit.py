n = 96                                                                         
m = 17                                                                         
bunnies = [1, 1]                                                               
months = 2                                                                     
while months < n:                                                              
    if months < m:                                                             
        bunnies.append(bunnies[-2] + bunnies[-1])                              
    elif months == m:                                       
        bunnies.append(bunnies[-2] + bunnies[-1] - 1)                          
    else:                                                                      
        bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(m + 1)])                                                           
    months += 1   

print(bunnies[-1])