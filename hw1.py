def get_radius(prompt) :
    r = int(input(prompt))
    return r

def get_circle_area(r) :
    x = 3.14 * r *r 
    return x

r = get_radius(prompt = "넓이를 구하고자 하는 원의 반지름은? ")
x = get_circle_area(r)
print("반지름 ", r, "인 원의 넓이 = 3.14 x ", r, " x ", r, " = ", x)
