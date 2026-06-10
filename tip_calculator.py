price = input ('what is the total bill?')
tip = input('what percentage do you want to tio?')
price = float(price)
tip = float(tip)
print(f'you should tip ${price * (tip/100) :.2f} ')

total=(price * (tip/100) + price)
print(f'your total bill is ${total :0.2f}')