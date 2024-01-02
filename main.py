import sqlite3

db = sqlite3.connect('bank.db')

fake_bank = db.cursor()

fake_bank.execute(
    "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT, phone_number TEXT, password TEXT, "
    "balance REAL);")

fake_bank.execute(
    "CREATE TABLE IF NOT EXISTS user_transactions (id INTEGER, transactions TEXT, amount INTEGER, transaction_date "
    "REAL);")


def register_user(name, phone_number, password):
    db = sqlite3.connect("bank.db")

    fake_bank = db.cursor()

    fake_bank.execute("INSERT INTO users(name,phone_number,password,balance)VALUES(?,?,?,0.0);",
                      (name, phone_number, password,))
    db.commit()
    print(f'{name}успешно зарегистрирован')


def find_users(name, phone_number):
    db = sqlite3.connect('bank.db')

    fake_bank = db.cursor()

    result = fake_bank.execute('SELECT name,phone_number FROM users WHERE name=? and phone_number=?;', (name
                                                                                                        ,
                                                                                                        phone_number)).fetchone()
    db.commit()


def balance_add(amount, user_id):
    db = sqlite3.connect('bank.db')

    fake_bank = db.cursor()
    deposit = fake_bank.execute('UPDATE users SET balance=balance+? WHERE id=?;', (amount, user_id))

    db.commit()
    print(f'ваш баланс изменен-ваша сечашняя сумма {amount}!!')


def balance_rem(amount, user_id):
    db = sqlite3.connect('bank.db')

    fake_bank = db.cursor()
    fake_bank.execute('UPDATE users SET balance=balance-? WHERE id=?;', (amount, user_id))

    db.commit()

    print(f'ваш баланс изменен-ваша сечашняя сумма {amount}!!')


def balance_viewing(user_id):
    db = sqlite3.connect('bank.db')
    fake_bank = db.cursor()
    viewing = fake_bank.execute("SELECT balance FROM users WHERE id=?;", (user_id,)).fetchone()
    balance = viewing[0]
    print(f'ваш баланс-{balance}')























