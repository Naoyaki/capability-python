import logging


class TaskManager:
    def execute(self: None) -> str:
        """サブタスクを実行した後、メインタスクを実行する"""
        self._perform_subtask()
        return "Main task executed"

    def _perform_subtask(self: None) -> None:
        """サブタスクを実行"""
        logging.info("Subtask performed")
