# Flask Shows API

A simple Flask REST API with JWT authentication for managing users, guests, episodes, and appearances.

## Setup

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo/server



🔐 Authentication
POST /auth/login → returns access token

Use the token for protected routes in the Authorization header:


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


