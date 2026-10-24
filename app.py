
from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd

# Create the FastAPI application
app = FastAPI(
    title="Telecom Customer Churn Prediction API",
    description="Predict whether a telecom customer is likely to churn.",
    version="1.0.0"
)

# Load the saved model and its settings
artifact = joblib.load("churn_model.joblib")

model = artifact["model"]
threshold = artifact["threshold"]
target_mapping = artifact["target_mapping"]


# Define the customer input fields
class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int = Field(ge=0, le=1)
    Partner: str
    Dependents: str
    tenure: int = Field(ge=0)
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float = Field(ge=0)
    TotalCharges: float = Field(ge=0)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Telecom Customer Churn Prediction API is running"
    }


# Health check endpoint
@app.get("/health")
def health():
    return {"status": "healthy"}


# Predict customer churn
@app.post("/predict")
def predict_churn(customer: CustomerData):

    # Convert customer details into a DataFrame
    customer_df = pd.DataFrame([customer.model_dump()])

    # Get the probability of churn
    churn_probability = model.predict_proba(customer_df)[0][1]

    # Apply the selected classification threshold
    prediction = int(churn_probability >= threshold)

    return {
        "prediction": target_mapping[prediction],
        "churn_probability": round(float(churn_probability), 4),
        "churn_probability_percent": round(
            float(churn_probability) * 100, 2
        ),
        "threshold": threshold
    }
