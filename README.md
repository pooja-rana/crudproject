# User Management API (Django + DRF)

This project provides a Django REST Framework (DRF)-based API for user management with authentication and role-based access control.

## Features
- User authentication via cell number and password
- Role-based access control (Admin & Normal User)
- Token-based authentication using `AccessToken`
- CRUD operations for user management
- Secure password storage using encryption

## API Endpoints
### Authentication
- **POST** `/user/login/` - User login (requires `cell_number` and `password`)

### Admin Only
- **POST** `/users/` - Create a new user
- **GET** `/users/<id>/` - Retrieve user details
- **PATCH** `/users/<id>/` - Update user details
- **DELETE** `/users/<id>/` - Delete a user
- **GET** `/users/` - List all users

### Normal User Access
- **GET** `/users/<id>/` - Retrieve their own profile details

---
## Installation Guide

### 1️⃣ System Requirements
Ensure you have the following installed:
- Python 3.10+
- PostgreSQL or MySQL
- Pip and Virtual Environment

### 2️⃣ Clone the Repository
```sh
$ cd <project-folder>
$ git clone --branch develop https://github.com/pooja-rana/crudproject.git
```

### 3️⃣ Create a Virtual Environment
```sh
$ python3 -m venv venv
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 4️⃣ Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 5️⃣ Configure Database (MySQL/PostgreSQL)
Update `DATABASES` settings in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':env.str("POSTGRES_DB"),
        'USER': env.str("POSTGRES_USER"),
        'PASSWORD': env.str("POSTGRES_PASSWORD"),
        'HOST': env.str("POSTGRES_HOST"),
        'PORT': env.str("POSTGRES_PORT"),
    }
}
```

### 6️⃣ Apply Migrations
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

### 7️⃣ Create a Superuser (Admin)
```sh
$ python manage.py createsuperuser
```
Follow the prompts to set up an admin user.

### 8️⃣ Run the Development Server
```sh
$ python manage.py runserver
```

### 9️⃣ Access the API
- Open `http://127.0.0.1:8000/api/users/`
- Use Postman or `curl` to test API endpoints

---
## Authentication & Token Management
- Users authenticate via `cell_number` and `password`
- On successful login, an `AccessToken` is generated and stored
- The token must be included in the `Authorization` header for protected routes:
```sh
Authorization:  <token>
```


