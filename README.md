# Bendora Technology — Portfolio Website

A modern, production-ready portfolio built with Flask.

## Local Development

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # edit SECRET_KEY
flask run
```

## Deploy to Render

1. Push repo to GitHub.
2. New Web Service → connect repo.
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `gunicorn app:app`
5. Add env var `SECRET_KEY`.

## Formspree

Replace `YOUR_FORM_ID` in `templates/contact.html` with your real Formspree endpoint.
