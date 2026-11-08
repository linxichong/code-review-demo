import sqlite3

from src.order_repository import find_by_reference


def lookup_order(connection: sqlite3.Connection, reference: str) -> tuple[int, dict]:
    """注文照会を応答形式へ変換する。"""
    row = find_by_reference(connection, reference)
    if row is None:
        return 404, {"error": "order_not_found"}
    return 200, {"id": row[0], "reference": row[1]}
