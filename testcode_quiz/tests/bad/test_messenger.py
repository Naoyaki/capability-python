from apps.messenger import Messenger
from pytest_mock import MockerFixture


def test_send_message_behavior(mocker: MockerFixture) -> None:
    messenger = Messenger()

    # _prepare_message の呼び出しをモックする
    mock_method = mocker.patch.object(
        Messenger,
        "_prepare_message",
        wraps=messenger._prepare_message,  # noqa: SLF001
    )

    # メインのメソッドを実行
    result = messenger.send_message("Satoshi", "Hello world")

    # _prepare_message が呼び出されたことを確認
    mock_method.assert_called_once_with("Satoshi", "Hello world")

    # 最終的な結果を検証
    expected_message = "Message sent to Satoshi: [To: Satoshi] Hello world"
    assert (
        result == expected_message
    ), f"Expected '{expected_message}', but got '{result}'"
