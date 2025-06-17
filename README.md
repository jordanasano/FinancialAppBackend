# FinancialAppBackend 🐍

A Flask-based backend for the FinancialApp that provides secure, RESTful APIs for financial planning, paycheck estimation, and user authentication. This service integrates with external APIs (e.g., ADP and Gemini AI) and is designed for seamless interaction with the React frontend.

## Features

- JWT-based authentication (signup/login)
- CRUD for financial entries (income, expenses, etc.)
- Paycheck and mortgage estimation logic
- Integration with Google Gemini AI and ADP APIs
- CORS support for frontend/backend communication
- Secure environment config with `python-dotenv`

## Tech Stack

- Python 3.10+
- Flask
- Flask-CORS
- Pydantic (for validation)
- Gunicorn (for production server)
- Requests (for HTTP calls)
- python-dotenv (env config)
- Google Generative AI SDKs

## Setup

1. **Clone the repo**:
   ```bash
   git clone https://github.com/jordanasano/FinancialAppBackend.git
   cd FinancialAppBackend

2. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # On Windows: venv\Scripts\activate
    
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   Set up environment variables:

4. Create a .env file in the root directory:
   ```bash
   API_KEY=your_gemini_api_key
   ORIGIN_TO_WHITELIST=your_frontend_url

5. Run the server locally:
   ```bash
   flask run

6. Run in production (e.g., with Gunicorn):
   ```bash
   gunicorn app:app

### Project Structure
```graphql
FinancialAppBackend/
├── app.py               # Main Flask app
├── routes/              # Blueprint routes for auth, finance, etc.
├── services/            # Logic for AI & API integrations
├── models/              # Pydantic schemas
├── utils/               # Helper functions
├── requirements.txt
└── .env                 # Environment variables (not committed)

### API Endpoints
```bash
POST /auth/signup – Register new user
POST /auth/login – Authenticate user & return JWT
POST /estimate/paycheck – Calculate net income
POST /estimate/mortgage – Estimate mortgage affordability
POST /ai/advice – Get personalized financial advice using Gemini AI
   
