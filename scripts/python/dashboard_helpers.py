from datetime import datetime, timedelta
from scripts.python.connect import run_query
from scripts.python.user import get_user_object_by_id
from scripts.python.query import get_query_by_name

# Returns a list of the past 6 days with "Today" as a filler for the seventh day 
def get_past_six_days():
    days_list = []
    today = datetime.today()
    
    # Generate the past 6 days
    for i in range(6):
        day = today - timedelta(days=6-i)
        days_list.append(day.strftime('%A'))  # Convert to string form (e.g., 'Monday')
    
    # Append 'Today' as the last element
    days_list.append('Today')
    
    return days_list


#This one is probably useless feel free to ignore it
#Returns the sql queries necessary to fetch data for new users aquired on each of the past 7 days
def generate_sql_queries():
    queries = []
    today = datetime.today()
    
    # Loop to generate queries for the past 7 days
    for i in range(7):
        # Calculate the start and end date for each query
        start_date = today - timedelta(days=(6 - i))
        end_date = start_date + timedelta(days=1)
        
        # Format the dates in YYYY, M, D format for SQL query
        start_date_str = f"make_date({start_date.year}, {start_date.month}, {start_date.day})"
        end_date_str = f"make_date({end_date.year}, {end_date.month}, {end_date.day})"
        
        # Create the SQL query
        query = (
            f'select count(*) from "User" u '
            f'inner join "ListingPreferences" p on p."userId" = u.id '
            f'where u."createdAt" > {start_date_str} and u."createdAt" < {end_date_str};'
        )
        
        # Add the query to the list
        queries.append(query)
    
    return queries


#Takes a list of queries and turns it into a list of data elements 
def generate_weekly_data(user):
    data = []
    queryText = get_query_by_name('New users by day for last 7 days')['queryText']
    dates_and_numbers = run_query(user=user, queryText=queryText)
    for row in dates_and_numbers:
        data.append(row[1])
    return data