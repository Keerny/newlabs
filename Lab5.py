import random
import math
a = 1.0
k = 0.0
f = 1
while f > 0.0001: #проверка на разницу
    x = random.random()
    y = random.random()
    k += (x * x + y * y < 1.0) #расчёт сколько точек попали в окружность
    f = (math.fabs(math.pi - (4 * k / a))) #считаем разницу
    print (4 * k / a) #умножение на 4(полный круг) и деление на общее кол-во точек
    a += 1 #прибавляем к точке
print (math.pi) #ввод pi из библиотеки питона
