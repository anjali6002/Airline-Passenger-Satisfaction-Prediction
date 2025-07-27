# Airline Passenger Satisfaction Prediction

## Project Overview
This project focuses on predicting airline passenger satisfaction (whether they are 'satisfied' or 'neutral/dissatisfied') based on various flight details and service interactions. By identifying key drivers of satisfaction, this model aims to provide actionable insights for airlines to enhance customer experience and operational efficiency.

## Key Features & Technologies
* **Data Analysis & Manipulation:** Python (Pandas, NumPy)
* **Data Visualization:** Matplotlib, Seaborn
* **Machine Learning Model:** XGBoost (for robust classification)
* **Model Interpretability:** SHAP (to explain model predictions)
* **Interactive Demo:** Streamlit (for a user-friendly web application)

## Dataset
The dataset used in this project contains detailed information about airline passengers, including demographics, flight history, service ratings, and their final satisfaction rating.
* `train.csv`: Training data for model development.
* `test.csv`: Independent test data for final model evaluation.
* * **Source:** This dataset was originally obtained from Kaggle (https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction).
  
  
## Project Structure
* `airline passengers satisfaction.ipynb`: The main Jupyter Notebook containing all the code for data loading, EDA, preprocessing, model training, evaluation, and interpretation.
* `app.py`: The Python script for the interactive Streamlit web application.
* `model.pkl`: The trained machine learning model, saved using `pickle`.
* `train.csv`, `test.csv`: The raw datasets.
* `requirements.txt`: Lists all Python dependencies required to run the project.

## Key Findings & Insights
Through comprehensive Exploratory Data Analysis (EDA) and model interpretation using SHAP, we identified the following key drivers of passenger satisfaction:

* **Inflight Wi-Fi Service:** Consistently found to be the **most significant factor** influencing satisfaction.
* **Travel Class (Business vs. Economy/Eco Plus):** Business Class passengers show notably higher satisfaction.
* **Customer Loyalty:** Loyal customers tend to be more satisfied.
* **Total Delay:** Delays negatively impact satisfaction.
* **Flight Distance:** Longer flight distances are generally associated with higher satisfaction.

## Model Performance
The XGBoost model achieved strong performance on unseen data:
* **Test Accuracy:** 84.0%
* **Test ROC AUC:** 0.924

## How to Run the Project Locally

To set up and run this project on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/anjali6002/Airline-Passenger-Satisfaction-Prediction.git](https://github.com/anjali6002/Airline-Passenger-Satisfaction-Prediction.git)
    cd Airline-Passenger-Satisfaction-Prediction
    ```
2.  **Create and Activate Virtual Environment (Recommended):**
    ```bash
    # Using Conda
    conda create -n airline_env python=3.9 # Or your Python version
    conda activate airline_env
    ```
    *(Or using pip venv: `python -m venv venv` and `source venv/bin/activate`)*
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Jupyter Notebook:**
    ```bash
    jupyter notebook
    # Then open 'airline passengers satisfaction.ipynb' in your browser.
    ```
    Run all cells to see the full analysis, model training, and evaluation.
5.  **Run the Streamlit Application:**
    ```bash
    streamlit run app.py
    ```
    This will open the interactive predictor in your web browser.

## Live Demo

Experience the interactive predictor online:
**https://airline-passenger-satisfaction-prediction-k3ntsfrsubfevknkxkmj.streamlit.app/**

