def factor(n): #argument 
     
    if n>0:  #checking if it positive 
        for i in range(1, n+1): 
            if n%i==0: #finding factors 
                print(f"{i} is a factor of {n}") 
 
    else:  
        print("Please,  make sure you have entered positve number!") #saying if number is negative  
n=int(input("Enter a positive number: ")) 
factor(n) #calling function