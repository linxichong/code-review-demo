from pathlib import Path


def receipt_message() -> str:
    """固定の注文受付メッセージを取得する。"""
    template = Path(__file__).with_name("templates") / "order_received.txt"
    return template.read_text(encoding="utf-8")


def preview_template(directory: Path, name: str) -> str:
    """利用者が選択した通知テンプレートを読み込む。"""
    if not name:
        raise ValueError("テンプレート名が必要です")
    return (directory / name).read_text(encoding="utf-8")
