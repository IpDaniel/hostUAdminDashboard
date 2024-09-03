import csv
from datetime import datetime

# File path to the CSV file
csv_file_path = 'data/queries.csv'


# """Get a query from the CSV file using its unique name."""
def get_query_by_name(unique_name):
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['uniqueName'] == unique_name:
                return row
    return None


# """Get a query from the CSV file using its unique name and creator"""
def get_query_by_name_and_creator(unique_name, creator_id):
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['uniqueName'] == unique_name and row['creatorId'] == creator_id:
                return row
    return None


# """Get a list of all queries created by a user with the given creator ID."""
def get_queries_by_creator(creator_id):
    queries = []
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['creatorId'] == str(creator_id):
                queries.append(row)
    return queries


# """Write a new query to the CSV file."""
def write_new_query(unique_name, creator_id, query_text, plaintext_prompt="", created_at=None, last_used=None):
    created_at = created_at or datetime.now().isoformat()
    last_used = last_used or ''
    existing_query_with_this_name = get_query_by_name(unique_name)
    if (existing_query_with_this_name and existing_query_with_this_name['creatorId'] == creator_id):
        raise NameError("Already a query with this name made by this user")
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['uniqueName', 'creatorId', 'queryText', 'plaintextPrompt', 'createdAt', 'lastUsed'])
        writer.writerow({
            'uniqueName': unique_name,
            'creatorId': creator_id,
            'queryText': query_text,
            'plaintextPrompt': plaintext_prompt,
            'createdAt': created_at,
            'lastUsed': last_used
        })


# """Update the 'lastUsed' timestamp for a query by its unique name and creatorId"""
def update_last_used(unique_name, creator_id):
    updated = False
    rows = []
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['uniqueName'] == unique_name and row['creatorId'] == creator_id:
                row['lastUsed'] = datetime.now().isoformat()
                updated = True
            rows.append(row)
    
    if updated:
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['uniqueName', 'creatorId', 'queryText', 'plaintextPrompt', 'createdAt', 'lastUsed'])
            writer.writeheader()
            writer.writerows(rows)


# """Delete a query from the CSV file by its unique name and creator Id"""
def delete_query_by_name_and_creator(unique_name, creator_id):
    rows = []
    deleted = False
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['uniqueName'] != unique_name or row['creatorId'] != creator_id:
                rows.append(row)
            else:
                deleted = True

    if deleted:
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['uniqueName', 'creatorId', 'queryText', 'plaintextPrompt', 'createdAt', 'lastUsed'])
            writer.writeheader()
            writer.writerows(rows)


# Returns all queries created by the user with the given id from the csv file with the given path 
def filter_csv_by_creator(creator_id, file_path='data/queries.csv'):
    """
    Parses through the queries file and returns a list of dictionaries for rows where creatorId matches the specified creator_id.

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


# """Edit an existing query in the CSV file by its unique name and creator ID."""
def edit_query(current_name, creator_id, new_title=None, plaintext_prompt=None, query_text=None):
    """
    Edits an existing query in the CSV file by its unique name and creator ID.

    Args:
    - current_name (str): The current unique name of the query to edit.
    - creator_id (str): The creator's ID associated with the query.
    - new_title (str, optional): New title for the query.
    - plaintext_prompt (str, optional): Updated plaintext prompt for the query.
    - query_text (str, optional): Updated SQL query text.

    Returns:
    - bool: True if the query was updated successfully, False otherwise.
    """
    updated = False
    rows = []

    # Read the current contents of the CSV file
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # If the specific query is found, update its fields
            if row['uniqueName'] == current_name and row['creatorId'] == str(creator_id):
                if new_title is not None:
                    row['uniqueName'] = new_title
                if plaintext_prompt is not None:
                    row['plaintextPrompt'] = plaintext_prompt
                if query_text is not None:
                    row['queryText'] = query_text
                row['lastUsed'] = datetime.now().isoformat()  # Update the 'lastUsed' timestamp
                updated = True
            rows.append(row)

    # If the query was updated, write back to the CSV file
    if updated:
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['uniqueName', 'creatorId', 'queryText', 'plaintextPrompt', 'createdAt', 'lastUsed'])
            writer.writeheader()
            writer.writerows(rows)
    
    return updated



# Example usage
# write_new_query('example_query', 1, 'SELECT * FROM users', 'Fetch all users')
# print(get_query_by_name('example_query'))
# print(get_queries_by_creator(1))
# update_last_used('example_query')
# delete_query_by_name('example_query')
