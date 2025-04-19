import requests
from typing import Dict, Any


class InboxException(Exception):
    """Custom exception for Inbox API errors"""
    pass


class Inbox:
    def __init__(self, inbox_token):
        """
        Initialize an Inbox client.

        Args:
            inbox_token: The token for authentication with the Inbox API
        """
        self.inbox_token = inbox_token
        self.api_url = f"https://inbox.gudong.site/api/inbox/{self.inbox_token}"
        self.headers = {
            "Content-Type": "application/json",
        }

    def send_note(self, content: str, title: str | None = None) -> Dict[str, Any]:
        """
        Send a note to the Inbox API.

        Args:
            content: Content of the note (max 3000 characters)
            title: Optional title of the note

        Returns:
            Dict: The response from the API

        Raises:
            InboxException: If there is an error sending the note
        """
        if len(content) > 3000:
            raise InboxException("Note content exceeds maximum length of 3000 characters")

        try:
            payload = {"content": content}
            if title is not None:
                payload["title"] = title
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise InboxException(f"Error sending note to Inbox: {str(e)}")