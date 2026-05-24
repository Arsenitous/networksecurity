# Network Security Phishing Detection Project

## 📚 Overview
This repository implements a **machine‑learning pipeline** for detecting phishing URLs. It covers the full lifecycle:
- **Data ingestion & validation**
- **Feature engineering / transformation**
- **Model training & registration** using **MLflow** (hosted on DagsHub)
- **FastAPI** service that serves predictions via an HTTP endpoint.

The goal is to provide an end‑to‑end example of a production‑ready ML workflow for network‑security analysts.

## 🚀 How to Use (step‑by‑step)
1. **Clone the repo & set up the environment**
   ```bash
   git clone <your‑repo‑url>
   cd "ML_Project Network Security"
   python -m venv venv
   venv\Scripts\activate   # on Windows
   pip install -r requirements.txt
   ```
2. **Configure secrets**
   - Create a `.env` file in the project root.
   - Add required variables (example):
     ```
     MONGODB_URL_KEY=mongodb+srv://<user>:<pass>@cluster0.mongodb.net
     DAGS_HUB_TOKEN=<your‑dagshub‑token>
     ```
3. **Run the training pipeline**
   ```bash
   python app.py   # this will also start FastAPI, but the `/train` endpoint triggers training
   # Or call the endpoint directly:
   curl http://localhost:8000/train
   ```
   After successful execution you will see the trained model and pre‑processor saved under `final_model/` and logged to DagsHub.
4. **Start the API server** (if not already running)
   ```bash
   uvicorn app:app --reload
   ```
5. **Make a prediction**
   ```bash
   curl -X POST "http://localhost:8000/predict" \
        -F "file=@your_test_file.csv" 
   ```
   The response returns an HTML table with the original data plus a `predicted_column` indicating *phishing* (1) or *legitimate* (0).
6. **View results**
   - Prediction CSV is stored in `prediction_output/output.csv`.
   - Browse `http://localhost:8000/docs` for Swagger UI and interactive testing.

## 🗂️ Project Structure
```
Network Security/
├─ components/          # data ingestion, validation, transformation, model trainer
├─ utils/               # helper functions (load_object, etc.)
├─ pipelines/           # training pipeline orchestrator
├─ app.py               # FastAPI entry point
├─ final_model/         # saved pre‑processor & model
├─ prediction_output/   # auto‑generated predictions
└─ README.md            # **you are here**
```

## 📦 Dependencies
- `fastapi`, `uvicorn`, `python‑multipart` – API server
- `mlflow`, `dagshub` – experiment tracking & model registry
- `pandas`, `scikit‑learn` – data handling & ML
- `python‑dotenv` – environment variables
- plus standard scientific stack (numpy, etc.)

---
*Happy hacking! 🎉*