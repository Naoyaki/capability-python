import pytest
from apps.actions import can_drive


@pytest.mark.parametrize(
    "age",
    [
        (17),  # 17歳: 運転できない
        (18),  # 18歳: 運転できる
    ],
)
def test_can_drive_if_age_is_18_or_above_cannot_if_below_18_actions_with_conditions(
    age: int,
) -> None:
    result = can_drive(age)

    if age < 18:  # noqa: PLR2004
        assert result is False
    else:
        assert result is True
