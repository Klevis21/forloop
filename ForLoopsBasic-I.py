#Basic
for x in range(0,151):
    print(x)
#Multiples of Five
multiples=[] 
for i in range(5, 1001): 
    if i%5==0: 
        multiples.append(i) 
print(multiples) 
#Counting, the Dojo Way
def printDojoWay(maxNumber):
    for number in range(0,maxNumber+1,1):
        if number % 10==0:
            print('Coding Dojo')
        elif number %5==0:
            print('Coding')
        else:
            print(number)
printDojoWay(100)
#Whoa. That Sucker's Huge
sum=0
for i in range(0,500001,1):
    if i%2!=0:
     sum= i + sum

print(sum)
#Countdown by Fours
def count_down_four():
    number = 2018
    while number > 0:
        print (number)
        number = number - 4
        
count_down_four()
#Flexible Counter
def flex_countdown(low, high, mult):
    for i in range (low, high):
        if i % mult == 0:
            print (i)
            
flex_countdown(2, 9, 3)