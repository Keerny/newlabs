import random
import math
print ("points") #слово после которого нужно вводить кол-во точек
a = int(input ()) #кол-во точек
k = 0.0
for i in range(a):
    x = random.random()
    y = random.random()
    k += (x * x + y * y < 1.0) #расчёт сколько точек попали в окружность
print (4 * k / a) #умножение на 4(полный круг) и деление на общее кол-во точек
print (math.pi) #ввод pi из библиотеки питона
