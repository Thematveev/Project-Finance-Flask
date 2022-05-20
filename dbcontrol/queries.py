TABLE_CREATION_QUERY = "create table if not exists accounts(id integer primary key autoincrement,username varchar(100) unique not null,password varchar(100) not null);"
REGISTER_USER_QUERY = "insert into accounts(username, password) values (?, ?)"
GET_USER_BY_NAME = "select * from accounts where username = ?"



#transactions

TRANSACTIONS_CREATION_QUERY = """create table if not exists transactions(
                                    id integer primary key autoincrement,
                                    account_id integer not null,
                                    created_at datetime not null,
                                    amount integer not null,
                                    comment varchar(50),
                                    type boolean not null
                                    );"""


TRANSACTION_ADD = """
                insert into transactions(account_id, created_at, amount, comment, type)
                values(?, datetime('now'), ?, ?, ?);
"""

GET_TRANSACTIONS_QUERY = """select * from transactions where account_id = ?"""