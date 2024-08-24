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

weekly_starting_dates = [
    'make_date(2023, 11, 10)',
    'make_date(2023, 11, 17)',
    'make_date(2023, 11, 24)',
    'make_date(2023, 12, 01)',
    'make_date(2023, 12, 08)',
    'make_date(2023, 12, 15)',
    'make_date(2023, 12, 22)',
    'make_date(2023, 12, 29)',
    'make_date(2024, 01, 05)',
    'make_date(2024, 01, 12)',
    'make_date(2024, 01, 19)',
    'make_date(2024, 01, 26)',
    'make_date(2024, 02, 02)',
    'make_date(2024, 02, 09)',
    'make_date(2024, 02, 16)',
    'make_date(2024, 02, 23)',
    'make_date(2024, 03, 01)',
    'make_date(2024, 03, 08)',
    'make_date(2024, 03, 15)',
    'make_date(2024, 03, 22)',
    'make_date(2024, 03, 29)',
    'make_date(2024, 04, 05)',
    'make_date(2024, 04, 12)',
    'make_date(2024, 04, 19)',
    'make_date(2024, 04, 26)',
    'make_date(2024, 05, 03)',
    'make_date(2024, 05, 10)',
    'make_date(2024, 05, 17)',
    'make_date(2024, 05, 24)',
    'make_date(2024, 05, 31)',
    'make_date(2024, 06, 07)',
    'make_date(2024, 06, 14)',
    'make_date(2024, 06, 21)',
    'make_date(2024, 06, 28)',
    'make_date(2024, 07, 05)',
    'make_date(2024, 07, 12)',
    'make_date(2024, 07, 19)',
    'make_date(2024, 07, 26)',
    'make_date(2024, 08, 02)',
    'make_date(2024, 08, 09)',
    'make_date(2024, 08, 16)'
]

monthly_starting_dates = [
    'make_date(2023, 11, 01)',
    'make_date(2023, 12, 01)',
    'make_date(2024, 01, 01)',
    'make_date(2024, 02, 01)',
    'make_date(2024, 03, 01)',
    'make_date(2024, 04, 01)',
    'make_date(2024, 05, 01)',
    'make_date(2024, 06, 01)',
    'make_date(2024, 07, 01)',
    'make_date(2024, 08, 01)'
]



# "SELECT * FROM \"Conversation\" LIMIT 10;"

def make_query(start_date, end_date):
    sql_query = f'''
    select count (*)
    from "User" u
    --inner join "ListingPreferences" p on p."userId" = u.id
    where u."createdAt" > {start_date} and u."createdAt" < {end_date}
    '''
    return sql_query

def convert_date_string(date_string):
    # Extract the year, month, and day from the string
    year, month, day = date_string.replace('make_date(', '').replace(')', '').split(', ')
    
    # Format the date as 'month/day/year'
    formatted_date = f"{month}/{day}/{year}"
    
    return formatted_date

final_numbers = []
starting_dates = monthly_starting_dates

try:
    # Connect to the database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Execute a read-only query
 
    for i in range(len(starting_dates) - 1):
        query = make_query(starting_dates[i], starting_dates[i+1])
        print(f"query for index {i}")
        print(query)
        cursor.execute(query)

        # Fetch the results
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)
            final_numbers.append(row[0])

except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL database: {e}")

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("final numbers:")
    print(final_numbers)
    for i in range(len(starting_dates) - 1):
        print(convert_date_string(starting_dates[i]) + ',' + str(final_numbers[i]))
    
