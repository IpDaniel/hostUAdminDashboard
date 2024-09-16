#Import project structure dependencies
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import bcrypt
from datetime import datetime, timedelta
import openai
import csv

#Import helper function files
from scripts.python.user import read_users, write_user, find_user_by_username, get_user_object_by_id
from scripts.python.connect import run_query
from scripts.python.query import write_new_query, get_queries_by_creator, get_query_by_name, update_last_used


query_text = '''SELECT COUNT(*) FROM "ConversationMessage" cm WHERE cm."createdAt" >= NOW() - INTERVAL '24 HOURS';'''

me = get_user_object_by_id('936df00d-f3ee-4596-8f35-3c97b4b644b8')



# write_new_query("Total messages in last 24 hours", me.id, query_text=query_text)



# TESTING OPENAI API
# Initialize the OpenAI API client with the API key
# openai.api_key = "your-api-key-here"

# def generate_sql_query(prompt):
#     """
#     Function to generate an SQL query using OpenAI's GPT model.
    
#     :param prompt: A string prompt that describes what SQL query you want.
#     :return: The generated SQL query string.
#     """

#     prompt = "Generate an SQL query that will fetch the data described here from the hostU database: " + prompt

#     # From the database with the following structure: blah blah blah

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[
#                 {"role": "system", "content": "You are an expert SQL query writer who writes SQL queries from "},
#                 {"role": "user", "content": prompt}
#             ],
#             max_tokens=150
#         )
        
#         # Extract the generated response
#         sql_query = response['choices'][0]['message']['content'].strip()
#         return sql_query
#     except Exception as e:
#         print(f"Error generating SQL query: {e}")
#         return None

# # Example usage
# prompt = "Write an SQL query to find the top 5 customers by order amount in the last month."
# sql_query = generate_sql_query(prompt)
# print(sql_query)


def filter_csv_by_creator(creator_id, file_path='data/queries.csv'):
    """
    Parses through the CSV file and returns a list of dictionaries for rows where creatorId matches the specified creator_id.

    Args:
    - file_path (str): Path to the CSV file.
    - creator_id (str): The creatorId to filter the rows by.

    Returns:
    - List[dict]: List of dictionaries where each dictionary represents a row from the CSV.
    """
    matching_rows = []

    # Open the CSV file
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        # Iterate over the rows in the CSV
        for row in csv_reader:
            # Check if the creatorId matches
            if row['creatorId'] == creator_id:
                matching_rows.append(row)

    return matching_rows

# Example usage
# creator_id = '936df00d-f3ee-4596-8f35-3c97b4b644b8'
# result = filter_csv_by_creator(creator_id)
# for query in result:
#     print(query)
