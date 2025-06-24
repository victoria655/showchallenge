# Flask Shows API

A simple Flask REST API with JWT authentication for managing users, guests, episodes, and appearances.

## Setup

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo/server

Create and activate virtual environment

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set environment variables in a .env file:

env
Copy
Edit
FLASK_APP=app
FLASK_DEBUG=True
FLASK_SQLALCHEMY_DATABASE_URI=postgresql://user:password@localhost:5432/shows
FLASK_JWT_SECRET_KEY=your_jwt_key
Run migrations and seed data

bash
Copy
Edit
flask db upgrade
python seed.py
Start the server

bash
Copy
Edit
flask run
🔐 Authentication
POST /auth/login → returns access token

Use the token for protected routes in the Authorization header:

makefile
Copy
Edit
Authorization: Bearer <token>
📬 Example Routes
GET /guests

POST /appearances (protected)

GET /episodes

✅ Models
1.User
2.Guest
3.Episode
4.Appearance

MIT License © 2025

pgsql
Copy
Edit
