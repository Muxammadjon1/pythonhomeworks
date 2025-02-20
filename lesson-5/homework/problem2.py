def invest(amount, rate, years): 
     
    for i in range(1, years+1):  
        expected_value=amount*(1+rate/100)**i  #calculation 
        print(f"year {i}: {expected_value:.2f}")  #printing 
         
     
amount=float(input("Enter you initial investment in $: ")) 
rate=float(input("Enter percentage of interest rate : ")) 
years=int(input("How many years you want to keep your money in bank: ")) 
 
 
invest(amount, rate, years)  #calling the function