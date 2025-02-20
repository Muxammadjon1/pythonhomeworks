def convert_far_to_cel(far): 
    """Converting Farangeit to Celcius""" 
    return (far-32)*5/9 
far=float(input("Enter a temperature in degrees F: "))  
 
cel = convert_far_to_cel(far)  
print(f"{far} degrees of F = {cel:.2f} degrees C") 
 
 
 
def convert_cel_to_far(cel): 
    """Converting celcius to farangeit""" 
    return cel*9/5 +32  
cel=float(input("Enter a temperature in degrees C: ")) 
 
far=convert_cel_to_far(cel)  
 
print(f"{cel} degrees in C = {far:.2f} degrees in F")  