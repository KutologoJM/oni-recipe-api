# ONI Recipe API

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.2-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.x-red.svg)
![Poetry](https://img.shields.io/badge/Poetry-managed-informational.svg)

---

A simple API for convenient viewing and filtering of foods in **Oxygen Not Included**.  

Most data and assets are sourced from the [Oxygen Not Included Wiki](https://oxygennotincluded.wiki.gg/).

📖 API documentation: `http://localhost:8000/api/docs/`

---

## Features
- View ONI food items with details like calories, spoilage, and ingredients.
- Filter foods by attributes (e.g., spoil time, quality, calorie density).
- RESTful API built with Django + DRF.
- Managed with Poetry for clean dependency handling.

---

## Usage

### Run locally
```bash
# clone repo
git clone https://github.com/yourusername/oni-recipe-api.git
cd oni-recipe-api

# install dependencies
poetry install

# activate virtual environment
poetry shell

# make and run migrations
python manage.py makemigrations
python manage.py migrate

# create superuser
python manage.py createsuperuser

# run server
python manage.py runserver
```
Visit: http://localhost:8000/api/docs/ for further help
## License

This project is licensed under the  
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/)  
unless otherwise noted.
