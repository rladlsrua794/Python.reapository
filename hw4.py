def rep_char(c) :
    n = c * 1 + 1
    return n

def draw_line_string(n, s1, s2) :  
    print('-' * n)
    print(f'{s1},')
    print(f'{s2}')
    print('-' * n)
    
msg1 = input('Input his/her name: ')
msg2 = 'Welcome to Seoul.'
nstr = len(msg1)if (len(msg1) > len(msg2))else len(msg2)
num = rep_char(nstr)
draw_line_string(num, msg1, msg2)
