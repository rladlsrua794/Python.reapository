def read_single_digit(n) :
    if n == 1 :
        n = '일 '
    elif n == 2 :
        n = '이 '
    elif n == 3 :
        n = '삼 '
    elif n == 4 :
        n = '사 '
    elif n == 5 :
        n = '오 '
    elif n == 6 :
        n = '육 '
    elif n == 7 :
        n = '칠 '
    elif n == 8 :
        n = '팔 '
    elif n == 9 :
        n = '구 '
    else :
        n = '영 '
    return n

def read_number(n) :
    n1 = n // 100
    if n1 > 0 :
        n1 = read_single_digit(n1)
    else :
        n1 = ''
    n %= 100
    n2 = n // 10
    if n2 > 0 :
        n2 = read_single_digit(n2)
    else :
        n2 = ''
    n %= 10
    n3 = n
    n3 = read_single_digit(n3)
    n = n1 + n2 + n3
    return n

num = int(input('세 자리 정수 입력 : '))
num = read_number(num)
print(num)
