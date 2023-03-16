def exchange(n) :
    n1 = n // 500
    print("500원 동전의 개수 : ", n1)
    n %= 500
    n2 = n // 100
    print("100원 동전의 개수 : ", n2)
    n %= 100
    n3 = n // 50
    print("50원 동전의 개수 : ", n3)
    n %= 50
    n4 = n // 10
    print("10원 동전의 개수 : ", n4)

def get_integer(prompt) :
    change = int(input(prompt))
    return change

n = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(n)
