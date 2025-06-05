# AI Chatbot Backend

A Django REST API providing user registration/login (with JWT), chat history, and OpenAI GPT-based chatbot integration.

---

## Features

- **User Auth:** Register, login, JWT-based authentication.
- **Chatbot:** Integrates with OpenAI GPT models (supports mock mode for development/testing).
- **Chat History:** Stores/retrieves user chat history.
- **PostgreSQL** database support.
- **Dockerized** for easy deployment.

---

## Requirements

- Python 3.9+
- PostgreSQL
- Docker (optional, for containerized deployment)
- OpenAI API key (or use mock mode for dev/testing)

---

## Setup

### 1. Clone the Repository

```bash
git clone <YOUR_REPO_URL>
cd <repo_folder>
```

### 2. Create `.env` File

Copy `.env.example` to `.env` and fill in your details:

```env
POSTGRES_DB=chatbot_db
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
OPENAI_API_KEY=sk-... 
USE_MOCK_AI=1      
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Server

```bash
python manage.py runserver
```

---

## Running with Docker

1. Ensure your `.env` is set up.
2. Build and run:

```bash
docker build -t ai-chatbot .
docker run --env-file .env -p 8000:8000 ai-chatbot
```

---

## API Documentation

### **Register**

- **Endpoint:** `POST /api/register`
- **Payload:**
  ```json
  {
    "username": "your_username",
    "password": "your_password",
    "email": "your@email.com"
  }
  ```
- **Response:**  
  `{"message": "User registered successfully"}`

---

### **Login**

- **Endpoint:** `POST /api/login`
- **Payload:**
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response:**  
  `{"token": "<jwt_token>"}`

---

### **Chat with Bot**

- **Endpoint:** `POST /api/chat`
- **Headers:** `Authorization: Bearer <jwt_token>`
- **Payload:**
  ```json
  {
    "message": "Hello AI!"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "user_message": "Hello AI!",
    "bot_response": "Hi! How can I help you?",
    "timestamp": "2025-06-05T07:30:23.208852Z"
  }
  ```

---

### **Get Chat History**

- **Endpoint:** `GET /api/chat/history`
- **Headers:** `Authorization: Bearer <jwt_token>`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "user_message": "Hello",
      "bot_response": "Hi, how can I help you?",
      "timestamp": "2025-06-05T05:11:35.205822Z"
    }
  ]
  ```

---

## Testing with Postman

1. Register a new user (`/api/register`).
2. Login to get JWT token (`/api/login`).
3. For `/api/chat` and `/api/chat/history`, set the header:
   ```
   Authorization: Bearer <jwt_token>
   ```
4. Send chat messages and fetch chat history.

---

## Deployment Notes

- For production, set `DEBUG=0` in `settings.py` and ensure strong secret keys.
- Use PostgreSQL as configured in `.env`.
- For actual OpenAI usage, provide a valid API key and set `USE_MOCK_AI=0` or remove.

---