import math

def fn(x):
    return math.sin(x)+math.cos(x)

#метод прямоугольников
def rect_integral(f,xmin,xmax,n):
    dx=(xmax-xmin)/n
    area=0
    x=xmin
    for i in range(n):
        area+=dx*f(x)
        x+=dx
    return area

#метод трапеций
def tr_integral(f,xmin,xmax,n):
    dx=(xmax-xmin)/n
    area=0
    x=xmin
    for i in range(n):
        area+=dx*(f(x)+f(x+dx))/2
        x+=dx
    return area

#метод симпсона

# Функция для вычисления f (x)
def func( x ):
    return math.log(x)
# Функция для приближенного интеграла
def simpsons_( ll, ul, n ):
    # Расчет значения h
    h = ( ul - ll )/n
    # Список для хранения значений x и f (x)
    x = list()
    fx = list()  
    # Расчет значений x и f (x)
    i = 0
    while i<= n:
        x.append(ll + i * h)
        fx.append(func(x[i]))
        i += 1
    # Расчет результата
    res = 0
    i = 0
    while i<= n:
        if i == 0 or i == n:
            res+= fx[i]
        elif i % 2 != 0:
            res+= 4 * fx[i]
        else:
            res+= 2 * fx[i]
        i+= 1
    res = res * (h / 3)
    return res    
# Код драйвера
lower_limit = 4   # Нижний предел
upper_limit = 5.2 # Верхний предел
n = 6 #Номер интервала

print("simpson = {}".format(simpsons_(lower_limit, upper_limit, n))) 
print("rect_integral = {}".format(rect_integral(fn,0,math.pi/4,10000)))
print("tr_integral = {}".format(tr_integral(fn,0,math.pi/4,10000)))
