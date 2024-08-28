# routes/dashboard.py

# import app dependencies
from flask import Blueprint, render_template, session, redirect, url_for, jsonify

# import other file dependencies
from scripts.python.connect import run_query
from scripts.python.user import User, find_user_by_id, get_user_object_by_id
from scripts.python.query import get_query_by_name
from scripts.python.dashboard_helpers import generate_weekly_data, get_past_six_days

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


#return new user data for last 7 days
@dashboard_bp.route('/get-bar-chart-data', methods=['GET'])
def get_bar_chart_data():
    data = {"labels": [], "data": []}
    if 'user_id' in session:
        user = get_user_object_by_id(session['user_id'])
        data["labels"] = get_past_six_days()
        data["data"] = generate_weekly_data(user)
    return jsonify(data)


#return total number of platform users
@dashboard_bp.route('/total-users', methods=['GET'])
def total_users():
    if 'user_id' in session:
        user = get_user_object_by_id(session['user_id'])
        total_users_query = get_query_by_name('Total number of users')
        total_users = run_query(user=user, queryText=total_users_query['text'])
        return jsonify({'total': total_users})
