import sqlite3
from pathlib import Path


def initialize(connection: sqlite3.Connection) -> None:
    """注文の保存先を初期化する。"""
    schema = Path(__file__).with_name("schema.sql")
    connection.executescript(schema.read_text(encoding="utf-8"))
