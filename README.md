
# End-to-End Customer Churn Prediction

An end-to-end Machine Learning project that predicts customer churn for a telecommunications company. The project covers data analysis, preprocessing, model training, evaluation, prediction API development, and deployment of a user-friendly web application.

The objective is to help businesses identify customers who are likely to leave and take proactive retention measures.

## 🚀 Live Demo

- **Streamlit Web App:** https://telecom-churn-app-v4k2oxncrzh8ivwfcyiyrp.streamlit.app/
- **FastAPI Backend / API Documentation:** https://end-to-end-customer-churn-hw7x.onrender.com/docs
- **Main GitHub Repository:** https://github.com/Praveen673-ui/end-to-end-customer-churn
- **Streamlit Frontend Repository:** https://github.com/Praveen673-ui/telecom-churn-streamlit

## 📌Project Overview

Customer churn is a major business problem in the telecommunications industry. When customers discontinue their services, businesses lose recurring revenue and may incur additional customer acquisition costs.

This project uses customer demographics, account information, service subscriptions, contract details, and billing information to predict whether a customer is likely to churn.

The trained model is served through a FastAPI backend, while a Streamlit application provides an interactive interface for submitting customer details and viewing predictions.

### Key Features

- Exploratory Data Analysis (EDA)
- Data cleaning and preprocessing
- Feature engineering through preprocessing pipelines
- Comparison of multiple classification algorithms
- Hyperparameter tuning using GridSearchCV
- Classification threshold evaluation
- Final model selection and evaluation
- Model serialization using Joblib
- REST API development using FastAPI
- Interactive frontend using Streamlit
- Cloud deployment of the API and web application
- Local setup instructions for reproducing the project

## 🛠️Tech Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib |
| Machine Learning | Scikit-learn |
| Algorithms | Logistic Regression, Random Forest, and other baseline models |
| Model Tuning | GridSearchCV, cross-validation |
| Model Serialization | Joblib |
| Backend API | FastAPI, Pydantic, Uvicorn |
| Frontend | Streamlit |
| API Requests | Requests |
| Development | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |
| Deployment | Render, Streamlit Community Cloud |

## Dataset

The project uses a telecommunications customer churn dataset containing **7,043 customer records and 21 columns**.

The data includes customer demographics, services, account details, contract information, and billing attributes.

### Important Features

| Feature | Description |
|---|---|
| customerID | Unique customer identifier |
| gender | Customer gender |
| SeniorCitizen | Indicates whether the customer is a senior citizen |
| Partner | Whether the customer has a partner |
| Dependents | Whether the customer has dependents |
| tenure | Number of months the customer has stayed |
| InternetService | Type of internet service |
| Contract | Customer contract type |
| PaymentMethod | Customer payment method |
| MonthlyCharges | Monthly service charges |
| TotalCharges | Total charges accumulated |
| Churn | Target variable indicating customer churn |

**Target variable:** `Churn`

- `Yes` — the customer churned.
- `No` — the customer did not churn.

The dataset contains customer information used for model development. The original dataset file is not included in the main repository structure shown below; use the dataset source or the notebook's existing data-loading instructions to reproduce the analysis.

## 🔄Machine Learning Workflow

1. **Data understanding:** Inspect the dataset dimensions, data types, target distribution, and feature relationships.
2. **Data cleaning:** Handle whitespace, convert `TotalCharges` to a numeric data type, and address blank values associated with zero-tenure customers.
3. **Exploratory Data Analysis:** Investigate churn patterns across customer tenure, contract type, services, and billing attributes.
4. **Train-validation-test split:** Split the data into stratified training, validation, and test sets using a 60:20:20 ratio.
5. **Preprocessing:** Use median imputation and standard scaling for numeric features, and most-frequent imputation and one-hot encoding for categorical features.
6. **Model comparison:** Evaluate baseline and candidate classification algorithms.
7. **Hyperparameter tuning:** Use GridSearchCV with three-fold cross-validation to tune Logistic Regression and Random Forest.
8. **Threshold evaluation:** Compare classification thresholds between 0.30 and 0.60 to study the trade-off between precision and recall.
9. **Final model selection:** Select the tuned Logistic Regression pipeline with a decision threshold of 0.55.
10. **Model serialization:** Save the fitted pipeline, threshold, and target mapping using Joblib.
11. **API development:** Load the saved artifact and expose a prediction endpoint through FastAPI.
12. **Frontend development:** Build a Streamlit interface that sends customer information to the API and displays the prediction and churn probability.
13. **Deployment:** Host the backend on Render and the frontend on Streamlit Community Cloud.

## 📈Model Evaluation

The final model selection prioritizes identifying customers who are likely to churn. Recall is particularly important because a false negative represents a customer who actually churns but is predicted not to churn.

The following are the reported test-set results from the notebook.

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 75.6% | 77.4% |
| Precision | 52.9% | 56.0% |
| Recall | 74.3% | 69.8% |
| F1-score | 61.9% | 62.2% |
| Actual churners missed | 96 | 113 |

### Why Logistic Regression Was Selected

Random Forest achieved slightly higher accuracy, precision, and F1-score in the reported comparison. However, Logistic Regression achieved higher recall and missed fewer actual churners.

For a customer retention use case, identifying more customers who may leave can be valuable because the business can investigate and offer targeted retention measures.

The tuned Logistic Regression pipeline was therefore selected as the final model, using a decision threshold of **0.55**.

These metrics describe the evaluated test data. Actual business performance will depend on customer behavior, the quality of new input data, and the effectiveness of retention actions.

## 🏗️System Architecture

```text
          Customer
              |
              v
     Streamlit Web App
              |
              | Customer details (JSON)
              v
       FastAPI Backend
              |
              v
    Saved ML Model Pipeline
       + Decision Threshold
              |
              v
      Churn Prediction
              |
              v
    Probability + Result
              |
              v
      Streamlit Interface
```

### How the Application Works

1. The user enters customer information in the Streamlit application.
2. Streamlit sends the information as a JSON request to the FastAPI `/predict` endpoint.
3. FastAPI validates the input and loads the saved model artifact.
4. The model pipeline applies the required preprocessing and generates a churn probability.
5. The configured decision threshold is applied to produce the prediction.
6. The API returns the prediction and probability to the frontend.
7. Streamlit displays the result to the user.

## 📁 GitHub Repository Structure

### Main Machine Learning and API Repository

```text
end-to-end-customer-churn/
├── Customer_Churn_CodeFile.ipynb
├── app.py
├── churn_model.joblib
├── requirements.txt
├── python-version
└── README.md
```

| File | Purpose |
|---|---|
| `Customer_Churn_CodeFile.ipynb` | Data analysis, preprocessing, model comparison, tuning, evaluation, and model development |
| `app.py` | FastAPI backend and prediction endpoints |
| `churn_model.joblib` | Saved model pipeline, threshold, and target mapping |
| `requirements.txt` | Python dependencies for the backend |
| `python-version` | Python runtime version configuration |
| `README.md` | Project documentation |

### Separate Streamlit Frontend Repository

```text
telecom-churn-streamlit/
├── streamlit_app.py
├── requirements.txt
└── README.md
```

| File | Purpose |
|---|---|
| `streamlit_app.py` | User interface and API request handling |
| `requirements.txt` | Streamlit and Requests dependencies |
| `README.md` | Frontend setup and deployment documentation |

## ⚙️Run the Project Locally

You can run the FastAPI backend and Streamlit frontend on your own computer. They are maintained in **two separate GitHub repositories**, so you need to open both project folders.

### Prerequisites

Install the following:

- Python 3.11
- Git
- Visual Studio Code (recommended)
- Internet connection for installing dependencies

### Where to Paste the Commands

Run the following commands in the **VS Code terminal**, not inside a Python file or a Jupyter Notebook cell.

1. Open Visual Studio Code.
2. Select **Terminal → New Terminal**.
3. Paste the commands for the relevant project into that terminal.
4. Keep the terminal open while the application is running.

The commands below are written for Windows PowerShell.

### Step 1: Run the FastAPI Backend Locally

**1. Clone the main repository**

Open a terminal and run:

```bash
git clone https://github.com/Praveen673-ui/end-to-end-customer-churn.git
```

**2. Move into the project folder**

```bash
cd end-to-end-customer-churn
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

```bash
venv\Scripts\Activate.ps1
```

If you are using Command Prompt instead of PowerShell, run:

```bat
venv\Scripts\activate.bat
```

**5. Install the dependencies**

```bash
python -m pip install -r requirements.txt
```

**6. Start the FastAPI server**

```bash
uvicorn app:app --reload
```

**7. Open the API documentation**

Visit:

http://127.0.0.1:8000/docs

You can use the interactive Swagger documentation to inspect the endpoints and test predictions.

**Important:** Keep this terminal running while using the local API. Make sure `churn_model.joblib` is present in the project directory.

### Step 2: Run the Streamlit Frontend Locally

Open a **second terminal** in VS Code, or open a second VS Code window.

**1. Clone the frontend repository**

```bash
git clone https://github.com/Praveen673-ui/telecom-churn-streamlit.git
```

**2. Move into the frontend folder**

```bash
cd telecom-churn-streamlit
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

```bash
venv\Scripts\Activate.ps1
```

**5. Install the frontend dependencies**

```bash
python -m pip install -r requirements.txt
```

**6. Start Streamlit**

```bash
python -m streamlit run streamlit_app.py
```

**7. Open the web application**

Visit:

http://localhost:8501

Streamlit will display the frontend in your browser.

### Step 3: Connect Streamlit to the Local API

The frontend is configured to use the deployed API by default:

```python
API_URL = "https://end-to-end-customer-churn-hw7x.onrender.com/predict"
```

To send predictions to the FastAPI backend running on your own computer, change this line in `streamlit_app.py` to:

```python
API_URL = "http://127.0.0.1:8000/predict"
```

Save the file and restart Streamlit if necessary.

For local integration, keep both services running:

| Terminal | Application | Address |
|---|---|---|
| Terminal 1 | FastAPI backend | `http://127.0.0.1:8000` |
| Terminal 2 | Streamlit frontend | `http://localhost:8501` |

If you only want to test the frontend against the deployed backend, you can leave the deployed `API_URL` unchanged. In that case, the local FastAPI server is not required.

### Troubleshooting

**Python is not recognized**

Install Python 3.11 and ensure it is added to your system PATH. On Windows, you can also try using `py` instead of `python`.

**Dependencies are missing**

Activate the appropriate virtual environment and run:

```bash
python -m pip install -r requirements.txt
```

**The port is already in use**

For FastAPI, use another port:

```bash
uvicorn app:app --reload --port 8001
```

For Streamlit, use another port:

```bash
python -m streamlit run streamlit_app.py --server.port 8502
```

If you change the FastAPI port, update the frontend `API_URL` to match.

**The model file cannot be found**

Verify that `churn_model.joblib` exists in the main repository folder and that the backend is loading the correct path.

**The frontend cannot connect to the API**

Check that the backend is running, that `API_URL` is correct, and that the request uses the expected input fields. For a local connection, verify that FastAPI is accessible at `http://127.0.0.1:8000/docs`.

**The deployed API is slow or temporarily unavailable**

A cloud-hosted service may take time to respond after inactivity, depending on its hosting configuration. Check the API documentation or health endpoint to verify its status.

## API Documentation

The FastAPI backend provides the following endpoints.

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Basic API information |
| GET | `/health` | Health check |
| POST | `/predict` | Predict customer churn |

### Interactive API Documentation

- **Deployed API:** https://end-to-end-customer-churn-hw7x.onrender.com/docs
- **Local API:** http://127.0.0.1:8000/docs

The `/predict` endpoint accepts customer information as JSON and returns the churn prediction and probability, along with the configured threshold.

The exact request fields must match the input schema defined in `app.py`.

##💼 Business Value

This project demonstrates how machine learning can support customer retention decisions.

Potential business applications include:

- Identifying customers who may be at risk of leaving.
- Prioritizing retention campaigns.
- Supporting targeted discounts or service improvements.
- Helping customer success teams focus on higher-risk accounts.
- Monitoring model performance as customer behavior changes.

Predictions should be combined with business context and retention campaign costs. A churn probability alone does not establish whether a particular intervention will be profitable.

## ⚠️Limitations and Future Improvements

Potential next steps include:

- Evaluate model calibration and probability reliability.
- Monitor performance on new customer data.
- Add automated tests for preprocessing, API inputs, and predictions.
- Introduce structured logging and better error handling.
- Add CI/CD checks and reproducible deployment workflows.
- Track precision, recall, F1-score, and drift over time.
- Evaluate retention strategies using business outcomes and campaign costs.
- Add authentication, rate limiting, and monitoring if the API is used in a production environment.

The current application performs **inference using a previously trained model**. It does not automatically retrain the model whenever someone submits a prediction. Any future retraining process should use an appropriate, validated dataset and a controlled model evaluation and deployment workflow.

## 👨‍💻Author

**Praveen**

- GitHub: https://github.com/Praveen673-ui
- Main Project: https://github.com/Praveen673-ui/end-to-end-customer-churn
- Streamlit Frontend: https://github.com/Praveen673-ui/telecom-churn-streamlit
- Live Application: https://telecom-churn-app-v4k2oxncrzh8ivwfcyiyrp.streamlit.app/

---

If you find this project useful, feel free to explore the repositories and try the live application.
