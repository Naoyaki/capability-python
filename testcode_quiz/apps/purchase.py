def can_purchase(balance: int, price: int) -> str:
    """ユーザーの残高を確認し、購入が可能かを判定する関数。

    :param balance: ユーザーの残高
    :param price: 購入する商品の価格
    :return: "Purchase approved" または "Insufficient balance"
    """
    if balance >= price:
        return "Purchase approved"
    return "Insufficient balance"
