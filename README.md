# Portfolio Website

Personal portfolio website built with FastAPI and plain HTML/Tailwind CSS.

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn
- **Frontend:** HTML, Tailwind CSS (CDN), Font Awesome, Google Fonts
- **Templating:** Jinja2

## Features

- Single-page portfolio with sections: About, Skills, Experience, Projects, Education
- CV download endpoint (`/cv`) serving a PDF directly
- No JavaScript framework, no build step — fast and lightweight

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open [http://localhost:8000](http://localhost:8000).

> **Note:** The CV PDF is not included in the repository. Place your file at `static/gonzalez-sanchez-cv.pdf` before running.
