import math
print("Введите коэффициенты a,b и с уравнения: ax^2+bx+c")
a=float(input("введите a:"))
b=float(input("введите b:"))
c=float(input("введите c:"))
if a>0:
   print("у=",a,'*x^2+',b,'x','+',c)
else:
   if a==0:
      print("Уравнение: у=",b,'x','+',c,"не является квадратным")
    
d=b*b-4*a*c
if d==b*b:
    print("проверьте значения")
else:
   if d<0:
      print("решений нет")
   else:
       if d==0:
          x1=(-b+math.sqrt(d))/(2*a)
          print("d=",d)
          print("x1=x2=",x1)
       else:
          x1=(-b+math.sqrt(d))/(2*a)
          x2=(-b-math.sqrt(d))/(2*a)
          print("d=",d)
          print("Ответ:")
          print("x1=",x1)
          print("x2=",x2)
   
print('конец')
