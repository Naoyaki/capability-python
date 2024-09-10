from apps.purchase import can_purchase


def test_purchase_is_approved_when_balance_is_greater_than_price() -> None:
    # Arrange
    balance: int = 100
    price: int = 50

    # Act
    result: str = can_purchase(balance, price)

    # Assert
    assert result == "Purchase approved"


def test_purchase_is_denied_when_balance_is_less_than_price() -> None:
    # Arrange
    balance: int = 10
    price: int = 1000

    # Act
    result: str = can_purchase(balance, price)

    # Assert
    assert result == "Insufficient balance"
