# HostU Administrative Dashboard

## Overview
HostU Administrative Dashboard is a tool designed for non-technical business administrators to access important user data and gain analytical insights. By allowing users to make requests in plain English, the tool uses a large language model (LLM) to translate queries into SQL, retrieve data, and display it in a readable format. This eliminates the need for SQL knowledge, while also offering the option to directly write SQL queries for advanced users.

## Features
### Navigation
A consistent top nav bar allows users to quickly access the dashboard, query pages, user guide, and account details.

### Dashboard
A landing page that displays major KPIs with customizable charts, helping business administrators track metrics like user engagement and revenue at a glance.

### Query Interface
#### LLM Queries
Users can describe the data they want in plain English, and the tool will automatically generate SQL code, run the query, and display the results.

#### Saved Queries
Users can access and run previously saved queries, modify their titles, or edit SQL directly.

#### SQL Queries
For advanced users, the SQL query page allows manual SQL entry to query the relational database.

### Account Details
View account information such as name, username, signup date, and session history.

### User Guide
A navigable guide to help users understand how to use the tool effectively.

## Project Structure
- **Backend**: Built with Flask, utilizing session cookies for security.
- **Routes**: Defined in the `routes` folder and imported to `app.py`.
- **Model Files**: Located in the `scripts` folder, handling backend logic such as database connections, dashboard data calculations, and API integration.

## LLM Integration
The tool uses the OpenAI API to interpret plain English queries, making data retrieval simple and intuitive for non-technical users.
