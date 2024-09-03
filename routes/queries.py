# routes/dashboard.py

# import app dependencies
from flask import Blueprint, render_template, session, redirect, url_for, jsonify, request

# import other file dependencies
from scripts.python.connect import run_query, run_query_with_headers
from scripts.python.user import User, find_user_by_id, get_user_object_by_id
from scripts.python.query import get_query_by_name, get_queries_by_creator, get_query_by_name_and_creator, edit_query

queries_bp = Blueprint('queries', __name__)



#PAGES
#----------------------------------------------------------

# Queries page route
@queries_bp.route('/queries-home')
def queries_home():
    if 'user_id' in session:
        return render_template('queries/queries-home.html')
    return redirect(url_for('index'))


#Saved queries route
@queries_bp.route('/saved-queries')
def saved_queries():
    if 'user_id' in session:
        return render_template('queries/saved-queries.html')
    return redirect(url_for('index'))


#LLM queries route
@queries_bp.route('/llm-queries')
def llm_queries():
    if 'user_id' in session:
        return render_template('queries/llm-queries.html')
    return redirect(url_for('index'))


#SQL queries route
@queries_bp.route('/sql-queries')
def sql_queries():
    if 'user_id' in session:
        return render_template('queries/write-sql-queries.html')
    return redirect(url_for('index'))



#DATA
#--------------------------------------------------------------------

#Returns the list of queries that this user has saved
@queries_bp.route('/get-saved-queries', methods=['GET'])
def get_saved_queries():
    if 'user_id' in session:
        # user = get_user_object_by_id(session['user_id'])
        queries = get_queries_by_creator(session['user_id'])
        print(f'user {session['user_name']} has retrieved their saved queries')
        return jsonify(queries)
    return jsonify({"message": "No session active"}), 401


# Runs a saved query and returns the results
@queries_bp.route('/run-saved-query', methods=['POST'])
def run_saved_queries():
    if 'user_id' in session:
        data = request.json
        query_name = data.get('queryName')
        user = get_user_object_by_id(session['user_id'])
        query = get_query_by_name_and_creator(query_name, user.id) #This returns a dictionary not object
        query_text = query['queryText']
        headers, fetched_data = run_query_with_headers(user, queryText=query_text)
        print(f'user {session['user_name']} ran query \"{query_name}\"')
        response = {"queryTitle": query_name,
                    "plaintextPrompt": query['plaintextPrompt'],
                    "queryText": query['queryText'],
                    "Headers": headers,
                    "Data": fetched_data}
        return jsonify(response)
    return jsonify({"message": "No session active"}), 401


# Saves a query (in theory)
@queries_bp.route('/save-query', methods=['POST'])
def save_query():
    if 'user_id' in session:
         # Parse the JSON data from the request
        data = request.json

        # Extract variables from the parsed data
        current_title = data.get('currentTitle')
        new_title = data.get('newTitle')
        plaintext_prompt = data.get('plaintextPrompt')
        sql_query = data.get('queryText')

        edit_query(current_name=current_title,
                   creator_id=session['user_id'],
                   new_title=new_title,
                   plaintext_prompt=plaintext_prompt,
                   query_text=sql_query)
        
        print(f'User {session['user_name']} has saved a query as \"{new_title}\"')
        return jsonify({'status': 'success'}), 200
    return jsonify({"message": "No session active"}), 401