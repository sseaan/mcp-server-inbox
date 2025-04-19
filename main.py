from typing import Dict, Any
import os
from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import (
    ErrorData,
    INTERNAL_ERROR,
)
from inbox import Inbox, InboxException

# Initialize FastMCP server
mcp = FastMCP("inbox")

# Get environment variables
INBOX_TOKEN = os.getenv("INBOX_TOKEN")
if not INBOX_TOKEN:
    raise ValueError("INBOX_TOKEN environment variable is required")

# Initialize Inbox client
inbox_client = Inbox(INBOX_TOKEN)


@mcp.tool()
def send_note(content: str, title: str | None = None) -> Dict[str, Any]:
    """
    Send a note to the Inbox API.

    Args:
        content: Content of the note (max 3000 characters)
        title: Optional title of the note

    Returns:
        A dictionary containing the API response
    """
    try:
        return inbox_client.send_note(content, title)
    except InboxException as e:
        # Map the Inbox exception to an MCP error
        raise McpError(ErrorData(code=INTERNAL_ERROR, message=str(e)))


if __name__ == "__main__":
    mcp.run()