def function(bar_price,total_money):
    number=total_money//bar_price 
    changes=total_money%bar_price
    return ('You can buy '+ str(number)+' chocolate bars and remaining '+str(changes))

# Examples
print(function(bar_price=10,total_money=100))
# output: You can buy 10 chocolate bars and remaining 0
