# HostU Administrative Dashboard
### A tool for non-technical business administrators of HostU to use to retrieve important user data and analytical insights 
The purpose of this tool is similar to that of software such as PowerBI or Tableau. Business administrators need to make informed decisions about the companies they run based on data. However, most data is stored in a relational database which requires knowledge of SQL in order to access. This tool allows business administrators to categorize and 
access the data they want by making requests in plain english. The tool will then use a large language model to take the plain english query, create a corresponding SQL query, and run it through the relational database to retrieve the desired data. The tool also contains a Dashboard with a few charts displaying major KPIs, and it has the ability to save previous queries for later, and write new queries directly in SQL.
## Features implemented:
### Navigation
The top nav bar is present almost every page, and it allows the user to route immediately to the queries page, the user guide, their account details, or their home dashboard. The routes and logic for this page linking is managed in [app.py]()
### Dashboard
This is a feature to display a landing page full of major KPI charts to allow business administrators to track certain important metrics more quickly and easily as soon as they enter their account. It contains editable widgets that are connected to saved quieries which make backend requests to fetch data. This feature is displayed in [file](), the routes are routed to [file]() and the processing and retrieval logic is managed mostly in [file]()
### Account Details
This feature allows users to view their account details, including their name, username, the date they signed up, and their session history. The feature is displayed in [file](), and the backend routes and logic are handled in [file]()
### User guide
This is a navigable user guide for the tool that is the same for every user. It is displayed in [file]()
### Queries
This is the heart of the software tool. It is the page where users can actually go to retrieve organized data from the HostU database with their method of choice. It is displayed in [file]()
#### Saved queries
This is where users can run queries that they have previously saved. Results are fetched from the database and returned in table format with headers where they can be saved by the user. User can also make edits to the title of the query, or edit the SQL code directly. Users cannot edit the plain english query that they used to initially generate the query. Displayed primarily in [file](). Backend routes and logic mostly in [file]() and [file]()
#### LLM queries
This is the flagship feature of the tool. It allows users to gather data from the database by describing the data they want to retrieve in plain english, and allowing the tool to generate the SQL code for them, run the SQL query in the database, and return the results to the user so they never have to look at a line of code. The display is in [file]() and the routes and logic are stored mostly in [files]()
#### SQL queries
This is a tool for any technical people who may be using this software who want to query the relational database in the old fashioned way without the use of any special tools to interpret English queries. User interface portion is displayed in [file](). Logic is handled in [files]()
## Project structure
The backend is tied together with the Flask framework in Python. Network security is created with session cookies to secure user connections and ensure that no unwanted access can be granted. The app is initialized in the [app.py]() file and routes are imported from various files in the [routes]() folder. Model functions for handling more complex backend processing functionality are stored in the [scripts]() folder. Currently, user data and query data is stored in csv files (partially omitted from this repo for security purposes), but we plan to migrate to a relational database system once other features have been fully implemented.
### Routes
All routes for communicating between frontend and backend are stored either directly in the app file, or they are stored in a different file in the routes folder, and imported to the app file.
### Model files
Most of the complexities of the app are managed in the [scripts]() folder. This includes the process for connecting to the HostU database, the calculations for dashboard data, API connections, and any other helper functions necessary to allow the application to run. 
## LLM integration
The llm is integrated through the openAI API.
