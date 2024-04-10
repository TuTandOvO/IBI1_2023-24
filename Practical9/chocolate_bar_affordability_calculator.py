bar_price=int(input('please enter the price of chocolate bar'))
total_money=int(input('please enter how many money do you have '))
def function(bar_price,total_money):
    number=total_money//bar_price 
    changes=total_money%bar_price
    return (number,changes)
numbers,change=function(bar_price,total_money)
print('You can buy '+ str(numbers)+'chocolate bars and remaining'+str(change))