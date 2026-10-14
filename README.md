# SWYNEX Deployable Backend Service

## Project Overview

This project is developed as part of the SWYNEX internship. It is a Flask-based REST API that provides health checks and sample item management.

## Technologies Used

* Python
* Flask
* REST API
* JSON
* Gunicorn

## Features

* Home endpoint
* Health check endpoint
* Retrieve all items
* Retrieve an item by ID
* Create an item
* Update an item
* Delete an item
* Basic input validation
* JSON responses with HTTP status codes

## Project Files

* `app.py` — Backend application.
* `requirements.txt` — Required Python packages.
* `sample_data.json` — Sample item data.
* `README.md` — Project documentation.

## Installation

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run Locally

Start the Flask application:

```bash
python app.py
```

The local service runs at:

`http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint          | Description          |
| ------ | ----------------- | -------------------- |
| GET    | `/`               | Welcome message      |
| GET    | `/health`         | Check service health |
| GET    | `/api/items`      | Retrieve all items   |
| GET    | `/api/items/<id>` | Retrieve one item    |
| POST   | `/api/items`      | Create an item       |
| PUT    | `/api/items/<id>` | Update an item       |
| DELETE | `/api/items/<id>` | Delete an item       |

## Sample POST Request

Endpoint: `POST /api/items`

JSON request body:

```json
{
  "name": "Webcam",
  "description": "USB webcam"
}
```

A successful creation returns HTTP status `201 Created`.

## Deployment

Install dependencies using:

```bash
pip install -r requirements.txt
```

Start the service using Gunicorn:

```bash
gunicorn app:app
```

The public deployment URL will be added after successful deployment.

## Important Note

The current application stores item changes in memory. Data added or modified through the API may be lost when the application restarts. The `sample_data.json` file is provided separately and is not automatically loaded by the current application.

## Internship

Developed as part of the SWYNEX internship.
