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

> **Note:** CV files are not included in the repository (gitignored). Place them manually before running or deploying:
> - `static/gonzalez-sanchez-cv.pdf`
> - `static/gonzalez-sanchez-cv-en.html`
> - `static/gonzalez-sanchez-cv-nl.html`

## Deployment

The app runs on the server as a Docker container behind a Cloudflare tunnel.

### Update code
```bash
# On the server
cd ~/portfolio/portfolio-website
git pull
docker build -t portfolio-website .
docker stop portfolio-website && docker rm portfolio-website
docker run -d --name portfolio-website --restart unless-stopped -p 8000:8000 portfolio-website
```

### Update CV files (manual — not in git)
```bash
# From local machine
scp static/gonzalez-sanchez-cv.pdf acer.gonzalezsanchez.dev:~/portfolio/portfolio-website/static/
scp static/gonzalez-sanchez-cv-en.html acer.gonzalezsanchez.dev:~/portfolio/portfolio-website/static/
scp static/gonzalez-sanchez-cv-nl.html acer.gonzalezsanchez.dev:~/portfolio/portfolio-website/static/
```
