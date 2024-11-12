# AN ANALYSIS OF TOP 50 SPOTIFY TRACKS IN 2020

**Overview**

This project focuses on analyzing the top 50 most popular Spotify tracks in 2020. The goal is to explore key features such as song duration, popularity, danceability, and other musical attributes using data analytics techniques. This analysis provides insights into trends and patterns in popular music during 2020.

**Features**

Data Exploration: Cleaning and organizing the dataset of top 50 tracks.
Descriptive Analysis: Summary statistics of key musical features.
Graphics: Graphical representations of trends such as popularity vs. energy, danceability vs. tempo, etc.
Insights: Discoveries about the relationship between audio features and song genre.

**Code Structure**

The core analysis is contained within the spotify_project.ipynb file.
The code is organized into sections for data loading, data cleaning, exploration, and conclusions.

**Project Setup and Execution**

Prerequisites
Ensure you have Python installed on your machine (version 3.6 or later is recommended).
You'll need the following Python libraries: pandas, numpy, os, and kagglehub.

1. Clone this repository to your local machine:
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
2. It’s recommended to create a virtual environment for this project. You can set it up as follows:
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
3. Install the necessary dependencies:
pip install pandas numpy os kagglehub
4. The kagglehub library may require authentication with the Kaggle API. You can follow these steps:
Sign in to your Kaggle account and go to My Account.
Scroll to the API section and select Create New API Token. A file named kaggle.json will be downloaded.
Place kaggle.json in the ~/.kaggle/ directory on Unix or %USERPROFILE%\.kaggle\ on Windows.
5. Open the Jupyter Notebook file:
jupyter notebook spotify_project.ipynb
6. Run the notebook cell by cell to execute the analysis. Outputs will be displayed directly in the notebook.
