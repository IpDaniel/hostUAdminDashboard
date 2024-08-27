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


# """Update the 'lastUsed' timestamp for a query by its unique name."""
def update_last_used(unique_name):
    updated = False
    rows = []
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['uniqueName'] == unique_name:
                row['lastUsed'] = datetime.now().isoformat()
                updated = True
            rows.append(row)
    
    if updated:
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['uniqueName', 'creatorId', 'queryText', 'plaintextPrompt', 'createdAt', 'lastUsed'])
            writer.writeheader()
            writer.writerows(rows)


# """Delete a query from the CSV file by its unique name."""
def delete_query_by_name(unique_name):
    rows = []
    deleted = False
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['uniqueName'] != unique_name:
                rows.append(row)
            else:
                deleted = True

    if deleted:
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['uniqueName', 'creatorId', 'queryText', 'plaintextPrompt', 'createdAt', 'lastUsed'])
            writer.writeheader()
            writer.writerows(rows)


# Example usage
# write_new_query('example_query', 1, 'SELECT * FROM users', 'Fetch all users')
# print(get_query_by_name('example_query'))
# print(get_queries_by_creator(1))
# update_last_used('example_query')
# delete_query_by_name('example_query')
