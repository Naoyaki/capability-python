from playwright.sync_api import sync_playwright  # noqa: D100, INP001


def test_create_button_navigation() -> None:
    """作成ボタンを押下し、画面遷移が正しく行われることを確認するテスト。"""
    with sync_playwright() as p:
        # ブラウザを起動
        browser = p.chromium.launch(
            headless=False,
        )  # headless=True にすると非表示で実行
        context = browser.new_context()

        # 新しいページを開く
        page = context.new_page()

        # アプリのトップページにアクセス
        page.goto("http://127.0.0.1:8000/sample_app/post/")

        # 作成ボタンを探してクリック
        page.get_by_role("link", name="作成2").click()

        # ページ遷移後のURLを確認
        assert page.url == "http://127.0.0.1:8000/sample_app/post/create/"  # noqa: S101

        # ページ内の要素を確認 (例: フォームの存在をチェック)
        assert page.locator("form").is_visible()  # noqa: S101

        # ブラウザを閉じる
        browser.close()


if __name__ == "__main__":
    test_create_button_navigation()
