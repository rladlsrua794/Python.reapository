def get_fixed_price(p, n) :
    n = (100 - n) / 100
    p = p / n
    p = int(p)
    return p

n = int(input('활인륭은? '))
p1 = int(input('A 상품의 활인된 가격은? '))
p2 = int(input('B 상품의 활인된 가격은? '))
p3 = get_fixed_price(p1, n)
p4 = get_fixed_price(p2, n)
print('A 상품의 정가는 ', p3, '원')
print('B 상품의 정가는 ', p4, '원')
