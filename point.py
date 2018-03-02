print("Введите координаты центра круга:")
Хц=float(input("X:"))
Yц=float(input("Y:"))
r=float(input("Радиус:"))
print("Введите координаты точки:")
x=float(input("х:"))
y=float(input("y:"))
if ((x-Хц)*(x-Хц)+(y-Yц)*(y-Yц))<r*r:
    print ("Точка попала в круг!")
else:
    print("Точка не попала в круг!")
print ("Конец")
