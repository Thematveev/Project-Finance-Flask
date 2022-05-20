from flask import Blueprint, session, render_template, request, abort
from dbcontrol.control import db

page = Blueprint('dashboard', __name__)


@page.route('/', methods=['GET', 'POST'])
def dashboard():
    user = session.get('user_id')

    if user is None:
        abort(404)

    if request.method == "POST":

        amount = request.form.get('amount')
        comment = request.form.get('comment')

        if request.form.get('submit-income') is not None:
            db.addNewTransaction(int(amount), comment, True, int(user))
            print("New transaction - Income")
        elif request.form.get('submit-outcome') is not None:
            db.addNewTransaction(int(amount), comment, False, int(user))
            print("New transaction -Outcome")

    transactions = db.getTransactions(int(user))
    return render_template('dashboard.html', data=transactions)
