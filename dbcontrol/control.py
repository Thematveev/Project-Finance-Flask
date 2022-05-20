import sqlite3
from dbcontrol import queries

class DbControl:

    connection = sqlite3.connect('database.db', check_same_thread=False)
    cursor = connection.cursor()

    def __init__(self):
        self.cursor.execute(queries.TABLE_CREATION_QUERY)
        self.cursor.execute(queries.TRANSACTIONS_CREATION_QUERY)
        print("Database connected!")


    def registerNewUser(self, username, password):
        try:
            self.cursor.execute(queries.REGISTER_USER_QUERY, [username, password])
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def getUserByUsername(self, username):
        userInfo = self.cursor.execute(queries.GET_USER_BY_NAME, [username]).fetchone()
        return userInfo

    def addNewTransaction(self, amount, comment, type, id):
        self.cursor.execute(queries.TRANSACTION_ADD, [id, amount, comment, type])
        self.connection.commit()

    def getTransactions(self, id):
        r = self.cursor.execute(queries.GET_TRANSACTIONS_QUERY, [id]).fetchall()
        # print(r)
        return r


db = DbControl()

if __name__ == "__main__":
    # if not db.registerNewUser("Maksim1", "1234331"):
    #     print("Username not unique!")
    # print(db.getUserByUsername('test1'))
    db.getTransactions(1)
