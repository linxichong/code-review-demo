from pathlib import Path


def receipt_message() -> str:
    """固定の注文受付メッセージを取得する。"""
    template = Path(__file__).with_name("templates") / "order_received.txt"
    return template.read_text(encoding="utf-8")
