# Bendora Technology — Portfolio & Business Website

A modern, production-ready business website for Bendora Technology, built with Flask and deployed on Render. The site showcases services, projects, and provides a direct contact channel for potential clients.

---

## 🌐 Live Website

**https://bendoratechnology.onrender.com**

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Frontend | HTML5, CSS3, JavaScript |
| Fonts | Syne, DM Sans (Google Fonts) |
| Icons | Font Awesome 6 |
| Form Handling | Formspree |
| Hosting | Render |
| Version Control | Git & GitHub |

---

## 📄 Pages

| Page | Description |
|------|-------------|
| **Home** | Hero section, services overview, featured projects, stats, and CTA |
| **About** | Story, tech stack, experience timeline, and personal interests |
| **Services** | Detailed breakdown of Web Development, Software Solutions, Cloud Services, and UI/UX Design |
| **Portfolio** | Filterable project showcase with tech stack tags |
| **Contact** | Contact form powered by Formspree, contact details and social links |
| **Privacy Policy** | Full privacy policy for the business |

---

## Project Structure

```
bendora-website/
│
├── 📄 app.py                    # Application entry point, routes & error handlers
├── 📄 requirements.txt          # Python package dependencies
├── 📄 Procfile                  # Render/Gunicorn deployment configuration
├── 📄 .env                      # Local environment variables (never committed)
├── 📄 .gitignore                # Files and folders excluded from version control
├── 📄 README.md                 # Project documentation
│
├── 📁 static/                   # All static assets served directly by Flask
│   ├── 📁 css/
│   │   └── 📄 style.css         # Global stylesheet — variables, layout, components
│   ├── 📁 js/
│   │   └── 📄 main.js           # Scroll animations, filters, navbar, form validation
│   └── 📁 images/
│       └── 📄 profile.jpeg      # Developer profile photo
│
└── 📁 templates/                # Jinja2 HTML templates rendered by Flask
    ├── 📄 base.html             # Master layout — navbar, footer, meta tags
    ├── 📄 index.html            # Homepage — hero, services, projects, stats
    ├── 📄 about.html            # About — story, skills, timeline, interests
    ├── 📄 services.html         # Services — detailed breakdown of all offerings
    ├── 📄 portfolio.html        # Portfolio — filterable project showcase
    ├── 📄 contact.html          # Contact — Formspree form and contact details
    ├── 📄 privacy.html          # Privacy Policy — legal data usage information
    ├── 📄 404.html              # 404 error — page not found handler
    └── 📄 500.html              # 500 error — internal server error handler

---

## 🚀 Local Development

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

---

## ☁️ Deployment on Render

1. Push your code to GitHub
2. Go to [render.com](https://render.com) and create a new **Web Service**
3. Connect your GitHub repository
4. Set the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Add environment variable:
   - `SECRET_KEY` — set to a long random string
6. Click **Deploy** — your site will be live in minutes

---

## 📬 Contact Form Setup

The contact form uses [Formspree](https://formspree.io). To set it up:

1. Create a free account at formspree.io
2. Create a new form and copy your Form ID
3. In `templates/contact.html` replace `YOUR_FORM_ID` with your real ID:
```html
action="https://formspree.io/f/YOUR_FORM_ID"
```

---

## 🔐 Environment Variables

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Flask secret key for session security |
| `FLASK_DEBUG` | Set to `true` for development, `false` for production |

---

## 📜 License

© 2024 Bendora Technology. All rights reserved.  
Unauthorized use, reproduction, or distribution of any content or code from this repository is strictly prohibited.

---

## 📞 Contact

| Channel | Details |
|---------|---------|
| **Email** | bendoratechnology@gmail.com |
| **LinkedIn** | https://www.linkedin.com/in/princeton-r-zahnmie-601a8a211 |
| **GitHub** | https://github.com/raccazahn |
| **Website** | https://bendoratechnology.onrender.com |
