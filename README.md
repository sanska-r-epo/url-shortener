# URL Shortener API

## Overview
This project is a basic URL shortener API built using FastAPI and PostgreSQL. The API allows users to shorten long URLs and redirect them to original URL using a short code. The project focuses on demonstrating clean and well-documented code, along with efficient API design.

## Endpoints

1. **POST /shorten**: Accepts a long URL and returns a shortened URL.
2. **GET /{short_code}**: Redirects to the original URL based on the provided short code.

## Requirements
- Python 3.8+
- PostgreSQL

### Setup

* Clone the repository :
   ```bash
   git clone https://github.com/sanska-r-epo/url-shortener.git
   ```
* Navigate to the project directory :
   ```bash
   cd url-shortener
   ```
* Creaing virtual environment :
   ```bash
   python3 -m venv env
   ```
* Install necessary dependencies :
   ```bash
   pip install -r requirements.txt
   ```
* Run  the application :
   ```bash
   uvicorn main:app --reload
   ```
* `you can access the application at`

   `http://127.0.0.1:8000`