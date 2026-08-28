# 🛡️ PhishGuard AI

### 🧠 Machine Learning Project — Phishing Website Detection & Classification System

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-UI-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](#-license)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](#-contributing)
[![GitHub stars](https://img.shields.io/github/stars/aryanvisualize/PhishGuard-AI?style=flat-square)](../../stargazers)
[![GitHub issues](https://img.shields.io/github/issues/aryanvisualize/PhishGuard-AI?style=flat-square)](../../issues)
[![Last Commit](https://img.shields.io/github/last-commit/aryanvisualize/PhishGuard-AI?style=flat-square)](../../commits/main)

[**Live Demo**](https://phishguard-ai-y0q2.onrender.com) · [**Report Bug**](../../issues) · [**Request Feature**](../../issues)

> **Paste a URL. Get a verdict. Stay off the hook.**

---

## 📋 Table of Contents

<details>
<summary><b>Click to expand/collapse</b></summary>

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#️-architecture)
- [Tech Stack](#️-tech-stack)
- [Application Workflow](#-application-workflow)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#️-environment-variables)
- [API Reference](#-api-reference)
- [Security Considerations](#️-security-considerations)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

</details>

---

## 🌟 Overview

**PhishGuard AI is a Machine Learning project** — a Flask-based web application that detects phishing websites in real time. It extracts URL-based features and runs them through a **logistic regression classifier** trained with **scikit-learn** to flag whether a given link is legitimate or a phishing attempt, all backed by user authentication, prediction history, and an analytics dashboard.

Built with **Python, Flask, scikit-learn, and SQLite**, PhishGuard AI simulates a real-world security tool — combining feature engineering, a trained ML model, persistent user accounts, and a clean Bootstrap UI into a single deployed platform.

> **One URL. One prediction. Zero blind trust.**

---

## ✨ Features

- 🔗 **URL Analysis**
  - Accepts any URL for inspection
  - Extracts lexical & structural features from the link
  - Feeds features into the trained classifier

- 🎣 **Phishing Detection**
  - Logistic regression model trained on phishing/legitimate URL data
  - Real-time classification — safe vs. phishing
  - Confidence-based prediction output

- 📊 **Analytics Dashboard**
  - Visual summary of scanned URLs
  - At-a-glance phishing vs. safe breakdown

- 🕓 **Prediction History**
  - Every scan logged per user
  - Revisit past URL checks anytime

- 🔐 **User Authentication**
  - Account registration & login
  - Session-based access to dashboard & history

---

## 🏗️ Architecture

```
flowchart TD
    A["🖥️ Bootstrap Frontend"] -->|Form Submit| B["⚙️ Flask Backend"]

    B --> C["🔐 Auth<br/>Session-based Login"]
    B --> D["🔗 URL Feature Extraction"]

    D --> E["🧠 Scikit-learn<br/>Logistic Regression Model"]
    E --> F["✅ Legit / 🎣 Phishing Verdict"]

    F --> G["🗄️ SQLite<br/>Prediction History"]
    G --> H["📊 Analytics Dashboard"]

    style A fill:#7952B3,color:#fff
    style B fill:#000000,color:#fff
    style E fill:#F7931E,color:#000
    style G fill:#07405E,color:#fff
```

---

## 🛠️ Tech Stack

| Layer                | Technologies                                                    |
| ---------------------- | ------------------------------------------------------------------ |
| **Frontend**            | Bootstrap, HTML5, CSS3, Jinja templates                            |
| **Backend**             | Python, Flask, RESTful routes                                      |
| **Machine Learning**    | Scikit-learn — logistic regression, URL feature extraction         |
| **Database**            | SQLite — user accounts & prediction history                        |
| **Authentication**      | Session-based login/registration                                   |
| **Deployment**          | Render                                                              |

---

## 🔄 Application Workflow

```
sequenceDiagram
    actor User
    participant App as PhishGuard AI
    participant ML as ML Model
    participant DB as SQLite DB

    User->>App: Register / log in
    User->>App: Submit a URL to scan
    App->>ML: Extract features & classify
    ML-->>App: Prediction (Safe / Phishing)
    App->>DB: Save prediction to history
    App-->>User: Show verdict
    User->>App: View dashboard
    App->>DB: Fetch prediction history
    DB-->>App: Past scan records
    App-->>User: Analytics & history view
```

---

## 📂 Project Structure

```
PhishGuard-AI/
│
├── app/                      # Flask application
│   ├── static/                 # CSS, JS, Bootstrap assets
│   ├── templates/               # Jinja HTML templates
│   ├── models/                  # Trained ML model files
│   ├── routes/                  # Flask route handlers
│   └── app.py                    # App entry point
│
├── data/                      # Training/reference URL datasets
├── database.db                 # SQLite database
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```
> The exact folder structure may vary depending on your implementation.

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/) & pip
- [Git](https://git-scm.com/)
- (Optional) a virtual environment tool — `venv` or `conda`

**1️⃣ Clone the repository**

```bash
git clone https://github.com/aryanvisualize/PhishGuard-AI.git
cd PhishGuard-AI
```

**2️⃣ Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

**3️⃣ Install dependencies**

```bash
pip install -r requirements.txt
```

**4️⃣ Configure environment variables**

See [Environment Variables](#️-environment-variables) below.

**5️⃣ Run the app**

```bash
flask run
```

The app will be available at `http://localhost:5000`.

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:

```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key

DATABASE_URL=sqlite:///database.db
```
> ⚠️ **Never commit your `.env` file or secret keys to GitHub.**

---

## 🔌 API Reference

**Expand full endpoint list**

```
/auth
    GET|POST  /register
    GET|POST  /login
    GET       /logout

/scan
    POST      /predict        # Submit a URL for classification

/dashboard
    GET       /               # Analytics overview

/history
    GET       /                # User's past predictions
```
> Exact routes depend on your implementation.

---

## 🛡️ Security Considerations

| Consideration        | Implementation                              |
| ---------------------- | ---------------------------------------------- |
| Authentication          | Session-based login, protected routes           |
| Secrets management      | Environment variables (`.env`)                  |
| Input validation         | URL sanitization before feature extraction      |
| Model integrity           | Versioned, pre-trained model artifacts          |
| Error handling             | Centralized Flask error handlers                |
| Logging                     | No sensitive data in logs                       |

---

## 📌 Roadmap

- [ ] 🌐 Browser extension for one-click URL scanning
- [ ] 🧠 Upgrade to ensemble / deep learning model
- [ ] 📈 Model performance metrics on dashboard
- [ ] 🔗 Bulk URL scanning via CSV upload
- [ ] 🔔 Real-time alerts for flagged domains
- [ ] 🗂️ Exportable prediction history (PDF/CSV)
- [ ] 🌍 Public API for third-party integration

---

## 🎯 Project Goals & Learning Outcomes

PhishGuard AI is a **Machine Learning project** built to demonstrate how classical ML techniques can power a practical cybersecurity tool — covering feature engineering, model training with scikit-learn, Flask backend development, authentication, and deployment.

```
flowchart LR
    A[Python] --> F[ML-Powered<br/>Security App]
    B[Flask] --> F
    C[Scikit-learn] --> F
    D[SQLite] --> F
    E[Bootstrap] --> F
```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Aryan Rastogi**
Full Stack Developer · AI/ML Enthusiast

GitHub: [github.com/aryanvisualize](https://github.com/aryanvisualize) · LinkedIn: [linkedin.com/in/aryan-rastogi-dev](https://www.linkedin.com/in/aryan-rastogi-dev/)

---

### ⭐ If you found this project useful, consider giving it a star!

**A Machine Learning project built with ❤️ using Python, Flask, Scikit-learn, and SQLite.**
