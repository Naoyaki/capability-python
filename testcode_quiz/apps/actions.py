# apps/user_actions.py

LEGAL_DRIVING_AGE: int = 18
LEGAL_DRINKING_AGE: int = 21


def can_drive(age: int) -> bool:
    """年齢に基づいて運転が許可されているかどうかを判定する。

    :param age: ユーザーの年齢
    :return: True if age >= LEGAL_DRIVING_AGE, otherwise False
    """
    return age >= LEGAL_DRIVING_AGE


def can_drink_alcohol(age: int) -> bool:
    """年齢に基づいて飲酒が許可されているかどうかを判定する。

    :param age: ユーザーの年齢
    :return: True if age >= LEGAL_DRINKING_AGE, otherwise False
    """
    return age >= LEGAL_DRINKING_AGE
