# Vet AI Assistant 🐾

An AI-powered veterinary assistant built with **Python**, **FastAPI**, **Google Gemini**, and **Google Calendar API**. The assistant helps pet owners receive instant veterinary guidance and seamlessly schedule appointments through natural language conversations.

## Features

### 🤖 AI-Powered Veterinary Support

* Answers pet care and wellness questions.
* Provides guidance on vaccinations, nutrition, and general health concerns.
* Natural conversational experience powered by Google Gemini.

### 📅 Automated Appointment Scheduling

* Creates Google Calendar events directly from user conversations.
* Extracts appointment details using AI.
* Checks calendar availability before booking.
* Generates confirmations automatically.

### ⚡ FastAPI Backend

* High-performance REST API.
* Async request handling.
* Easily extensible architecture.

### 🔒 Secure Configuration

* Environment variable management using `.env`.
* Secure integration with Gemini and Google APIs.

---

## Tech Stack

| Technology          | Purpose                |
| ------------------- | ---------------------- |
| Python              | Backend Language       |
| FastAPI             | API Framework          |
| Google Gemini       | LLM & Function Calling |
| Google Calendar API | Appointment Scheduling |
| uv                  | Dependency Management  |
| Uvicorn             | ASGI Server            |

---

## Project Structure

```text
vet-ai-assistant/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── utils/
│
├── credentials/
│   └── credentials.json
│
├── .env
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```

---

## Prerequisites

* Python 3.11+
* uv
* Google Gemini API Key
* Google Calendar API Credentials

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd vet-ai-assistant
```

### Install Dependencies Using uv

```bash
uv sync
```

This will create the virtual environment and install all dependencies defined in `pyproject.toml`.

---

## Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key

GOOGLE_CALENDAR_ID=your_calendar_id

GOOGLE_CREDENTIALS_FILE=credentials/credentials.json
```

---

## Google Calendar Setup

1. Create a project in Google Cloud Console.
2. Enable the Google Calendar API.
3. Create OAuth or Service Account credentials.
4. Download the credentials JSON file.
5. Place it inside:

```text
credentials/credentials.json
```

6. If using a Service Account, share the calendar with the service account email.

---

## Running the Application

Start the FastAPI server:

```bash
uv run uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

---

## API Documentation

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

---

## Example Conversation

### User

```text
My dog needs a vaccination appointment next Tuesday at 4 PM.
```

### Assistant Workflow

1. Gemini identifies appointment intent.
2. Extracts date and time.
3. Checks Google Calendar availability.
4. Creates calendar event.
5. Returns booking confirmation.

### Response

```text
Your appointment has been successfully scheduled for Tuesday at 4:00 PM.
```

---

## API Endpoint

### POST /chat

#### Request

```json
{
  "message": "Book a vet appointment for my cat tomorrow at 3 PM"
}
```

#### Response

```json
{
  "response": "Your appointment has been scheduled successfully."
}
```

---

## Development

Install a new dependency:

```bash
uv add package-name
```

Install a development dependency:

```bash
uv add --dev package-name
```

Update dependencies:

```bash
uv lock
uv sync
```

Run Python scripts:

```bash
uv run python script.py
```

---

## Future Enhancements

* Appointment rescheduling
* Appointment cancellation
* Email notifications
* SMS reminders
* Voice-enabled interactions
* Multi-language support
* Pet medical history tracking

---

## Disclaimer

This application provides informational assistance and appointment scheduling support only. It is not intended to replace professional veterinary advice, diagnosis, treatment, or emergency care.

---

## Author

**Divyshekhar Sinha**

Built with FastAPI, Google Gemini, Google Calendar API, and uv.
