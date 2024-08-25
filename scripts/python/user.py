import csv

# Path to the CSV file storing user data
USER_CSV_FILE = 'data/users.csv'


# Utility function to read users from the CSV file
def read_users():
    users = []
    try:
        with open(USER_CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append(row)
    except FileNotFoundError:
        pass
    return users


# Utility function to write a new user to the CSV file
def write_user(id, username, password, db_username='', db_password='', name='', title=''):
    with open(USER_CSV_FILE, mode='a', newline='') as file:
        fieldnames = ['id', 'username', 'password', 'db_username', 'db_password', 'name', 'title']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write the header if the file is empty
        if file.tell() == 0:
            writer.writeheader()
        
        writer.writerow({'id': id,
                         'username': username,
                         'password': password,
                         'db_username': db_username,
                         'db_password': db_password,
                         'name': name,
                         'title': title })


# Utility function to find a user by username
def find_user_by_username(username):
    users = read_users()
    for user in users:
        if user['username'] == username:
            return user
    return None


#Utility function to find a user by id
def find_user_by_id(user_id):
    users = read_users()
    for user in users:
        if user['id'] == user_id:
            return user
    return None


# Sample user creation for testing
# if not find_user_by_username('ip.d@northeastern.edu'):
#     hashed_pw = bcrypt.hashpw('hostu2'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
#     id = str(uuid.uuid4())
#     write_user(id, 'ip.d@northeastern.edu', hashed_pw)


class User:
    def __init__(self, username, password, db_username, db_password, name, title):
        self.id = '1'
        self.username = username
        self.password = password
        self.db_username = db_username
        self.db_password = db_password
        self.name = name
        self.title = title

