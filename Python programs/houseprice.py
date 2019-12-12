price_of_house = 1000000
buyer_credit_good = True

if buyer_credit_good:
    print ('You need a downpayment of ' + str(price_of_house * 10/100) + str(' $ '))
else:
    print ('You need a downpayment of ' + str(price_of_house * 20/100) + str(' $ '))