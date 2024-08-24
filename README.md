# Shelf Life Prediction of Dairy Products

This project implements a predictive model to estimate the remaining shelf life of dairy products based on various environmental and chemical parameters. The model uses machine learning techniques to predict how long a product will remain safe and of high quality before it expires.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Data Exploration](#data-exploration)
  - [Data Preprocessing](#data-preprocessing)
  - [Model Training](#model-training)
  - [Model Evaluation](#model-evaluation)
  - [Model Inference](#model-inference)
- [Model Architecture](#model-architecture)
- [Dependencies](#dependencies)
- [License](#license)

## Project Overview

The goal of this project is to develop a machine learning model to predict the shelf life of dairy products. The model is trained on a dataset containing features such as temperature, pH levels, moisture content, and storage conditions. Predicting shelf life accurately is crucial for minimizing waste and ensuring product safety.

## Dataset

The dataset used in this project is synthesized to simulate the real-world scenario of dairy product shelf life. It includes the following features:

- **Temperature**: Storage temperature in Celsius.
- **pH Level**: Acidity level of the product.
- **Moisture Content**: Percentage of moisture in the product.
- **Storage Conditions**: Categorical data indicating whether the product was stored in optimal or suboptimal conditions.
- **Shelf Life (target)**: The number of days the product remains safe and of high quality.

You can find the dataset in the `data/` directory as `shelf_life_data.csv`.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/shelf_life_prediction.git
    cd shelf_life_prediction
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

```plaintext
shelf_life_prediction/
│
├── data/
│   ├── raw/
│   │   └── shelf_life_data.csv       # Raw dataset for shelf life prediction
│   ├── processed/
│   │   ├── train.csv                 # Preprocessed training data
│   │   ├── val.csv                   # Preprocessed validation data
│   │   └── test.csv                  # Preprocessed test data
│
├── notebooks/
│   └── shelf_life_exploration.ipynb  # Jupyter notebook for data exploration
│
├── src/
│   ├── data_preprocessing.py         # Script for data preprocessing
│   ├── model.py                      # Machine learning model definition
│   ├── train_model.py                # Script to train the predictive model
│   ├── evaluate_model.py             # Script to evaluate the predictive model
│   └── inference.py                  # Script for making predictions on new data
│
├── models/
│   └── shelf_life_model.pkl          # Trained shelf life prediction model
│
├── utils/
│   ├── data_utils.py                 # Utility functions for data handling
│   └── model_utils.py                # Utility functions for model handling
│
├── requirements.txt                  # List of dependencies
└── README.md                         # Project documentation

