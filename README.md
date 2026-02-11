# Earthquake Data Analysis Using Python and MySQL

**Technologies Used**
- Python
- Pandas
- MySQL
- MySQL Connector
- Matplotlib
  
**Project Structure**
Earthquake-Data-Analysis/
│
├── database.csv        # Raw earthquake dataset
├── config.py           # Database configuration
├── db_setup.py         # Database creation and data insertion
├── data_analysis.py    # Data analysis and visualization
└── README.md

**How the Project Works**
1. Earthquake data is read from a CSV file.
2. Cleaned data is inserted into a MySQL database.
3. Data is retrieved using SQL queries.
4. Statistical analysis is performed on depth and magnitude.
5. Visualizations are generated to identify trends.

**Setup Instructions**
Step 1: Install Required Libraries
 pip install pandas mysql-connector-python matplotlib
Step 2: Create Database in MySQL
CREATE DATABASE earthquake_db;
Step 3: Update Database Credentials
Edit config.py and update:
host
user
password
database
Step 4: Run Database Setup Script
python db_setup.py
Step 5: Run Data Analysis
python data_analysis.py




 
