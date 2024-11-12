# Data Analysis of Coursera Course Data: Focus on Python Visualization

**Overview**
This project, titled **"coursera_course_project"**, presents an exploratoyr analysis of Coursera courses. It leverages a dataset sourced from Kaggle, consisting of 890 observations, where each row represents a course and columns represent various attributes associated with the courses. The analysis aims to answer key questions: which Coursera courses and attributes are the most popular, and which courses are worth investing in to attract more students?

**Features**
- **Course Title**: The title of the course.
- **Course Organization**: The organization offering the course.
- **Course Certificate Type**: Details on the different types of certifications available.
- **Course Rating**: The ratings associated with each course.
- **Course Difficulty**: The difficulty level of the course.
- **Course Students Enrolled**: The number of students enrolled in each course.

**Dataset Limitations**

It's important to note that the dataset does not include date information, which limits the analysis as we cannot ascertain when specific courses started or their availability duration.

**Code Structure**

The core analysis is contained within the coursera_course_project.ipynb file. The code is organized into sections for data loading, data cleaning, exploration, conclusions, and further analysis recommendations.

**Project Setup and Execution**

The project is structured as a Jupyter Notebook, utilizing the following libraries:
- `pandas`: For data manipulation and analysis.
- `numpy`: For numerical operations.
- `seaborn`: For data visualization.
- `plotly`: For interactive visualizations.
- `cufflinks`: For integrating Plotly with Pandas.

To set up and execute the project, follow these steps:

Environment: Ensure you are using the cs50dev environment with Python and Jupyter Notebook installed.

Dataset: Download the dataset from Kaggle: Coursera Course Dataset.

Notebook: Open the Jupyter Notebook titled "coursera_course_project" and run the code cells in order.

Analysis: Review the analysis questions addressed within the notebook to gain insights into course popularity and potential student enrollment.

By following these steps, you will be able to replicate the analysis and draw your conclusions regarding the courses on Coursera.


The analysis begins with importing necessary libraries and setting up the Jupyter environment:
```python
import kagglehub
import pandas as pd
import numpy as np
import os
import seaborn as sns
import plotly.express as px
import cufflinks as cf

%matplotlib inline
