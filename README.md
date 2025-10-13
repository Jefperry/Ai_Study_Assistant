# Ai_Study_Assistant
Smart Note Summarizer & Flashcard Generator for Students
 Overview

AI Study Assistant is a modern web application that helps students quickly summarize their study notes and automatically generate flashcards using AI models from Hugging Face.

Users can:

Paste text notes 

Generate concise summaries 

Create smart flashcards for studying 

Save their work securely under their accounts 

 Tech Stack
Layer	Technology	Description
Frontend	HTML, TailwindCSS, JavaScript	Modern, responsive UI
Backend	Python (Flask)	REST API for auth & AI endpoints
Database	MySQL	Stores users and summaries
AI Engine	Hugging Face Transformers (T5 or BART)	Performs text summarization
Auth	JWT (Flask-JWT-Extended)	Secure user login & token handling
 Project Structure
ai_study_assistant/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── prompt_templates.py
│   ├── requirements.txt
│   ├── .env
│   └── routes/
│       ├── __init__.py
│       ├── auth_routes.py
│       └── ai_routes.py
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── js/
│   │   ├── api.js
│   │   ├── auth.js
│   │   └── generate.js
│   ├── css/
│   │   └── styles.css
│   └── README.md
│
└── README.md

 Backend Setup Guide
1️ Clone the repository
git clone https://github.com/<your-username>/ai-study-assistant.git
cd ai-study-assistant/backend

2️ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate    # On Windows
# or
source venv/bin/activate # On macOS/Linux

3️ Install dependencies
pip install -r requirements.txt

4️ Configure environment variables

Create a .env file in the backend folder:

SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
DATABASE_URL=mysql+pymysql://root:password@localhost/ai_study_assistant

5️ Initialize the database

Open Python shell:

python
>>> from app import create_app, db
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
>>> exit()

6️ Run the backend server
python app.py


Server will start on http://127.0.0.1:5000

 Frontend Setup Guide
1️ Go to frontend folder
cd ../frontend

2️ Open index.html in your browser

You can use a local live server (VS Code extension or Python) to serve it:

python -m http.server 8080


Frontend will be available at http://localhost:8080

 How It Works

Register/Login → Each student has their own account.

Paste Notes → Paste text notes in the main dashboard.

Generate Summary → AI (Hugging Face) summarizes the notes.

View Flashcards → AI creates flashcards from the summary.

Save Results → The app saves summaries and flashcards under the user profile.

 API Endpoints
Endpoint	Method	Description
/api/auth/register	POST	Register new user
/api/auth/login	POST	Login and receive JWT token
/api/generate	POST	Generate summary and flashcards (requires JWT)
📦 Example Request
POST /api/generate

Headers:

Authorization: Bearer <token>
Content-Type: application/json


Body:

{
  "title": "Machine Learning Notes",
  "text": "Machine learning is a branch of AI that enables systems to learn from data..."
}


Response:

{
  "summary": "Machine learning enables systems to learn from data...",
  "flashcards": [
    {"question": "What is key point 1?", "answer": "..."},
    {"question": "What is key point 2?", "answer": "..."}
  ]
}

 Deployment Options
Type	Platform	Cost	Description
Local Deployment	Run Flask + HTML locally	✅ Free	Best for testing & school projects
Cloud Deployment	Render / Railway / Vercel	⚠️ Some free tiers	Simple 1-click deployment
Database Hosting	Local MySQL or Planetscale	✅ Free options	Planetscale recommended for small apps

 For free MVP: deploy backend on Render, frontend on Vercel, and use Planetscale for MySQL.

 Next Steps (Recommended Improvements)
Feature	Description
View Saved Summaries	Add dashboard to list all user summaries
Flashcard Quiz Mode	Interactive Q&A quiz from flashcards
Advanced AI Model	Upgrade to facebook/bart-large-cnn for better quality
Theme Switch	Light/Dark mode toggle
Export Options	Download summaries as PDF or TXT
 Author

Jef Perry
2nd Year Computer Programming Student
AI Study Assistant Project — 2025
