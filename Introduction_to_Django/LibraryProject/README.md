# Introduction to Django – ALX Week 10

## Task: Introduction to Django Development Environment Setup

### Objective

    The goal of this task is to gain familiarity with Django by setting up a basic development environment and creating a simple Django project. This serves as the foundation for all future Django applications and introduces you to the workflow of Django development.

### Steps Followed

    1. Install Django

-       Ensured Python was already installed.
-       Installed Django using pip:

        pip install django

  2.  Create Django Project
      Created a new Django project named LibraryProject:

      django-admin startproject LibraryProject

  3.  Run Development Server
      Navigated into the project directory:
      cd LibraryProject

      Created this README.md file inside the project directory.

      Started the development server:
      python manage.py runserver

      Project Structure Overview
      File/Folder Purpose
      manage.py Command-line utility to interact with the project.

      LibraryProject/ Main project folder (contains configuration files).

      settings.py Configuration file for Django project (installed apps, middleware, etc).

      urls.py URL declarations – like a “table of contents” for the site.

      asgi.py/wsgi.py Interface files used for deploying the application.

      Repository Info
      GitHub Repository: Alx_DjangoLearnLab

      Directory: Introduction_to_Django

      Author
      Ohazulike Stanley
      ALX Software Engineering Program – Week 10
