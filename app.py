#Import project structure dependencies
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import bcrypt
from datetime import timedelta

#Import helper function files
from scripts.python.user import read_users, write_user, find_user_by_username, get_user_object_by_id

#Import other routes as blueprints
from routes.dashboard import dashboard_bp

#create app
app = Flask(__name__)

#Register other routes blueprints
app.register_blueprint(dashboard_bp)

# Configure the secret key for session management
app.config['SECRET_KEY'] = 'my-temporary-secret-key'

# Set Permanent session lifetime
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

# Setting session properties
@app.before_request
def make_session_permanent():
    session.permanent = True
    session.modified = True


# route for login form
@app.route('/', methods=['GET'])
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard.dashboard'))
    return render_template('index.html')


# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password').encode('utf-8')
    user = find_user_by_username(username)

    if user and bcrypt.checkpw(password, user['password'].encode('utf-8')):
        session['user_id'] = user['id']
        print(user['id'] + ' logged in')
        return jsonify({"message": "Login successful", "redirect": url_for('dashboard.dashboard')}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


# Logout route
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful"}), 200


# Check session route
@app.route('/session')
def check_session():
    if 'user_id' in session:
        return jsonify({"user_id": session['user_id']}), 200
    return jsonify({"message": "No user logged in"}), 401


# Help page route
@app.route('/help')
def help():
    if 'user_id' in session:
        return render_template('help.html')
    return jsonify({"message": "No session active"}), 401


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
