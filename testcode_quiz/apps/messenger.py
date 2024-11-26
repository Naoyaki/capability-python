class Messenger:
    def send_message(self, user: str, message: str) -> str:
        """メッセージを送信する。"""
        prepared_message = self._prepare_message(user, message)
        return f"Message sent to {user}: {prepared_message}"

    def _prepare_message(self, user: str, message: str) -> str:
        # メッセージ内容を加工
        return f"[To: {user}] {message.capitalize()}"
