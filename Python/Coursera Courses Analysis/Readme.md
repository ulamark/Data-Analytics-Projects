# Data Analysis of Coursera Course Data: Focus on Python Visualization

**Overview**

This project, titled **"coursera_course_project"**, presents an exploratory analysis of Coursera courses. It leverages a dataset sourced from Kaggle, consisting of 890 observations, where each row represents a course and columns represent various attributes associated with the courses. The analysis aims to answer key questions: which Coursera courses and attributes are the most popular, and which courses are worth investing in to attract more students?

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

## Conclusions and Further Analysis Recommendations

**Summary:** 

**Main Analysis Questions:** Which Coursera courses and attributes are the most popular, and which courses are worth investing in to attract more students?

The analysis of Coursera course data reveals that certain courses, identified as outliers, are highly popular in terms of student enrollment. **The top course, "Machine Learning," has 3.2M  students, followed by "The Science of Well-Being" with 2.5M, and "Python for Everybody" with 1.5M.** Notably, there are two versions of "Machine Learning" offered with different difficulty levels, certification types, and universities, each drawing significantly more students than the upper threshold of 220k enrollments.

**Six of the top 10 courses relate to IT topics such as AI and programming**, with the remainder covering well-being, language skills, and career development. However, due to the lack of data on course launch dates, these popularity comparisons may be influenced by course duration on the platform. Based on the available data, a substantial portion of popular topics are in the IT sector.

**Course ratings analysis** shows a median rating of 4.7. Among the highest-rated courses (scoring 5), "Infectious Disease Modelling" and "The Lawyer of the Future" each have fewer enrollments (1,500–1,600 students). With varied attributes among top-rated courses, no clear trend explains why some courses are more popular or investment-worthy based on ratings alone.

**The relationship between course ratings and student enrollment shows a very weak correlation of 0.07.** While most courses have high ratings, their enrollment varies widely, from 1.5k to over 3M students.

**Course Attributes Analysis: Among the 888 courses analyzed, the majority (487) are beginner-level**, with intermediate and mixed levels at 198 and 187, respectively, and advanced courses at just 19. **Despite this, the mixed-level courses have the highest average enrollments (133k students)**, suggesting that although most courses are beginner-focused, the mixed level attracts more students per course on average.

**Certification Types Analysis** shows that most courses are general, followed by specializations, with professional certificates making up only 1.35% of courses. However, **professional certificate courses are not unpopular; they attract high enrollments on average**. Since specializations and regular courses offer a broader range of options, their average enrollments are somewhat lower due to greater variation across student distribution.

Here are some suggestions how this analysis can be improved and further implemented:
- For a deeper analysis and stronger conclusions, it is important to examine the start dates of specific courses. This would help determine whether the high enrollment numbers in popular courses are due to their longevity or other factors.
- Additionally, a year-by-year comparison of all courses or specific ones within set time boundaries could provide further insights.

## Installation Guide

To replicate this project, follow these steps to set up the environment and install necessary libraries:

**1. Environment Setup**

Ensure you have the cs50dev environment installed. You can set up a Python environment with Jupyter Notebook by using Anaconda or another environment manager of your choice.

If using conda, you can create the environment with:

`bash
Copy code
conda create -n cs50dev python=3.9
conda activate cs50dev`

**2. Install Required Libraries**

You will need to install the following Python libraries to run the project:

`numpy` for numerical operations.
`pandas` for data manipulation and analysis.
`seaborn` for data visualization.
`plotly` for interactive visualizations.
`cufflinks` for integrating Plotly with Pandas.
`kagglehub` for accessing datasets from Kaggle.
Run the following commands to install the necessary libraries:

`bash
Copy code
pip install os numpy pandas seaborn plotly cufflinks kagglehub`

**3. Dataset Setup**

The dataset is automatically downloaded through `kagglehub` in the Jupyter notebook. The code will download the "Coursera Course Dataset" from Kaggle when executed.

**4. Running the Project**

Once the environment is set up and libraries are installed, follow these steps:

Open the Jupyter Notebook: Launch Jupyter Notebook and open the `coursera_course_project.ipynb` file.

Execute the Code Cells: Run the code cells in order. The first cell imports the necessary libraries and sets up the environment. The second cell downloads the dataset using kagglehub and loads it into a Pandas DataFrame.
