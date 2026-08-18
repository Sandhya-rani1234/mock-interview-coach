import streamlit as st

from dotenv import load_dotenv

# Load .env before importing chains
load_dotenv()

from langchain_core.runnables.history import RunnableWithMessageHistory

from chains import interview_chain, feedback_chain
from memory_store import getSession_history


# ---------------------------------------------------------
# Add memory to interview chain
# ---------------------------------------------------------

interview_with_memory = RunnableWithMessageHistory(
    interview_chain,
    getSession_history,
    input_messages_key="input",
    history_messages_key="history",
)


# ---------------------------------------------------------
# Format transcript
# ---------------------------------------------------------

def format_transcript(session_id: str):

    history = getSession_history(session_id)

    lines = []

    for msg in history.messages:

        speaker = (
            "interviewer"
            if msg.type == "ai"
            else "candidate"
        )

        lines.append(
            f"{speaker}: {msg.content}"
        )

    return "\n".join(lines)


# ---------------------------------------------------------
# Streamlit configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Mock Interview Coach",
    page_icon="🎤"
)

st.title("🎤 AI Mock Interview Coach")


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    name = st.text_input(
        "Your name (this is your session id)"
    )

    role = st.text_input(
        "Role you are interviewing for",
        placeholder="e.g. Backend developer"
    )

    start_clicked = st.button(
        "Start/Resume Interview"
    )


# ---------------------------------------------------------
# Streamlit session state
# ---------------------------------------------------------

if "started" not in st.session_state:

    st.session_state.started = False


if "interview_ended" not in st.session_state:

    st.session_state.interview_ended = False


# ---------------------------------------------------------
# Start / Resume interview
# ---------------------------------------------------------

if start_clicked and name and role:

    st.session_state.started = True
    st.session_state.interview_ended = False


# ---------------------------------------------------------
# Don't continue until interview starts
# ---------------------------------------------------------

if not st.session_state.started:

    st.info(
        "Please enter your name and the role you are "
        "interviewing for, then click "
        "'Start/Resume Interview' to begin."
    )

    st.stop()


# ---------------------------------------------------------
# LangChain session configuration
# ---------------------------------------------------------

config = {
    "configurable": {
        "session_id": name
    }
}


# ---------------------------------------------------------
# Get conversation history
# ---------------------------------------------------------

history = getSession_history(name)


# ---------------------------------------------------------
# Start new interview
# ---------------------------------------------------------

if len(history.messages) == 0:

    with st.spinner("Starting interview..."):

        interview_with_memory.invoke(
            {
                "role": role,
                "input": "Start the interview."
            },
            config=config
        )


# ---------------------------------------------------------
# Display saved conversation
# ---------------------------------------------------------

for msg in getSession_history(name).messages:

    with st.chat_message(
        "assistant"
        if msg.type == "ai"
        else "user"
    ):

        st.write(msg.content)


# ---------------------------------------------------------
# Interview is still running
# ---------------------------------------------------------

if not st.session_state.interview_ended:

    answer = st.chat_input(
        "Type your answer"
    )

    if answer:

        with st.spinner("Thinking..."):

            interview_with_memory.invoke(
                {
                    "role": role,
                    "input": answer
                },
                config=config
            )

        st.rerun()


    # End Interview button
    if st.button("End Interview"):

        st.session_state.interview_ended = True

        st.rerun()


# ---------------------------------------------------------
# Interview ended → Generate feedback
# ---------------------------------------------------------

else:

    st.subheader("📊 Feedback Report")

    with st.spinner("Generating feedback..."):

        transcript = format_transcript(name)

        report = feedback_chain.invoke(
            {
                "role": role,
                "transcript": transcript
            }
        )

    # Gemini returns an AIMessage
    st.write(report.content)