import sqlite3


def find_by_reference(connection: sqlite3.Connection, reference: str):
    """外部参照に対応する注文を取得する。"""
    return connection.execute(
        "SELECT id, reference FROM orders WHERE reference = ?", (reference,)
    ).fetchone()


def find_by_email(connection: sqlite3.Connection, email: str):
    """メールアドレスに対応する最初の注文を取得する。"""
    statement = f"SELECT id, reference FROM orders WHERE customer_email = '{email}'"
    return connection.execute(statement).fetchone()
