#Basic 

"""
for i in range(0,151):
    print(i)
"""

#Multiples of 5

"""
for i in range (5,1001,5):
    print(i)
"""
#Counting,the dojo way
"""
for i in range(0,101):
    if i%10 == 0:
        print("coding dojo")
    elif i%5 == 0:
        print("coding")
    else :
        print(i)
"""

#whoa ,that sucker's huge

"""
sum = 0
for i in range(0,500000):
    if i%2 == 1 :
        sum += i
print(sum)        
"""

#Countdown by fours

"""
for i in range(2018,0,-4):
    print(i)
"""

#flexible counter

"""
def multiples(lownum,highnum,mult):
    for i in range(lownum,highnum+1):
        if i%mult ==0:
            print(i)
    return None

multiples(2,17,5)
"""
