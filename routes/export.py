from flask import Blueprint, session, send_file
from dbcontrol.control import db
from docx_generator import CreateDocument

page = Blueprint('export', __name__)


@page.route('/')
def export():
    user_id = session.get('user_id')
    username = session.get('username')
    transactions = db.getTransactions(user_id)

    path = CreateDocument(user_id, username, transactions).save()

    return send_file(path)
