import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    'dbname': 'hostu-db',
    'user': 'daniel-admin',
    'password': 'AVNS_GJc4RFzPbp3L9jqJniD',
    'host': 'app-36e6af5c-2e43-41be-bd12-6ea0d3dd6ad1-do-user-14475986-0.b.db.ondigitalocean.com',
    'port': '25060'
}

try:
    # Connect to the database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Execute a read-only query
    cursor.execute("SELECT * FROM \"Conversation\" LIMIT 10;")

    # Fetch the results
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL database: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
