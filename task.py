from flask import Flask, request, render_template

app = Flask(__name__)


def calculate_credit_score(personal_code, loan_amount, loan_period):
    credit_modifier = 1
    if loan_amount == 0:
        return 0
    if personal_code == '49002010965':
        return 0
    elif personal_code == '49002010976':
        credit_modifier = 100
    elif personal_code == '49002010987':
        credit_modifier = 300
    elif personal_code == '49002010998':
        credit_modifier = 1000
    credit_score = (credit_modifier / loan_amount) * loan_period
    return credit_score


@app.route('/')
def render():
    return render_template('index.html')


@app.route('/decision', methods=['POST'])
def make_decision():
    personal_code = request.form['personal_code']
    loan_amount = int(request.form['loan_amount'])
    loan_period = int(request.form['loan_period'])

    maximum_loan = loan_amount
    maximum_loan_period = loan_period
    previous_approved_maximum_loan = loan_amount
    credit_score = calculate_credit_score(personal_code, loan_amount, loan_period)
    if credit_score >= 1:
        while maximum_loan <= 10000 and credit_score >= 1:
            previous_approved_maximum_loan = maximum_loan
            maximum_loan += 100
            credit_score = calculate_credit_score(personal_code, maximum_loan, loan_period)
        if maximum_loan > 10000:
            maximum_loan = 10000
        if credit_score < 1:
            maximum_loan = previous_approved_maximum_loan
            credit_score = 1
    elif credit_score < 1:
        while maximum_loan >= 2100 and credit_score < 1:
            maximum_loan -= 100
            credit_score = calculate_credit_score(personal_code, maximum_loan, loan_period)
        if credit_score < 1:
            while maximum_loan_period <= 59 and credit_score < 1:
                maximum_loan_period += 1
                credit_score = calculate_credit_score(personal_code, loan_amount, maximum_loan_period)

    if credit_score < 1:
        decision = 'negative'
        maximum_loan = 0
        maximum_loan_period = 0
    else:
        decision = 'positive'
    print(personal_code)
    print(loan_amount)
    print(loan_period)
    if decision == "positive":
        return render_template('decision.html', personal_code=personal_code, maximum_loan=maximum_loan,
                               maximum_loan_period=maximum_loan_period, decision=decision)
    else:
        return render_template('negativeDecision.html', decision=decision)


if __name__ == "__main__":
    app.run()
