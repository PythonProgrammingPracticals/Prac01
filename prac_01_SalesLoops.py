
sales = float(input('Hello! Please input your amount:'))
while(sales >= 0):

    if (sales < 1000):
        bonus = (sales * 0.10)
        print(bonus)

    elif (sales >= 1000):
        bonus = (sales * 0.15)
        print(bonus)

    print('Congratulations! You have a bonus of:', bonus)
    sales = float(input('Hello! Please input your amount:'))





