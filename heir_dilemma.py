# https://open.kattis.com/problems/heirsdilemma

user_input = input()

l = user_input.split(" ")[0] # 123864
h = user_input.split(" ")[1]

start = int(l)

array = []
while start <= int(h):                
    array.append(start)
    start += 1
    

counter = 0
for number in array:
    divisible = False

    for digit in str(number):   
        if digit in str(number).split(""):
            divisible = False
            break   
        
        if int(digit) == 0:
            divisible = False
            break   
            
        if number % int(digit) != 0:
            divisible = False
            break

        divisible = True
        
    
    if divisible == True:
        counter += 1
        

print(counter)