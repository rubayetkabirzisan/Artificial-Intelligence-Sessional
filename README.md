# **AI Lecture Note Generator + Churn Sentinel (Dual AI Project)**

### *A multimodal education assistant + a predictive churn analytics bot*

---

## 🚀 **Project Overview**

This repository contains **two fully production-ready AI systems**:

### **1. AI Lecture Note Generator**

A multimodal pipeline that converts **lecture audio → clean transcript → structured summary → slides → quizzes** and automatically emails all materials to students.

### **2. Churn Sentinel (Customer Retention Bot)**

A predictive analytics system for SaaS businesses that identifies customers likely to cancel and triggers a **personalized discount email** using GPT automation.

Both projects demonstrate strong skills in:

* ML model training (Whisper, T5, XGBoost)
* End-to-end AI pipeline design
* Workflow automation using ActivePieces / AgentOps
* Practical implementation of AI in real-world domains (education + SaaS)

---

# 📚 **1. AI Lecture Note Generator**

## 🎯 **Features**

* 🎤 **Audio → Text** using fine-tuned Whisper
* 🧹 Transcript cleaning (filler removal, grammar correction)
* 📝 Bullet-point summary using fine-tuned T5
* 🖼 Auto-generated **PowerPoint slides**
* ❓ Auto-generated **quiz questions**
* 📧 Automatic email delivery to students
* 🔌 API endpoints for all operations

---

## 🏗 **Architecture**

```
Audio Input  
   ↓  
Whisper STT (fine-tuned)
   ↓  
Transcript Cleaner
   ↓  
T5 Summarizer (fine-tuned)
   ↓  
Slide Generator (Python-PPTX)
   ↓  
Quiz Generator (GPT / Rule-based)
   ↓  
Email Automation (SMTP / SendGrid)
```

---

## 🛠 **Tech Stack**

* **ML Models:** Whisper-small, T5-small
* **Backend:** Python, FastAPI
* **Document Generation:** python-pptx
* **Automation:** ActivePieces / AgentOps
* **Email Service:** SendGrid / Gmail API
* **Storage:** Local / S3

---

## 📦 **Installation**

```bash
git clone https://github.com/your-username/ai-lecture-generator-churn-sentinel.git
cd ai-lecture-generator-churn-sentinel

pip install -r requirements.txt
```

---

## ▶️ **Usage**

### **1. Run FastAPI**

```bash
uvicorn app.main:app --reload
```

### **2. Upload Audio**

```bash
POST /process-audio
file: lecture.mp3
```

### **3. Generate Slides**

```bash
GET /generate-slides/{session_id}
```

### **4. Email Final Package**

```bash
POST /email-materials
{
  "email": "student@example.com",
  "session_id": "123"
}
```

---

# 📊 **2. Churn Sentinel — Customer Retention Bot**

## 🎯 **Features**

* Predicts customer churn using XGBoost
* Runs daily automated churn check
* Detects customers with **>75% churn probability**
* Auto-generates “We miss you” retention email
* Sends via SendGrid / SMTP
* Logs all events for analytics

---

## 🏗 **Architecture**

```
Daily Cron Job
    ↓  
Pull User Activity Data
    ↓  
ML Model (XGBoost)
    ↓  
Risk Score > 0.75?
    ↓ Yes
GPT Email Generator → SendGrid → Customer
```

---

## 🛠 **Tech Stack**

* **ML:** XGBoost, Pandas, Scikit-learn
* **Automation:** ActivePieces / AgentOps
* **Emailing:** SendGrid API
* **Backend:** Python

---

## 📦 **Installation**

```bash
pip install -r churn/requirements.txt
```

---

## ▶️ **Usage**

### **Train the model**

```bash
python churn/train_model.py
```

### **Run prediction**

```bash
python churn/predict.py --user_id=1234
```

---

# 📁 **Folder Structure**

```
/
├── ai_lecture_generator/
│   ├── audio/
│   ├── transcripts/
│   ├── slides/
│   ├── quizzes/
│   ├── app/
│   │   ├── main.py
│   │   ├── stt.py
│   │   ├── summarizer.py
│   │   ├── ppt_generator.py
│   │   └── emailer.py
│   └── models/
│
└── churn_sentinel/
    ├── data/
    ├── models/
    ├── train_model.py
    ├── predict.py
    └── automation/
```

---

# 🖼 **Screenshots (Placeholders)**

### 🎤 Audio Upload UI

```
/screenshots/audio_upload.png
```

### 📊 Churn Dashboard

```
/screenshots/churn_dashboard.png
```

You can update these with real screenshots later.

---

# 🚀 **Future Improvements**

### AI Lecture Generator

* Add multimodal slide generation (images + diagrams)
* Add plagiarism detection
* Add classroom analytics dashboard

### Churn Sentinel

* Integrate Telegram/WhatsApp alerts
* Add A/B testing for retention email strategies
* Add LTV (Lifetime Value) prediction model

