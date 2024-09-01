# routes/dashboard.py

# import app dependencies
from flask import Blueprint, render_template, session, redirect, url_for, jsonify

# import other file dependencies
from scripts.python.connect import run_query
from scripts.python.user import User, find_user_by_id, get_user_object_by_id
from scripts.python.query import get_query_by_name
from scripts.python.dashboard_helpers import generate_weekly_data, get_past_six_days

queries_bp = Blueprint('queries', __name__)

# Queries page route
@queries_bp.route('/queries-home')
def queries_home():
    if 'user_id' in session:
        return render_template('queries/queries_home.html')
    return jsonify({"message": "No session active"}), 401


#Saved queries route
@queries_bp.route('/saved-queries')
def saved_queries():
    if 'user_id' in session:
        return render_template('queries/saved-queries.html')
    return jsonify({"message": "No session active"}), 401


#LLM queries route
@queries_bp.route('/llm-queries')
def llm_queries():
    if 'user_id' in session:
        return render_template('queries/llm-queries.html')
    return jsonify({"message": "No session active"}), 401


#SQL queries route
@queries_bp.route('/sql-queries')
def sql_queries():
    if 'user_id' in session:
        return render_template('queries/write-sql-queries.html')
    return jsonify({"message": "No session active"}), 401