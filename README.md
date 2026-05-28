# Bendora Technology — Portfolio & Business Website

A modern, production-ready business website for Bendora Technology, built with Flask and deployed on Render. The site showcases services, projects, and provides a direct contact channel for potential clients.

## Live Website

https://bendoratechnology.onrender.com

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Fonts:** Syne, DM Sans (Google Fonts)
- **Icons:** Font Awesome 6
- **Form Handling:** Formspree
- **Hosting:** Render
- **Version Control:** Git & GitHub

## Pages

- **Home** — Hero section, services overview, featured projects, stats, and CTA
- **About** — Story, tech stack, experience timeline, and personal interests
- **Services** — Detailed breakdown of Web Development, Software Solutions, Cloud Services, and UI/UX Design
- **Portfolio** — Filterable project showcase with tech stack tags
- **Contact** — Contact form powered by Formspree, contact details and social links
- **Privacy Policy** — Full privacy policy for the business

## Project Structure
bendora-website/
├── app.py                  # Flask application and routes
├── requirements.txt        # Python dependencies
├── Procfile                # Render deployment config
├── .env                    # Environment variables (not committed)
├── static/
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── js/
│   │   └── main.js         # JavaScript interactions
│   └── images/
│       └── profile.jpeg    # Profile photo
└── templates/
├── base.html           # Base template with navbar and footer
├── index.html          # Homepage
├── about.html          # About page
├── services.html       # Services page
├── portfolio.html      # Portfolio page
├── contact.html        # Contact page
├── privacy.html        # Privacy policy page
├── 404.html            # 404 error page
└── 500.html            # 500 error page

## Local Development

**1. Clone the repository**
```bash
git clone https://github.com/raccazahn/bendora-website.git
cd bendora-website
```

**2. Create and activate virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create environment file**
```bash
cp .env.example .env
```
Then open `.env` and set your secret key:
SECRET_KEY=your-random-secret-key-here
FLASK_DEBUG=true

**5. Run the development server**
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## Deployment on Render

1. Push your code to GitHub
2. Go to [render.com](https://render.com) and create a new **Web Service**
3. Connect your GitHub repository
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Add environment variable:
   - `SECRET_KEY` — set to a long random string
6. Click **Deploy** — your site will be live in minutes

## Contact Form Setup

The contact form uses [Formspree](https://formspree.io). To set it up:

1. Create a free account at formspree.io
2. Create a new form and copy your Form ID
3. In `templates/contact.html` replace `YOUR_FORM_ID` with your real ID:
```html
action="https://formspree.io/f/YOUR_FORM_ID"
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Flask secret key for session security |
| `FLASK_DEBUG` | Set to `true` for development, `false` for production |

## License

© 2024 Bendora Technology. All rights reserved.

## Contact

**Email:** bendoratechnology@gmail.com  
**LinkedIn:** https://www.linkedin.com/in/princeton-r-zahnmie-601a8a211  
**GitHub:** https://github.com/raccazahn  
**Website:** https://bendoratechnology.onrender.com
