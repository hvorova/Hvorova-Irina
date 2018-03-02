import math
a=float(input("введите a:"))
b=float(input("введите b:"))
c=float(input("введите c:"))
print(a,'*x^2+',b,'x','+',c)
d=b*b-4*a*c
if d<0:
   print("решений нет")
else:
   x1=(-b+math.sqrt(d))/(2*a)
   x2=(-b-math.sqrt(d))/(2*a)
   print("x1=",x1)
   print("x2=",x2)
print('конец')
