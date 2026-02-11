# Earthquake Data Analysis Using Python and MySQL

## Description
This project focuses on analyzing earthquake data by storing it in a MySQL database and performing statistical analysis and visualizations using Python. The project helps in understanding earthquake patterns based on magnitude, depth, and yearly occurrences.

---

## Technologies Used
- Python  
- Pandas  
- MySQL  
- MySQL Connector  
- Matplotlib  

---

## Project Structure
Earthquake-Data-Analysis/
│
├── database.csv 
├── config.py 
├── db_setup.py 
├── data_analysis.py 
└── README.md

---

## How the Project Works
1. Earthquake data is read from a CSV file.
2. Data is cleaned using Pandas.
3. Cleaned data is inserted into a MySQL database.
4. Data is retrieved using SQL queries.
5. Statistical analysis is performed on earthquake depth and magnitude.
6. Visualizations are generated to identify trends and patterns.

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Maitreebapna/Earthquake-Data-Analysis.git
cd Earthquake-Data-Analysis

### 2. Install Required Libraries
Make sure Python is installed on your system. Then install the required Python libraries using pip:

```bash
pip install pandas mysql-connector-python matplotlib

### 3.Create Database in MySQL
CREATE DATABASE earthquake_db;

### 4. Configuration
db_config = {
    'host': 'localhost',
    'user': 'your_username',  # Replace with your MySQL username
    'password': 'your_password',  # Replace with your MySQL password
    'database': 'earthquake_db'
}

### 5. Initialization
python db_setup.py

### 6. Execution
python data_analysis.py



