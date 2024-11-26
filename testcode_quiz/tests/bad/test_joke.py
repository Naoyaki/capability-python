import os
from pathlib import Path


def test_product_code_file_content() -> None:
    expected = """class SampleClass:
    def greet(self) -> str:
        \"\"\"挨拶\"\"\"
        return "Hello, World!"
"""
    os.chdir(Path(__file__).resolve().parent.parent.parent)

    # ファイルを開いて実際の内容を取得
    with Path("apps/joke.py").open("r", encoding="utf-8") as f:
        file_content = f.read()

    assert file_content == expected, "プロダクトコードの内容が一致しません。"
