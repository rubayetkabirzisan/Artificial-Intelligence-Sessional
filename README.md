# Churn Sentinel — Week-by-Week Development Plan

## Project Overview
Churn Sentinel is a predictive analytics system designed for SaaS businesses. It identifies customers at risk of churn and automatically generates personalized retention actions using AI agents and ML models.

## Week 1 — Data Collection & Exploratory Data Analysis (EDA)

**Goal:**  
Prepare clean datasets and understand customer behavior patterns.

**Tasks:**  
- Collect data:  
  - Activity logs  
  - Subscription/payment data  
  - Support tickets and interactions  
- Clean and preprocess datasets (`data_preprocessing.py`)  
- Explore features:  
  - Login trends  
  - Feature usage patterns  
  - Payment history and anomalies  
- Identify potential churn signals and thresholds

**Deliverables:**  
- Clean datasets (`/data/clean/`)  
- EDA report or notebook  
- Feature engineering plan for Week 2  


## Week 2 — Feature Engineering & Baseline Model

**Goal:**  
Engineer predictive features and build an XGBoost baseline model.

**Tasks:**  
- Engineer features:  
  - RFM (Recency, Frequency, Monetary)  
  - Activity trends  
  - Support ticket counts  
  - Payment delays  
- Train baseline XGBoost model (`train_model.py`)  
- Evaluate model performance:  
  - ROC-AUC  
  - Precision/Recall  
  - Confusion matrix  
- Save trained model artifacts (`/models/`)

**Deliverables:**  
- Trained baseline XGBoost model  
- Evaluation metrics report  
- Reproducible training script  



## Week 3 — Prediction Pipeline & Behavior Change Detector

**Goal:**  
Implement daily prediction flow and integrate Behavior Change Detector Agent.

**Tasks:**  
- Implement `predict.py` with:  
  - Threshold-based alerts (e.g., >0.75 risk score)  
  - Logging for flagged users  
- Add explainability using SHAP for feature importance  
- Implement **Behavior Change Detector Agent**:  
  - Detect unusual behavior (login/usage drops, ticket spikes, payment delays)  
  - Generate GPT-based summary for flagged users  

**Deliverables:**  
- Prediction script with logging and alerts  
- Behavior Change Detector outputs integrated  
- SHAP visualizations  



## Week 4 — GPT Email Generator & SendGrid Integration

**Goal:**  
Automate personalized retention emails for high-risk users.

**Tasks:**  
- Design GPT email prompt templates  
- Build `email_generator.py`  
- Integrate SendGrid email sending (`send_email.py`)  
- Test email generation and sending in sandbox environment  

**Deliverables:**  
- Generated email previews  
- Successful sandbox email sends  
- Templates ready for production automation  



## Week 5 — AI Agents: Discount Recommendation & Retention Planner

**Goal:**  
Enhance retention strategy with high-impact AI agents.

**Tasks:**  
- **Discount Recommendation Agent (`discount_agent.py`)**:  
  - Suggest 5%, 10%, or 15% discount based on churn risk and customer value  
  - Generate GPT explanations for recommended discounts  
- **Retention Action Planner Agent (`planner_agent.py`)**:  
  - Generate a full customer-specific action plan:  
    - Email type  
    - Discount (if applicable)  
    - Follow-up schedule  
    - Onboarding or assistance recommendations  
- Integrate agents with Behavior Change Detector into daily prediction pipeline  

**Deliverables:**  
- `discount_agent.py`  
- `planner_agent.py`  
- Fully integrated daily pipeline with AI agents  



## Week 6 — Automation & Conversational Dashboard Assistant

**Goal:**  
Orchestrate end-to-end pipeline and add a GPT-powered mini chat assistant.

**Tasks:**  
- Build automation workflow (`/automation/run_daily.py` or ActivePieces workflow):  
  - Pull data → Predict → Run agents → Generate emails → Send emails → Log actions → Dashboard updates  
- Add **Conversational Dashboard Assistant**:  
  - Query high-risk users  
  - Explain why users were flagged  
  - List sent discounts or emails  
- Build interactive dashboard using **Streamlit** or **Flask**  

**Deliverables:**  
- Fully automated daily pipeline  
- Interactive dashboard with chat assistant  
- GPT function-calling queries integrated  



## Optional Week 7 — Polishing & Monitoring

**Goal:**  
Enhance production readiness and analytics.

**Tasks:**  
- Add monitoring:  
  - Daily churn summary  
  - Email open and click rates  
- Refine agent outputs, email templates, and dashboard UI  
- Add screenshots for project README/demo  

**Deliverables:**  
- Dashboard enhancements and monitoring metrics  
- Logs and analytics  
- Demo screenshots  



## Optional Week 8 — Advanced Improvements

**Goal:**  
Extend AI capabilities for scalability and experimentation.

**Tasks:**  
- Multi-channel notifications (Telegram/WhatsApp)  
- LTV (Lifetime Value) scoring for customers  
- A/B testing for email subjects and retention strategies  
- Automated model retraining pipeline  

**Deliverables:**  
- Multi-channel alert system  
- LTV-based prioritization in agents  
- Automated retraining workflow  



## ✅ Summary of AI Agents and Features by Week

| Week | AI Feature / Agent                 | Description                                     |
|------|----------------------------------|-------------------------------------------------|
| 3    | Behavior Change Detector Agent    | Rule-based anomaly detection + GPT summary     |
| 4    | GPT Email Generator               | Personalized retention email automation        |
| 5    | Discount Recommendation Agent     | Suggests optimal retention discount            |
| 5    | Retention Action Planner Agent    | Generates full action plan per customer        |
| 6    | Conversational Dashboard Assistant| Mini GPT-powered chat for dashboard            |
| 1–6  | XGBoost Model + Automation + Logging | Core ML model with explainability and end-to-end pipeline |

## ⚡ Key Takeaways
- Achievable in **7 weeks** with **1–2 hours/day**  
- Delivers **AI-like functionality** without complex algorithms  
- Provides **real functionality**, **clean UI**, and **smart scheduling**  
- Perfect for **beginner–intermediate developers**  

