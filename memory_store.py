from pathlib import Path

from langchain_community.chat_message_histories import SQLChatMessageHistory


# ---------------------------------------------------------
# SQLite database location
# ---------------------------------------------------------

DATA_DIR = Path(__file__).parent / "data"

DB_PATH = DATA_DIR / "interview_history.db"


# Create data directory if it doesn't exist
DATA_DIR.mkdir(exist_ok=True)


# ---------------------------------------------------------
# Get interview history for a session
# ---------------------------------------------------------

def getSession_history(session_id: str):

    """
    Return the SQLite-backed chat history for a session.

    The same session_id will always connect to the same
    conversation history.
    """

    return SQLChatMessageHistory(
        session_id=session_id,
        connection=f"sqlite:///{DB_PATH.as_posix()}",
    )