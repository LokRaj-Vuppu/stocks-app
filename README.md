# Stocks App 📈

A Django-based web application for viewing and tracking stock market information. Built with Python, Django 4.2, and a clean HTML/CSS/JavaScript frontend.

---

## Features

- Search and view stock details
- Stock data display with a structured Django app
- Clean, responsive frontend using HTML, CSS, and JavaScript
- Django templating for dynamic page rendering
- SQLite database for lightweight local storage
- CI/CD pipeline via GitHub Actions

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Django 4.2 |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| CI/CD | GitHub Actions |

---

## Project Structure

```
stocks-app/
├── .github/workflows/    # GitHub Actions CI/CD
├── stock_details/        # Core Django app (models, views, urls)
├── stocks_app/           # Django project settings
├── templates/            # HTML templates
├── static/               # CSS, JS, and static assets
├── manage.py
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/LokRaj-Vuppu/stocks-app.git
cd stocks-app
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Database Setup

```bash
python manage.py migrate
```

### Run the App

```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

---

## CI/CD

GitHub Actions workflow is included under `.github/workflows/` for automated checks on every push.

---

## Author

**LokRaj Vuppu** — [GitHub](https://github.com/LokRaj-Vuppu)
