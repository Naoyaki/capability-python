from apps.actions import can_drive


def test_cannot_drive_if_under_18() -> None:
    age: int = 17

    result = can_drive(age)

    assert result is False


def test_can_drive_if_18_or_older() -> None:
    age: int = 18

    result = can_drive(age)

    assert result is True
