customers = []
customers.append((2, "Harry")) #no sort needed here because 1 item. 
customers.append((3, "Charles"))
customers.sort(reverse=True) 
#Need to sort to maintain order
customers.append((1, "Riya"))
customers.sort(reverse=True) 
#Need to sort to maintain order
customers.append((4, "Stacy"))
customers.sort(reverse=True)
while customers:
     print(customers.pop(0))

print(customers)
#Will print names in the order: Stacy, Charles, Harry, Riya. 

test = []

test.append('a')
test.append('b')
test.append('c')
test.append('d')
print(test)
# test.insert('1')
# test.insert('2')
# test.insert('3')
# test.insert('4')

test.remove('a')




print(test)