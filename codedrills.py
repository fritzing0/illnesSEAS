#for i in range(1,50):
#    if i % 3 == 0:
#        print("DEAD")
#    elif i % 4 == 0:
#        print("BEEF")
#    elif i % 3 == 0 and i % 4 == 0:
#        print("DEADBEEF")
#
#        print (i)



#list = ["1", "2", "3", "4", "5", "7"]
#for i in range(len(list)):
#    if i % 2 == 0:
#        print (i)


#doesn't work
#int(userlist)
#def userfunction(userlist):
#    evennum = 0
#    for i in range(len(list)):
#        if (list[i]) % 2 == 0:
#            evennum = evennum + 1
#    return evennum
#
#print (userfuction())


#working one even counter of how ever many numbers you put in
#list_amount = int(input("how many mubers"))
#list = []
#for num in range (list_amount):
#    user_input = int(input ("pick number"))
#    list.append(user_input)
#counter = 0
#for num in list:
#    if num % 2 == 0:
#        counter += 1
#print("number of evens: ", counter)




#return the number of evens and put in list
while True:
    try:
        list_amount = int(input("how many numbers"))
        break
    except ValueError:
        print("That is not a number")

list = []
for num in range (list_amount):
    try:
        user_input = int(input ("pick number"))
        list.append(user_input)
    except ValueError:
        print("not a nummber")
        
counter = 0
even_list = []
for num in list:
    if num % 2 == 0:
        counter += 1
        even_list.append(num)
print("There are", counter, "even numbers")
print(even_list)
