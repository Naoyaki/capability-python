import pytest
from apps.actions import can_drive


def test_cannot_drive_if_under_18() -> None:
    # Arrange
    age: int = 17

    # Action
    result = can_drive(age)

    # Assert
    assert result is False


def test_can_drive_if_18_or_older() -> None:
    # Arrange
    age: int = 18

    # Action
    result = can_drive(age)

    # Assert
    assert result is True


@pytest.mark.parametrize(
    ("age", "expected"),
    [
        (17, False),
        (18, True),
    ],
)
def test_18歳以上なら運転できて_18歳未満は運転できない(
    age: int,
    expected: bool,  # noqa: FBT001
) -> None:
    result = can_drive(age)

    assert result is expected
