import statistics 
universities = [ 
    ['California Institute of Technology', 2175, 37704], 
    ['Harvard', 19627, 39849], 
    ['Massachusetts Institute of Technology', 10566, 40732], 
    ['Princeton', 7802, 37000], 
    ['Rice', 5879, 35551], 
    ['Stanford', 19535, 40569], 
    ['Yale', 11701, 40500] 
] 
 
def enrollment_stats(universities):  
      total_students=sum(university[1] for university in universities) #summing data by indexing 
      total_tuition=sum(university[2] for university in universities)   
       
       
      return total_students, total_tuition #return  
 
 
enrollment_stats(universities) #calling funtion 
 
def mean(universities): 
      mean_value_students=sum(university[1] for university in universities)/len(universities) #finding mean by indecies 
      mean_value_tuition=sum(university[2] for university in universities)/len(universities) 
      return mean_value_students, mean_value_tuition 
 
 
mean(universities) #callig funtion 
 
 
 
 
def median(universities): 
    students_list = sorted(university[1] for university in universities) 
    tuition_list = sorted(university[2] for university in universities) #finding median by import statistics and indicies 
    n = len(students_list) 
 
    if n % 2 == 1:  # Odd length 
        median_students = students_list[n // 2] 
        median_tuition = tuition_list[n // 2]         #considering number of universities 
    else:  # Even length 
        median_students = (students_list[n // 2 - 1] + students_list[n // 2]) / 2 
        median_tuition = (tuition_list[n // 2 - 1] + tuition_list[n // 2]) / 2 
 
    return median_students, median_tuition 
median(universities) 
 
total_students, total_tuition = enrollment_stats(universities) #assigning  
mean_students, mean_tuition = mean(universities)#assigning  
median_students, median_tuition = median(universities)#assigning  
print("*"*50) 
print(f"Total students : {total_students}") 
print(f"Total tuition : {total_tuition}\n") #printing 
 
print(f"Student mean: {mean_students}") 
print(f"Student median: {median_students}\n") 
 
print(f"Tuition mean: {mean_tuition}") 
print(f"Tuition median: {median_tuition}\n") 
print("*"*50)