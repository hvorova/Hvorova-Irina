eur = 70
dol = 60
uah = 2
money = int(input('Vvedite summy: '))
currency = int(input('dollar - 400, euro - 401, uah - 402, \n'))
if currency == 400:
   cash = round (money*dol,2)
   print ('Valuta USA:' , cash )
elif currency == 401:
     cash = round (money*eur,2)
     print ('Valuta euro: ',cash)
elif currency == 402:
    cash = round(money*uah, 2)
    print('Valuta uah: ',cash)
else:
    cash = 0
    print ('Neizvestno')
print("Na ruki", cash)
