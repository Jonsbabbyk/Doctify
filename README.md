#  Hospital Booking Website Built With Bootstrap Template  And Django
## Welcome to Doctify a simple site  for booking medical appointments conveniently.
![Screenshot (21)](https://github.com/Jonsbabbyk/Doctify/assets/125735215/4f8ebf56-bd71-4532-bcc1-d292534d1439)
# Django Project Quick Start Guide

This guide will walk you through the steps to create a new Django project and run the development server.

## Step 1: Create a Django Project Directory
  Open your terminal or command prompt.
  Run the following command to create a new directory for your Django project:
     ```bash
     mkdir django && cd django
     ```
   - This command will create a directory named "django" and then change the current directory to "django".
##  Step 2: Set Up Virtual Environment
    pip install virtualenv 
    virtualenv venv
   **On Windows**
   venv\Scripts\activate
  **On Unix or MacOS**
   source venv/bin/activate
## Step 3:Install Django 
    Install Django using pip:
     ```bash
     pip install django
     ```
## Step 4:Start a Django Project
   - Create a new Django project using the following command:
     ```bash
     django-admin startproject my_project .
     ```
   - Replace "my_project" with your preferred project name.
## Step 5:Create a Django Application:
   - Once your project is set up, you can create Django applications within it.
   - To create a new Django application, run the following command:
     ```bash
     python manage.py startapp my_app
     ```
   - Replace "my_app" with the name of your new application.

## Step 6:Create templates:
  mkdir templates static

## Step 7:Run Migrations
Run Migrations:**
   - Navigate to your project directory and run initial migrations:
     ```bash
     python manage.py migrate
     ```
## Step 8:Run the Development Server
   - Start the Django development server:
     ```bash
     python manage.py runserver
     ```
     *Essential commands for Django backend development, a concise reference guide.*

[Click here for full guidance on development of the project](https://www.youtube.com/watch?v=3_3q_dE4_qs)





