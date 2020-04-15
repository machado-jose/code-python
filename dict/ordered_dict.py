from collections import OrderedDict

products = OrderedDict()
for _ in range(int(input())):
    datas = input().rsplit(' ')
    price = datas.pop()
    product = ' '.join(datas).upper()
    products[product] = products.get(product, 0) + int(price)

print(*[" ".join([item, str(price)]) for item, price in products.items()], sep="\n")
