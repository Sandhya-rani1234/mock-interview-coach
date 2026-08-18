\# 🎤 AI Mock Interview Coach



An AI-powered mock interview application built with \*\*Streamlit, LangChain, Gemini, and SQLite\*\*.



The application acts as an interviewer, asks one question at a time, remembers the conversation, and generates a feedback report after the interview.



\---



\## 🚀 Features



\- 🎤 AI-powered mock interviews

\- 👤 Candidate name and interview role

\- 🤖 Gemini LLM for interview questions

\- 💬 Conversational interview experience

\- 🧠 Conversation memory

\- 💾 SQLite-based interview history

\- 📊 Feedback report after interview

\- ⭐ Overall readiness score out of 10

\- 🔄 Resume previous interview session



\---



\## 🛠️ Tech Stack



\- Python

\- Streamlit

\- LangChain

\- Gemini API

\- SQLite

\- SQLAlchemy

\- python-dotenv



\---



\## 📁 Project Structure



```text

mock-interview-coach/

│

├── app.py

├── chains.py

├── prompts.py

├── memory\_store.py

├── requirements.txt

├── README.md

├── .env

│

└── data/

&#x20;   └── interview\_history.db











File Responsibilities

File	Purpose

app.py	Main Streamlit application

chains.py	Gemini LLM and LangChain chains

prompts.py	Interview and feedback prompts

memory\_store.py	SQLite conversation memory

requirements.txt	Python dependencies

.env	Gemini API key

data/interview\_history.db	Interview history database

⚙️ Prerequisites



Before running the application, make sure you have:



Python 3.11 or higher

Git

Google Gemini API key

Internet connection



Check Python:



python --version



Check Git:



git --version

📥 Installation

1\. Clone the Repository

git clone https://github.com/YOUR\_USERNAME/mock-interview-coach.git



Go to the project directory:



cd mock-interview-coach

2\. Create a Virtual Environment

python -m venv .venv



This creates a virtual environment inside the project:



mock-interview-coach/

└── .venv/

3\. Activate the Virtual Environment



For Windows PowerShell:



.venv\\Scripts\\activate



After activation, you should see something similar to:



(.venv) PS C:\\Users\\...\\mock-interview-coach>



To deactivate the environment later:



deactivate

4\. Install Dependencies



Install all required packages:



python -m pip install -r requirements.txt



Verify the installation:



python -m pip list

🔑 Gemini API Configuration



The application uses Google Gemini to generate interview questions and feedback.



Create a file named:



.env



in the project root directory.



The project should look like:



mock-interview-coach/

│

├── .env

├── app.py

├── chains.py

├── prompts.py

├── memory\_store.py

└── requirements.txt



Add your Gemini API key to .env:



GEMINI\_API\_KEY=your\_gemini\_api\_key



Example:



GEMINI\_API\_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXX



The application loads this value using python-dotenv.



🔐 Security



Never commit your .env file to GitHub.



Your .gitignore should contain:



.env

.venv/

\_\_pycache\_\_/

\*.pyc

data/



The data/ directory is ignored because it contains the SQLite interview history.



▶️ How to Run the Application



Follow these steps every time you want to run the project.



Step 1: Open PowerShell



Navigate to the project:



cd C:\\Users\\sandh\\mock-interview-coach

Step 2: Activate the Virtual Environment

.venv\\Scripts\\activate



You should see:



(.venv) PS C:\\Users\\sandh\\mock-interview-coach>

Step 3: Start Streamlit



Run:



python -m streamlit run app.py



You should see:



You can now view your Streamlit app in your browser.





Local URL: http://localhost:8501

Step 4: Open the Application



Open your browser and visit:



http://localhost:8501



You should see:



🎤 AI Mock Interview Coach

Step 5: Start an Interview



In the sidebar:



Enter your name.

Enter the role you are interviewing for.

Click Start/Resume Interview.



Example:



Name:

Sandhya





Role:

Java Backend Developer

Step 6: Answer Questions



The AI interviewer will ask one question at a time.



Enter your answer in:



Type your answer



The AI will remember the previous conversation and ask the next question.



The interview flow is:



AI Question

&#x20;    ↓

Candidate Answer

&#x20;    ↓

AI Follow-up Question

&#x20;    ↓

Candidate Answer

&#x20;    ↓

AI Follow-up Question

&#x20;    ↓

...

Step 7: End the Interview



Click:



End Interview



The application will generate a feedback report.



📊 Feedback Report



After the interview ends, Gemini evaluates the complete interview transcript.



The feedback contains:



💪 Strengths



2-3 areas where the candidate performed well.



Example:



\- Good understanding of Java fundamentals

\- Clear communication

\- Strong knowledge of Spring Boot

📈 Areas to Improve



2-3 areas where the candidate needs improvement.



Example:



\- Improve system design knowledge

\- Provide more detailed real-world examples

\- Strengthen Kafka knowledge

⭐ Readiness Score



The AI provides an overall score out of 10.



Example:



Overall Readiness Score: 7.5/10

🧠 Conversation Memory



The application uses SQLite to persist interview conversations.



The database is stored at:



data/interview\_history.db



Conversation history is associated with the candidate's session ID.



For example:



Session ID:

Sandhya



When the same session is resumed, the previous conversation can be retrieved from SQLite.



🔄 Resume an Interview



To resume an existing interview, enter the same:



Name



and:



Role



Then click:



Start/Resume Interview



The application retrieves the existing conversation history from SQLite.



🧩 Application Architecture

&#x20;                        Candidate

&#x20;                            │

&#x20;                            ↓

&#x20;                    ┌───────────────┐

&#x20;                    │  Streamlit UI │

&#x20;                    └───────┬───────┘

&#x20;                            │

&#x20;                            ↓

&#x20;                    ┌───────────────┐

&#x20;                    │    app.py     │

&#x20;                    └───────┬───────┘

&#x20;                            │

&#x20;                            ↓

&#x20;             ┌─────────────────────────────┐

&#x20;             │ RunnableWithMessageHistory │

&#x20;             └──────────────┬──────────────┘

&#x20;                            │

&#x20;                ┌───────────┴───────────┐

&#x20;                ↓                       ↓

&#x20;       ┌─────────────────┐     ┌─────────────────┐

&#x20;       │ Interview Prompt│     │ SQLite History  │

&#x20;       └────────┬────────┘     └─────────────────┘

&#x20;                │

&#x20;                ↓

&#x20;       ┌─────────────────┐

&#x20;       │  LangChain Chain│

&#x20;       └────────┬────────┘

&#x20;                │

&#x20;                ↓

&#x20;       ┌─────────────────┐

&#x20;       │  Google Gemini  │

&#x20;       └────────┬────────┘

&#x20;                │

&#x20;                ↓

&#x20;       ┌─────────────────┐

&#x20;       │Interview Question│

&#x20;       └─────────────────┘

📝 Feedback Flow

Candidate

&#x20;   │

&#x20;   ↓

End Interview

&#x20;   │

&#x20;   ↓

SQLite Conversation History

&#x20;   │

&#x20;   ↓

format\_transcript()

&#x20;   │

&#x20;   ↓

Feedback Prompt

&#x20;   │

&#x20;   ↓

LangChain

&#x20;   │

&#x20;   ↓

Google Gemini

&#x20;   │

&#x20;   ↓

Feedback Report

&#x20;   │

&#x20;   ├── Strengths

&#x20;   ├── Areas to Improve

&#x20;   └── Readiness Score

📦 Requirements



The project dependencies are stored in:



requirements.txt



Install them with:



python -m pip install -r requirements.txt

🧪 Useful Commands

Check Python Version

python --version

Check Pip

python -m pip --version

Check Streamlit

python -m streamlit --version

Run Application

python -m streamlit run app.py

Stop Application



Press:



Ctrl + C

Activate Virtual Environment

.venv\\Scripts\\activate

Deactivate Virtual Environment

deactivate

Install Dependencies

python -m pip install -r requirements.txt

🐛 Troubleshooting

Streamlit command not recognized



If you get:



streamlit : The term 'streamlit' is not recognized...



use:



python -m streamlit run app.py

ModuleNotFoundError



Example:



ModuleNotFoundError: No module named 'dotenv'



Make sure the virtual environment is activated:



.venv\\Scripts\\activate



Then install dependencies:



python -m pip install -r requirements.txt

Gemini API Key Error



If you get:



KeyError: 'GEMINI\_API\_KEY'



check that .env exists in the project root:



mock-interview-coach/

├── .env

├── app.py

├── chains.py

└── ...



The .env file should contain:



GEMINI\_API\_KEY=your\_api\_key

Gemini Model Error



If the configured Gemini model is unavailable, check the model configured in:



chains.py



For example:



llm = ChatGoogleGenerativeAI(

&#x20;   model="gemini-3.6-flash",

&#x20;   google\_api\_key=os.environ\["GEMINI\_API\_KEY"],

)

SQLite Database



The SQLite database is automatically created when the application runs.



Location:



data/interview\_history.db



You do not need to manually create the database.



📤 GitHub Commands



Check the current status:



git status



Add changes:



git add .



Commit changes:



git commit -m "Add AI mock interview coach"



Push changes:



git push



For the first push:



git push -u origin main

🔍 Verify Before Pushing



Run:



git status



Make sure .env is not listed.



You can also check:



git status --ignored



The following files should be ignored:



.env

.venv/

\_\_pycache\_\_/

\*.pyc

data/

🚫 Files That Should NOT Be Committed



Never commit:



.env

.venv/

\_\_pycache\_\_/

\*.pyc

data/interview\_history.db



The .env file contains your Gemini API key.



The SQLite database contains your interview history.



🔮 Future Improvements

🎙️ Voice-based interview

🎤 Microphone input

🗣️ Speech-to-text

🔊 Text-to-speech

⏱️ Interview timer

📄 Resume upload

📄 Resume-based interview questions

🎯 Interview difficulty levels

💻 Technical interview mode

👔 HR interview mode

📊 Candidate performance dashboard

📈 Interview analytics

🔐 User authentication

🗄️ PostgreSQL support

⚛️ React frontend

🚀 FastAPI backend

🧩 LangGraph-based persistence

👩‍💻 Author



Sandhya Rani



⭐ Project Goal



The goal of this project is to build an AI-powered interview coach that helps candidates:



Practice realistic interviews

Receive role-specific interview questions

Continue conversations with memory

Identify strengths

Identify areas for improvement

Measure interview readiness

🚀 Quick Start



For users who already cloned the repository:



cd C:\\Users\\sandh\\mock-interview-coach





python -m venv .venv





.venv\\Scripts\\activate





python -m pip install -r requirements.txt



Create .env:



GEMINI\_API\_KEY=your\_gemini\_api\_key



Then run:



python -m streamlit run app.py



Open:



http://localhost:8501



🎤 Start your mock interview!







After pasting and saving it, commit the README with:





```powershell

git add README.md

git commit -m "Add complete project README and run instructions"

git push

