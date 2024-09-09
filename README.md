# Rightshero Project

## Description
This project is designed to manage categories and subcategories with Ajax integration. The backend is built with Django, and the project is containerized using Docker.

## Features
- Categories and subcategories management.
- Ajax integration for dynamic subcategory loading.
- Dockerized setup with MySQL as the database.
- Admin panel for managing data.

## Prerequisites
To run this project, you'll need:
- **Python 3.9 or higher**
- **Docker** and **Docker Compose**

## Local Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Ghonem23/Rightshero-Project
cd rightshero_project
```

### 2. Set up environment variables
Create an .env file with the following:
```bash
DB_NAME=rightshero_db
DB_USER=rightshero_user
DB_PASSWORD=SecureDATAP@ssword2024
DB_HOST=db
DB_PORT=3306
SECRET_KEY=<your_django_secret_key>
```

### 3. Start the Docker containers
```bash
docker-compose up --build
```

### 4. Create a superuser (optional)
To access the admin panel, create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

### 5. Access the application
- Django app: http://localhost:8000/
- Admin panel: http://localhost:8000/admin/

### Testing
- Ensure the categories and subcategories work correctly via Ajax integration.
- Access the admin panel and manage categories/subcategories.

### Technologies Used
- Django 4.2.10
- MySQL 8.0
- Docker & Docker Compose# Rightshero-Project
