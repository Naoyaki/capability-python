from unittest.mock import patch

from apps.task_manager import TaskManager


def test_execute() -> None:
    manager = TaskManager()

    # 内部メソッド _perform_subtask が呼ばれることを確認する
    with patch.object(manager, "_perform_subtask") as mock_subtask:
        result = manager.execute()

        mock_subtask.assert_called_once()

    assert result == "Main task executed"
