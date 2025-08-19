# Streamlit - Worldwide Analysis of Quality of Life and Economic Factors

## Overview
This interactive Streamlit app enables you to explore relationships between **Healthy Life Expectancy**, **GDP per capita**, and **Poverty rates** across countries and years.  
It includes:
- **Key metrics dashboard** per selected year.
- **Scatterplots and line charts** to visualize trends.
- **Interactive map** of countries.
- **Machine learning model** (RandomForestRegressor) to predict life expectancy.
- **Data explorer** with download option.

---

## Project Structure
Streamlit/
│
├── app.py                      # main Streamlit app
├── config.py                   # constants, config vars
├── data.py                     # data loading and preprocessing
├── model.py                    # train/load model, feature importance
├── plots.py                    # plotting functions
├── requirements.txt
├── README.md
└── rf_model.pkl                # trained model

---

## Installation

**1. Clone the repository**
git clone https://github.com/nzelinska-job/Streamlit.git
cd Streamlit


**2. Create and activate a virtual environment (optional)**
pip install -r requirements.txt


---

## Usage

**Run the Streamlit app**

streamlit run app.py



## Model Training

The model is trained locally and saved to `rf_model.pkl`:



---

## Data Source
Dataset is loaded from:
https://raw.githubusercontent.com/JohannaViktor/streamlit_practical/refs/heads/main/global_development_data.csv


---

## Author
Developed by [nzelinska-job].
