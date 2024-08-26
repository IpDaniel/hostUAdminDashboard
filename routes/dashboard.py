# routes/dashboard.py
from flask import Blueprint, render_template, session, redirect, url_for

dashboard_bp = Blueprint('dashboard', __name__)

#Dashboard route
@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('home.html', user=session['user_id'])
    return redirect(url_for('index'))
