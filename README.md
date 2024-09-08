# Django-Based Blog Application

## Overview

This document outlines the structure and functionality of a blog application built using the Django framework for Python. This project allows users to create, view, and manage blog posts through a user-friendly web interface.

## Directory Structure

```bash
Django_blog
|
├── README.md
├── db.sqlite3
├── django_blog
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── posts
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static
│   ├── css
│   │   └── style.css
│   ├── img
│   │   └── logo.png
│   ├── js
│   └── posts
│       ├── css
│       ├── img
│       │   └── contact.png
│       └── js
└── templates
    ├── base.html
    ├── contact.html
    ├── post_list.html
    └── single_post.html

16 directories, 34 files
```

## Key Components

- `manage.py`: The command-line utility for interacting with the Django project.
- `django_blog/`: Contains the main Django project configuration.
  - `settings.py`: Contains settings for the Django project.
  - `urls.py`: Maps URL paths to views across the entire project.
  - `wsgi.py`: Entry point for WSGI-compatible web servers.
- `posts/`: Contains application-specific code related to blog posts.
  - `models.py`: Defines the data models for blog posts.
  - `views.py`: Contains view functions for handling requests and responses related to blog posts.
  - `urls.py`: Maps URL paths to views for the posts application.
- `static/`: Contains static assets like CSS files, JavaScript, and images.
  - `css/style.css`: Defines the application's visual styling.
  - `img/logo.png`: Logo image used in the application.
  - `posts/`: Contains additional static assets related to posts.
    - `css/`: Additional CSS for the posts section.
    - `img/contact.png`: Image used in the contact page.
- `templates/`: Contains HTML templates for rendering the application's UI.
  - `base.html`: Base template that other templates extend.
  - `contact.html`: Page displaying contact information.
  - `post_list.html`: Displays a list of blog posts.
  - `single_post.html`: Page showing detailed information for a single blog post.

## Prerequisites

Ensure you have Python (version 3.6 or higher) and pip installed on your system.

## Setup Instructions

1. Clone the repository:

```bash
git clone git@github.com/django_blog.git
cd django_blog
```

2. Set up a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations to set up the database:

```bash
python manage.py migrate
```

5. Create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```

## Running the Application

To start the application, execute these commands in your terminal:

```bash
python manage.py runserver
```

Once running, you can access the application at <http://127.0.0.1:8000>.

## Key Features

1. **View Blog Posts**: Browse the list of blog posts on the main page.
2. **Read Single Post**: Click on a blog post to view detailed content.
3. **Contact Page**: Access the contact page for getting in touch.

## Contributing

I welcome contributions to this project. If you'd like to suggest improvements or report issues, please submit a pull request or open an issue through the appropriate channels.

## Conclusion

This Blog Application, built on the Django framework, offers a simple and effective way to manage and display blog posts. With its intuitive interface and basic functionality, it serves as a solid foundation for creating a full-featured blogging platform. I encourage you to explore the capabilities of this application and contribute to its development.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
