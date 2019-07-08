from calculation import main, main_early

if __name__ == '__main__':
    print('---------------------------------------------------------------------------------------------')
    print("Добро пожаловать в Real mortgage!")
    print('---------------------------------------------------------------------------------------------')
    total_credit = int(input("Введите сумму кредита: "))
    total_term = int(input("Введите полный срок кредита: "))
    interest_rate = float(input("Введите годовую процентную ставку: "))
    main(total_credit, total_term, interest_rate)
    print('---------------------------------------------------------------------------------------------')
    while True:
        early_pay = int(input("Введите сумму для досрочного погашения: "))
        early_month = int(input("Введите месяц внесения суммы для досрочного погашения: "))
        print('---------------------------------------------------------------------------------------------')
        main_early(total_credit, total_term, interest_rate, early_pay, early_month)