import pytest
from unittest.mock import AsyncMock, patch
from app.domain.usecases.email_sender.email_sender import EmailSender

@pytest.mark.asyncio
async def test_send(mocker):
    # Arrange
    mock_logging = mocker.patch(
        "app.domain.usecases.email_sender.email_sender.logging", autospec=True,
    )
    mock_sleep = mocker.patch(
        "app.domain.usecases.email_sender.email_sender.sleep", new_callable=AsyncMock,
    )
    sender = EmailSender()
    recipient = "test@example.com"
    subject = "test subject"
    body = "test body"

    # Act
    await sender.send(recipient, subject, body)

    # Assert
    mock_sleep.assert_called_once()
    mock_logging.info.assert_any_call(
        f"Sending email to {recipient} with subject {subject} and body {body}"
    )
    mock_logging.info.assert_any_call(
        f"Email sent to {recipient} with subject {subject} and body {body}"
    )
