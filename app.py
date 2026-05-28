import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'bendora-tech-secret-2024')

# ─── Page Routes ────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html', active='home')

@app.route('/about')
def about():
    return render_template('about.html', active='about')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', active='portfolio')

@app.route('/services')
def services():
    return render_template('services.html', active='services')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', active='')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name    = request.form.get('name', '').strip()
        email   = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()

        if not all([name, email, subject, message]):
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('contact'))

        flash('Message sent! I\'ll get back to you soon.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html', active='contact')

# ─── Error Handlers ─────────────────────────────────────────────────────────────

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

# ─── Run ────────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))