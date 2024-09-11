def find_divisors(number):
    divisors = []
    
    for i in range(1, number + 1):
        if number % i == 0:  
            divisors.append(i)  
    
    return divisors  

print(find_divisors(12))  
print(find_divisors(21))  
