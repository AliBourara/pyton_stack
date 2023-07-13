#Countdown

def countdown(number):
    if number > 0:
        for i in range(number,-1,-1):
            print(i)
    else:
        for i in range(number,+1):
            print(i)
    return i 
print(countdown(6))

#Print and Return

def print_and_return(list):
    print(list[0])
    return list[1]

new_list = [5,2]
print(print_and_return(new_list))

#First Plus Length

def first_plus_length(list):
    return (list[0] + len(list))

num_list = [5,2,7,9,6]

x = first_plus_length(num_list)
print(x)

# Values Greater than Second

def value_greater_than_second(list):
    test_list = []
    values = 0
    if len(list) < 2 :
        return False 
    for i in range (0,len(list)):
        if list[i] > list[1]:
            values += 1
            new_list.append(list[i])
    print(values)
    return test_list

rdm_list = [9,5,1,3,7,8]
print(value_greater_than_second(rdm_list))

#This Length, That Value

def this_length_that_value(size,value):
    list = []
    for i in range(0,size):
        list.append(value)
    return list

print(this_length_that_value(8,6))