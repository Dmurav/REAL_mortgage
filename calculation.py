from prettytable import PrettyTable


class CalculateIpoteca:
    def __init__(self, total_credit, total_term, interest_rate):
        self.total_credit = total_credit
        self.total_term = total_term
        self.interest_rate = interest_rate

    def calculate_percent_per_month(self):
        self.percent_per_month = round(self.interest_rate / (100 * 12), 6)
        return self.percent_per_month

    def calculate_pay_per_month(self):
        a, b, c = self.total_credit, self.calculate_percent_per_month(), self.total_term
        a = float(a)
        c = float(c)
        self.pay_per_month = round(a * (b + b / ((1 + b) ** c - 1)), 2)
        return self.pay_per_month

    def calculate_total_pay(self):
        self.total_pay = round(self.calculate_pay_per_month() * self.total_term, 2)
        return self.total_pay

    def calculate_total_overpay(self):
        self.total_overpay = round(self.calculate_total_pay() - self.total_credit, 2)
        return self.total_overpay

    def calculate_table(self):
        table = PrettyTable(['Месяц', 'Сумма долга до выплат',
                             'Сумма в уплату процентов',
                             'Сумма в уплату основного долга'])
        debt_after_pay = self.total_credit
        total_result = []
        for month in range(1, self.total_term):
            pay_for_rate = debt_after_pay * self.calculate_percent_per_month()
            pay_for_total_debt = self.calculate_pay_per_month() - pay_for_rate
            total_result.append([month, '{:.2f}'.format(debt_after_pay), '{:.2f}'.format(pay_for_rate),
                                 '{:.2f}'.format(pay_for_total_debt)])
            debt_after_pay -= pay_for_total_debt

        for row in total_result:
            table.add_row(row)
        print(table)

    def calculate_table_for_web(self):
        debt_after_pay = self.total_credit
        total_result = []
        for month in range(1, self.total_term):
            pay_for_rate = debt_after_pay * self.calculate_percent_per_month()
            pay_for_total_debt = self.calculate_pay_per_month() - pay_for_rate
            total_result.append([month, debt_after_pay, pay_for_rate, pay_for_total_debt])
            debt_after_pay -= pay_for_total_debt
        return total_result

def main(total_credit, total_term, interest_rate):
    print('---------------------------------------------------------------------------------------------')
    print("Общая сумма кредита: {:.2f} руб.".format(total_credit))
    print("Общий срок кредита: {:.2f} мес.".format(total_term))
    print("Процентная ставка: {:.2f}%".format(interest_rate))
    print('---------------------------------------------------------------------------------------------')
    calc = CalculateIpoteca(total_credit, total_term, interest_rate)
    pay_per_month = round(calc.calculate_pay_per_month(), 2)
    total_pay = calc.calculate_total_pay()
    total_overpay = calc.calculate_total_overpay()
    print("Ежемесячный платёж: {:.2f} руб.".format(pay_per_month))
    print("Общая сумма выплат: {:.2f} руб.".format(total_pay))
    print("Общая переплата: {:.2f} руб.".format(total_overpay))
    print('---------------------------------------------------------------------------------------------')
    calc.calculate_table()


if __name__ == '__main__':
    total_credit = int(input("Cумма кредита: "))
    total_term = int(input("Срок кредита: "))
    interest_rate = float(input("Процентная ставка: "))
    main(total_credit, total_term, interest_rate)
