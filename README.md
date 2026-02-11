# Earthquake Data Analysis

A data analysis project built with Python and Jupyter Notebooks to explore, clean, and visualize global earthquake data, identifying seismic patterns and trends.

## Features

* **Data Cleaning & Preprocessing:** Handles missing values, converts date/time formats, and filters irrelevant data points (e.g., nuclear explosions) to ensure dataset integrity.
* **Exploratory Data Analysis (EDA):** Statistical summaries of earthquake magnitudes, depths, and frequencies over time.
* **Geospatial Visualization:** Interactive world maps using **Folium** to plot earthquake epicenters, with markers color-coded by magnitude or depth.
* **Temporal Analysis:** Visualizes seismic activity trends over years, months, and days to identify seasonal or long-term patterns.
* **Depth vs. Magnitude Analysis:** Scatter plots and correlation matrices to investigate the relationship between the depth of the hypocenter and the earthquake's magnitude.
* **Category Classification:** Categorizes earthquakes into classes (e.g., Minor, Light, Moderate, Strong, Major, Great) based on the Richter scale.
* **Static Visualizations:** Generates high-quality bar charts, histograms, and heatmaps using **Matplotlib** and **Seaborn**.

## Prerequisites

* Python 3.x
* `pip` (Python package installer)
* Jupyter Notebook or JupyterLab
* Basic understanding of Data Science libraries (Pandas, NumPy)

## Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Maitreebapna/Earthquake-Data-Analysis-](https://github.com/Maitreebapna/Earthquake-Data-Analysis-)
    cd Earthquake-Data-Analysis-
    ```

2.  **Create and Activate Virtual Environment:**
    * It's highly recommended to use a virtual environment to manage dependencies.
    ```bash
    # Create the environment (e.g., named .venv)
    python -m venv .venv

    # Activate it:
    # On Linux/macOS:
    source .venv/bin/activate
    # On Windows (Command Prompt):
    # .venv\Scripts\activate.bat
    # On Windows (PowerShell):
    # .venv\Scripts\Activate.ps1
    ```

3.  **Install Dependencies:**
    * Install the required Python libraries.
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt` file yet, run: `pip install pandas numpy matplotlib seaborn folium jupyter`)*

## Running the Analysis

1.  **Ensure Virtual Environment is Active:** If not already active, run the activation command from the setup step.
2.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
3.  **Open the Project File:**
    * In the browser window that opens, navigate to the project folder.
    * Click on the main notebook file (e.g., `Earthquake_Analysis.ipynb` or `main.ipynb`) to open it.

## Usage

1.  **Load the Data:** Run the initial cells to import libraries and load the earthquake dataset.
2.  **Run Analysis Cells:** Execute the cells sequentially to perform data cleaning and generate visualizations.
    * **View Statistics:** See the `.describe()` and `.info()` outputs for a data overview.
    * **View Maps:** Look for the interactive Folium map outputs where you can zoom and click on earthquake markers.
    * **View Plots:** Analyze the generated histograms and scatter plots to understand the distribution of earthquake magnitudes.
3.  **Export Results:**
    * Interactive maps can often be saved as HTML files (e.g., `earthquake_map.html`).
    * Static plots can be saved as images using `plt.savefig()`.

## Dataset Information

The project uses a dataset containing historical earthquake records. Key columns typically include:
* **Date/Time:** The exact moment the earthquake occurred.
* **Latitude/Longitude:** The geographic coordinates of the epicenter.
* **Depth:** The depth of the earthquake in kilometers.
* **Magnitude:** The measure of the earthquake's size (Richter/Moment scale).
* **Type:** The type of seismic event (Earthquake, Explosion, etc.).

* **Interactive Maps:** If the interactive maps do not render on GitHub's preview, please clone the repo and run the notebook locally to view them.
* **Data Source:** This analysis is based on public datasets, often sourced from the USGS (United States Geological Survey) or Kaggle.
