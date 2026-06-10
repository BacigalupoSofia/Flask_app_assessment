# Dental Inventory App

A Flask-based web application for managing dental clinic inventory. The system allows users to track products, including categories, quantities, suppliers, and expiration dates, with built-in low-stock alerts and user authentication.

---

## Features

### User Authentication
- Secure login and logout system for predefined users
- Access control for inventory management features

### Inventory Management (CRUD)
- **Create:** Add new products to the inventory
- **Read:** View all products with key details
- **Update:** Edit existing product information
- **Delete:** Remove products from inventory

### Stock Monitoring
- Low-stock alerts for items below minimum threshold
- Visual highlighting of critical inventory levels

### Account Management
- View logged-in user account details

### Responsive Interface
- Built with Bootstrap 5 for mobile and desktop compatibility

---

## Technologies Used

- Backend: Python, Flask  
- Frontend: HTML, CSS, Bootstrap 5  
- Data Storage: In-memory Python data structures (for educational/demo purposes)

---

## Getting Started

### Prerequisites

- Python 3.x  
- pip (Python package installer)

---

### Installation

#### 1. Clone the repository:

bash
```
git clone https://github.com/BacigalupoSofia/Flask_app_assessment.git
cd Flask_app_assessment
```

#### 2,  Create and activate a virtual environment
macOS / Linux
```
python3 -m venv venv
source venv/bin/activate
```
Windows
```
python -m venv venv
venv\Scripts\activate
```

#### 3. Install dependencies
```
pip install -r requirements.txt
```

### Running the Application
Start the Flask server 
```python app.py```
Open in browser 
```http://127.0.0.1:5000```

---
## Demo Accounts

The application uses predefined users stored in data_base.py:
```
Clinic1
Username: Clinic1
Password: Clinic1!
Clinic2
Username: Clinic2
Password: Clinic2!
```

---
## Project Structure
```
📁 Flask_app_assessment 
├── 📄 app.py
├── 📄 data_base.py
├── 📄 requirements.txt
├── 📁 templates/
├── 📁 static/
└── 📄 README.md
```

---
## Security Note

This project is intended for educational purposes only. It uses hardcoded demo user accounts and in-memory storage.

---
## Future Improvements
- Replace in-memory storage with a database.
- Add a "Create new user" feature to link to a specific data base for the user. 
- Improve inventory analytics and reporting to see orders, low stock list and providers. 
