locks = int(input("ใส่Locks : "))
stocks = int(input("ใส่Stocks : "))
barrels = int(input("ใส่Barrels : "))
if locks > 70 or locks < 0 or stocks > 80 or stocks < 0 or barrels > 90 or barrels < 0:
    exit()
else:    
    sales = 45 * locks + 30 * stocks + 25 * barrels
    commission = 0
    sales = (45 * locks ) + (30 * stocks) + (25 * barrels)
    if (sales <= 1000):
        commission = 0.10 * 1000
        commission = commission + 0.10 * sales 
    elif (sales <= 1800):
        commission = 0.10 * 1000
        commission = commission + 0.15 * (sales - 1000)
    else:
        commission = commission + 0.15 * 800
        commission = commission + 0.20 * (sales - 1800)
    print("sale is : ",sales,'$')
    print("commisstion is : " , commission , '$')
exit()