# Simple House Price Predictor

Live demo: https://dngphuu-simple-house-price-predictor.streamlit.app/

A small Streamlit app and trained model that predict house prices using a linear regression model. This repository contains the minimal code and serialized model artifacts needed to run the app locally or inspect the model.

## Features

- Web UI built with Streamlit (`app.py`) for entering house features and getting a price prediction.
- Pre-trained linear regression model saved as `linear_regression_model.pkl` and the model's expected column order in `model_columns.pkl`.
- Lightweight `model.py` module that loads the model and exposes prediction logic.

## Repository structure

- `app.py` — Streamlit application that serves the web UI.
- `model.py` — Helper functions to load the model and make predictions.
- `linear_regression_model.pkl` — Serialized scikit-learn model used for predictions.
- `model_columns.pkl` — Pickled list/array describing the feature column order expected by the model.
- `requirements.txt` — Python dependencies.
- `README.md` — This file.

## Requirements

- Python 3.8+ (recommended)
- pip

Install dependencies:

```cmd
pip install -r requirements.txt
```

## Run the app (Windows cmd)

1. (Optional) Create and activate a virtual environment:

```cmd
python -m venv venv
venv\Scripts\activate
```

2. Install requirements if you haven't already:

```cmd
pip install -r requirements.txt
```

3. Start the Streamlit app:

```cmd
streamlit run app.py
```

This will open a local web UI where you can interactively enter house features and see predicted prices. You can also visit the live deployed app at the link above.

## Quick usage (programmatic)

If you prefer to use the model programmatically, `model.py` exposes functions to load the model and predict given a feature vector or a pandas DataFrame. Typical steps:

1. Load the model (example inside `model.py`).
2. Prepare input features in the same columns and order as `model_columns.pkl`.
3. Call the prediction function to get numeric results.

Note: Always make sure your input columns match the trained model's expected columns (names and order), otherwise predictions may be incorrect or fail.

## FAQ / Troubleshooting

Q: What does `df.head()` do?

A: `df.head()` is a pandas DataFrame method that returns the first 5 rows of the DataFrame by default (you can pass an integer like `df.head(10)` to get the first 10 rows). It's useful to quickly inspect the top rows and column names.

Q: When I run `df.head()` in my script it shows nothing in the terminal — why?

A: Common reasons and fixes:

- In a Python script run from the terminal, `df.head()` by itself doesn't print to stdout. You need to explicitly print the result: `print(df.head())`.
- In an interactive environment like Jupyter Notebook or IPython, simply writing `df.head()` will render a nice table. In plain `python` executed from the terminal you must use `print()`.
- The DataFrame might be empty. Check `print(df.shape)` or `print(df.empty)` to confirm.
- If your code runs in a web app (Streamlit, Flask, etc.), stdout might not be visible in the browser — use the app's UI or logger to display values (for Streamlit use `st.write(df.head())`).

Q: I see an error loading the model or columns pickle files — how to debug?

- Ensure `linear_regression_model.pkl` and `model_columns.pkl` exist in the project root.
- Confirm the Python environment has the same major library versions used to create the model (scikit-learn, pandas, etc.).
- If you get an unpickle error, the file may be corrupted or was created with an incompatible library version.

## Notes & Next steps

- If you modify the model or retrain, update `linear_regression_model.pkl` and `model_columns.pkl` accordingly.
- Consider adding unit tests for `model.py` and a CI workflow for automatic checks.
