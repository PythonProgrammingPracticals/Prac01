user = int(input('Number of items:'))
while (user <= 0):
    print("Invalid input")
    user = int(input('Number of items:'))

total = 0
for i in range(0,user,1):
    price = int(input('price of items:'))
    total = (price + total)
print('You have a total of:', total)

if (total > 100):
        discount = total-(total * 0.10)
print('You have a discounted total of:', discount)






