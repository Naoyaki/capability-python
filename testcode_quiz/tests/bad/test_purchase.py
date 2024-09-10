from apps.purchase import can_purchase


def test_can_purchase() -> None:
    assert can_purchase(100, 50) == "Purchase approved"
    assert can_purchase(10, 1000) == "Insufficient balance"
