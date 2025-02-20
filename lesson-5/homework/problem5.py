def is_prime(n): 
     
    if n>0: #check if number is positive 
        for i in range(2,int(n**0.5) + 1): #checking prime number 
            if n%i==0:  
                return False 
        return True #return true is if it prime 
    else: 
        print("Check if it is positive!") #if number is negative 
        
     
number=int(input("Enter number to check if it is prime number: "))     
result=is_prime(number)  #assigning 
 
print(result)