import account
def main():
    rate = int(input('Vvedite stavky:'))
    money = int(input('Vvedite summy:'))
    period = int(input('Vvedite period:'))
    result = rt.calculate_income(rate,period,money)
    print ("Parametri scheta:\n", "Summ",money, "\n", "Stavki", rate, "\n", "Period", period, "\n", "Obsh sum", result, "\n")
if __name__=="__main__":
    main()
