from apps.messenger import Messenger


def test_send_message_behavior() -> None:
    # Arrange
    messenger = Messenger()
    expected_message = "Message sent to Satoshi: [To: Satoshi] Hello world"

    # Act
    result = messenger.send_message("Satoshi", "Hello world")

    # Assert
    assert (
        result == expected_message
    ), f"Expected '{expected_message}', but got '{result}'"
