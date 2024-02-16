# Piscine Django - Day 7

## Overview

The FightClub Django Blog project is a comprehensive exploration of advanced Django features through a series of exercises that cumulatively build a fully functional blog. Key features implemented in this project include:

- **Model Construction:** Setting up the basic models for the application, such as articles and user favorites.
- **Generic Class-Based Views:** Utilization of Django's generic views for efficient and modular code.
- **User Authentication:** Implementing user login, registration, and logout functionalities.
- **Article and Favorites Management:** Enabling users to publish articles and save favorites.
- **Template Tags and Filters:** Customization of the display of information using Django's template system.
- **Bootstrap Integration:** Styling the site using Bootstrap for a professional look.
- **Internationalization:** Making the site multilingual, primarily focusing on English and French.
- **Testing with Django's Framework:** Ensuring reliability and functionality through Django's built-in testing tools.

This project serves as a robust example of a Django web application

## Installation

To get started with this project, follow these steps:

### Setting Up the Environment

1. **Create a Virtual Environment:**
   ```bash
   python3 -m virtualenv venv
   source venv/bin/activate
   ```
2. **Dependency Installation**
   ```bash
   pip install -r requirements.txt
   ```
3. **Project Initialization**
   ```bash
   cd fightclub
   python manage.py makemigrations blog
   python manage.py migrate
   python manage.py runserver
   ```
4. **DB Initialization**
   ```bash
   python manage.py loaddata users_fixture.json
   python manage.py loaddata articles_fixture.json
   python manage.py loaddata favourite_fixture.json
   ```