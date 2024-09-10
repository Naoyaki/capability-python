from apps.task_manager import TaskManager


def test_execute() -> None:
    manager = TaskManager()

    result = manager.execute()

    assert result == "Main task executed"
