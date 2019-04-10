#Exercises
#1)
price = 300
print (price**0.5)

#2)
stock_index = 'SP500'
print (stock_index[2:])

#3)
print ('The {x} is at {y} today.'.format(x=stock_index, y=price))

#4)
stock_info = {'sp500':{'today':300, 'yesterday': 250},
    'info':['Time', [24, 7, 365]]}

print ('The yesterday price is {x}, and {y} is time.'.format(x=stock_info['sp500']['yesterday'], y=stock_info['info'][1][2]))

#5)
string = "PRICE:345.324:SOURCE--QUADL"
find_for_me = "SOURCE"

def source_finder(text, item):
    number = text.find(item)
    return text[(number+8):]

print (source_finder(string, find_for_me))

#5')
def price_finder(phrase):
    phrase = phrase.lower()
    index = phrase.find('price')

    if index < 0:
        return False
    else :
        return True

print (price_finder("What is the price?"))
print (price_finder("DUDE WHAT IS THE PRICE!!!!"))
print (price_finder("the price is 300"))

#6)
def count_price(phrase):
    phrase = phrase.lower()
    return phrase.count('price')

s = "Wow This is a string price with a lot Prices, With nice price!"
print (count_price(s))

#7)
def avg_price(priceList):
    sum = 0
    for value in priceList:
        sum += value

    return sum/len(priceList)

print (avg_price([3, 4, 5]))
