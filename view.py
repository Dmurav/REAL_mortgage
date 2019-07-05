from flask import Flask, render_template, request, g, \
    flash, redirect, url_for
import _config
from calculation import CalculateIpoteca

app = Flask(__name__)
app.config.from_object(_config)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    total_credit = float(request.form['total_credit'])
    total_term = int(request.form['total_term'])
    interest_rate = float(request.form['interest_rate'])
    c = CalculateIpoteca(total_credit, total_term, interest_rate)
    t_pay = c.calculate_total_pay()
    t_overpay = c.calculate_total_overpay()
    pay_month = c.calculate_pay_per_month()
    table = c.calculate_table_for_web()
    return render_template('result.html',
                           t_pay=t_pay,
                           t_overpay=t_overpay,
                           pay_month=pay_month,
                           table=table)