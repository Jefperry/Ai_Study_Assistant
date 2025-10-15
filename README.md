# AI Study Assistant

Smart Note Summarizer & Flashcard Generator for Students

## 📋 Overview

AI Study Assistant is a modern web application that helps students quickly summarize their study notes and automatically generate flashcards using optimized AI models from Hugging Face.

**Key Features:**

- Paste text notes (up to 10,000 characters)
- Generate AI-powered concise summaries
- Create smart flashcards using rule-based extraction
- Save and manage study materials securely
- Export summaries and flashcards
- Interactive quiz mode for studying

## 🛠️ Tech Stack

| Layer      | Technology                                      | Description                                          |
| ---------- | ----------------------------------------------- | ---------------------------------------------------- |
| Frontend   | HTML5, CSS3, Vanilla JavaScript                 | Modern, responsive UI with no framework dependencies |
| Backend    | Python (Flask)                                  | REST API for authentication & AI processing          |
| Database   | MySQL                                           | Stores users, summaries, and flashcards              |
| AI Engine  | HuggingFace Transformers (google/flan-t5-small) | Optimized text summarization (~500MB memory)         |
| Auth       | JWT (Flask-JWT-Extended)                        | Secure user login & token handling                   |
| Flashcards | Rule-based Heuristics                           | Fast key term and definition extraction              |

## 📁 Project Structure

```
ai-study-assistant/
├── backend/
│   ├── app.py                     # Main Flask application
│   ├── config.py                  # Environment configuration
│   ├── models.py                  # Database models (User, Summary)
│   ├── requirements.txt           # Python dependencies
│   ├── .env.example              # Environment variables template
│   ├── routes/
│   │   ├── auth_routes.py        # Authentication endpoints
│   │   └── ai_routes.py          # AI processing endpoints
│   ├── services/
│   │   ├── ai_client.py          # Main AI orchestrator
│   │   ├── summarizer_hf.py      # HuggingFace summarization
│   │   └── flashcard_generator.py # Rule-based flashcard creation
│   └── templates/
│       └── prompt_templates.py   # AI prompt templates
├── frontend/
│   ├── index.html                # Main dashboard
│   ├── login.html               # User authentication
│   ├── register.html            # User registration
│   ├── history.html             # Saved summaries management
│   ├── result.html              # Summary and flashcard display
│   ├── css/
│   │   └── styles.css          # Application styling
│   └── js/
│       ├── api.js              # API communication utilities
│       ├── auth.js             # Authentication logic
│       ├── generate.js         # Summary generation
│       └── history.js          # History management
├── sql/
│   └── schema.sql              # Database schema
└── README.md
```

## 🚀 Setup Guide

### Backend Setup

1️⃣ **Clone and navigate to project**

```bash
git clone https://github.com/<jefperry>/ai-study-assistant.git
cd ai-study-assistant/backend
```

2️⃣ **Create and activate virtual environment**

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# or
source venv/bin/activate # macOS/Linux
```

3️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Configure environment variables**
Create a `.env` file in the backend folder:

```env
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-here
DB_USER=root
DB_PASSWORD=your-password
DB_HOST=localhost
DB_NAME=ai_study_assistant
TEXT_MAX_LENGTH=10000
AI_MODEL_NAME=google/flan-t5-small
AI_MODEL_CACHE_DIR=./models_cache
```

5️⃣ **Initialize the database**

```bash
# Run the SQL schema first
mysql -u root -p < ../sql/schema.sql

# Then create tables with Flask
python
>>> from app import create_app, db
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
>>> exit()
```

6️⃣ **Start the backend server**

```bash
python app.py
```

Server will start on `http://127.0.0.1:5000`

### ⚡ First Run Note

The HuggingFace model (~500MB) will download automatically on first use. This may take 2-5 minutes depending on your internet connection.

Frontend Setup Guide
1️ Go to frontend folder
cd ../frontend

2️ Open index.html in your browser

You can use a local live server (VS Code extension or Python) to serve it:

python -m http.server 8080

Frontend will be available at http://localhost:8080

## 🔄 How It Works

1. **Register/Login** → Secure JWT-based authentication for each student
2. **Paste Notes** → Add text content (up to 10,000 characters) in the dashboard
3. **AI Processing** → google/flan-t5-small generates concise summaries
4. **Smart Flashcards** → Rule-based extraction creates Q&A pairs from key terms
5. **Save & Manage** → All content saved to user profile with full CRUD operations
6. **Study Tools** → Interactive quiz mode and export functionality

## 🎯 Key Features

### ✅ **Current Features**

- **Multi-user authentication** with secure JWT tokens
- **AI-powered summarization** using optimized HuggingFace models
- **Smart flashcard generation** with rule-based heuristics
- **Text input validation** (10,000 character limit)
- **Data persistence** with MySQL database
- **Responsive web interface** with modern CSS
- **Memory-optimized deployment** (~500MB model footprint)

### 🚧 **Planned Features** (See workload.txt)

- **Summary history management** with search and pagination
- **Export functionality** (PDF, TXT, JSON formats)
- **Interactive quiz mode** for flashcard studying
- **Bulk operations** and advanced study tools

API Endpoints
Endpoint Method Description
/api/auth/register POST Register new user
/api/auth/login POST Login and receive JWT token
/api/generate POST Generate summary and flashcards (requires JWT)
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

## 🌐 Deployment Options

| Type                  | Platform                    | Memory | Cost                   | Description                       |
| --------------------- | --------------------------- | ------ | ---------------------- | --------------------------------- |
| **Local Development** | Run Flask + HTML locally    | 1GB    | ✅ Free                | Best for development & testing    |
| **Cloud Deployment**  | Railway / Render            | 1GB    | ⚠️ Free tier available | Memory-optimized for small models |
| **Database Hosting**  | PlanetScale / Railway MySQL | -      | ✅ Free tier           | Managed MySQL with scaling        |
| **Alternative**       | Heroku Performance          | 2.5GB  | 💰 Paid                | For larger models if needed       |

### 🎯 **Recommended Free Deployment Stack**

- **Backend**: Railway or Render (1GB memory sufficient for flan-t5-small)
- **Database**: PlanetScale MySQL (generous free tier)
- **Frontend**: Vercel or Netlify (static hosting)

### ⚡ **Performance Requirements**

- **Memory**: 500MB for AI model + 500MB for application = 1GB total
- **CPU**: 1-2 cores sufficient for small scale (10-50 concurrent users)
- **Storage**: 2GB (model cache + database)
- **Network**: Moderate bandwidth for model downloads during deployment

Next Steps (Recommended Improvements)
Feature Description
View Saved Summaries Add dashboard to list all user summaries
Flashcard Quiz Mode Interactive Q&A quiz from flashcards
Advanced AI Model Upgrade to facebook/bart-large-cnn for better quality
Theme Switch Light/Dark mode toggle
Export Options Download summaries as PDF or TXT
Author

Jef Perry
2nd Year Computer Programming Student
AI Study Assistant Project — 2025
