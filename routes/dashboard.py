# routes/dashboard.py

# import app dependencies
from flask import Blueprint, render_template, session, redirect, url_for, jsonify

# import other file dependencies
from scripts.python.connect import run_query
from scripts.python.user import User, find_user_by_id, get_user_object_by_id
from scripts.python.query import get_query_by_name

dashboard_bp = Blueprint('dashboard', __name__)

#Dashboard route
@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('home.html', user=session['user_id'])
    return redirect(url_for('index'))


#Return the guest/host ratio
@dashboard_bp.route('/guest-host-ratio', methods=['GET'])
def guest_host_ratio():
    
    ratio = "-.--"
    if 'user_id' in session:

        #Create user object
        user = get_user_object_by_id(session['user_id'])

        #Set query strings
        num_guest_users_query = get_query_by_name('Number of guest users')['queryText']

        num_users_query = get_query_by_name('Total number of users')['queryText']

        # calculate the guest/host ratio
        num_guests = run_query(user, num_guest_users_query)[0][0] 
        num_hosts = run_query(user, num_users_query)[0][0] - num_guests 
        ratio = round(num_guests/num_hosts, 2) 
    return jsonify({"ratio": ratio})