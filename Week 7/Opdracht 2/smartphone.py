from termcolor import colored

samsung = float(input('What is the price of the Samsung Galaxy S22 ? '))
iphone = float(input('What is the price of the Iphone 13 ? '))

priceDiff = samsung - iphone

SamsungPriceFormat = f'€{samsung:.2f}'
IphonePriceFormat = f'€{iphone:.2f}'

if samsung > iphone:
    print(f'The Samsung Galaxy S22 is more expensive. The phone costs: {colored(SamsungPriceFormat, "red")}')
    print(f'The Iphone 13 is cheaper. The phone costs: {colored(IphonePriceFormat, 'green')}')
elif iphone > samsung:
    print(f'The Samsung Galaxy S22 is cheaper. The phone costs: {colored(SamsungPriceFormat, 'green')}')
    print(f'The Iphone 13 is more expensive. The phone costs: {colored(IphonePriceFormat, 'red')}')
else:
    print(f'Both the Iphone and the Samsung costs the same: {colored(SamsungPriceFormat, 'orange')}')

if iphone <= samsung + 50:
    print(f'The advice is to buy the Iphone 13 it costs: {colored(IphonePriceFormat, 'yellow')}')
else:
    print(f'The advice is to buy the Samsung Galaxy S22 it costs: {colored(SamsungPriceFormat, 'yellow')}')