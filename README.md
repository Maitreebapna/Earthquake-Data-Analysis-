# Earthquake-Data-Analysis-
> Description of Files
**database.csv**
Contains raw earthquake data including:
-Date
-Latitude
-Longitude
-Depth
-Magnitude

**config.py**
Stores MySQL database configuration details such as:
-Host
-Username
-Password
-Database name

**db_setup.py**
Responsible for:
-Reading earthquake data from database.csv
-Cleaning and formatting the data
-Creating a MySQL table named earthquakes
-Inserting cleaned data into the database

**data_analysis.py**
Performs data analysis by:
-Fetching data from the MySQL database
-Calculating statistics like:
  -Mean depth
  -Maximum and minimum magnitude
-Analyzing earthquakes per year
-Categorizing earthquakes by depth range
-Displaying:
  -Top 5 deepest earthquakes
  -Top 5 most powerful earthquakes
-Generating visualizations using Matplotlib

**Technologies Used**
-Python
-Pandas
-MySQL
-MySQL Connector
-Matplotlib

>**Prerequisites**
Make sure you have the following installed:
  Python 3.x
  MySQL Server


_**How to Run the Project**__
1. Clone the repository
  git clone <your-repository-link>
