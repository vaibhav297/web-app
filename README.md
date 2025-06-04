# 📊 Finance Vision – Revenue Calculator & Excel Generator (Flask App)

**Finance Vision** is a simple yet powerful web application built with Python and Flask. It allows users to input revenue data, perform calculations, and export results to a professionally styled Excel file. This project demonstrates the use of a micro web framework (Flask) to create a financial dashboard and automate Excel reporting with formatting.

---

## 🔍 Overview

This application is designed for small-scale revenue tracking. Users can:

- Add and manage financial records
- Perform backend calculations on revenues
- Generate Excel reports with:
  - Background colors
  - Cell formatting
  - Organized tabular data

The frontend uses Jinja2 templates for dynamic rendering, while the backend handles business logic and Excel generation using Python libraries like `openpyxl` or `xlsxwriter`.

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS, Jinja2
- **Backend**: Flask (Python)
- **Excel Handling**: openpyxl / xlsxwriter
- **Data Handling**: Python dictionaries / Pandas (optional)

---

## 📁 Project Structure

```
web-app/
├── static/               # CSS and static assets
├── templates/
│   ├── base.html         # Reusable layout template
│   ├── dashboard.html    # Dashboard page with financial info
│   └── home.html         # About/landing page
├── app.py                # Main Flask application
├── generate_excel.py     # Excel report generation logic
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

Follow the steps below to set up the project on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/vaibhav297/web-app.git
cd web-app
```

### 2. Set up a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Visit `http://localhost:5000` in your browser to start using the app.

---

## 📦 Features

- ✅ Revenue record input form
- 📊 Revenue dashboard
- 📁 Excel export with:
  - Styled headers
  - Colored rows/columns
  - Proper formatting
- 🔐 Modular Flask code structure

---

## 💡 Example Use Cases

- Small business revenue tracking
- Educational demo for Flask and Excel automation
- Financial data reporting for coursework or clients

---

## 🔮 Future Enhancements

- Add charts using `Plotly` or `Chart.js`
- Store records in a database (SQLite/MySQL)
- Add authentication and role-based access
- Deploy on platforms like Heroku or Render

---


## 👤 Author

**Vaibhav Sahastrabuddhe**  
