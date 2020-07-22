products = [] #二维清单
while True:
	name = input('Please input the name of product: ')
	if name == 'q':
		break
	price = input('Please input the price of this product: ')
	attribute = []
	attribute = [name, price]
	# attribute.append(name)
	# attribute.append(price)
	products.append(attribute)

print(products)

for p in products:
	print(p[0], '的价格为: ', p[1])

