import os

from langchain_google_genai import ChatGoogleGenerativeAI

from prompts import interview_prompt, feedback_prompt


# ---------------------------------------------------------
# Gemini LLM
# ---------------------------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.environ["GEMINI_API_KEY"],
)


# ---------------------------------------------------------
# Interview chain
# ---------------------------------------------------------

interview_chain = interview_prompt | llm


# ---------------------------------------------------------
# Feedback chain
# ---------------------------------------------------------

feedback_chain = feedback_prompt | llm