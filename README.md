

---

# 🏦 MoolaVest Bank  

**MoolaVest Bank** is a sleek and modern web-based banking application built using Flask. It offers core banking functionalities like creating accounts, managing balances, viewing transaction history, and transferring funds, all wrapped in a user-friendly and visually appealing design.  

![image](https://github.com/user-attachments/assets/4f1e02c9-46ad-4a7e-bed7-9074609a77a9)


---

## 🚀 Features  

### 🛡️ User Authentication  
- **Secure Login and Registration**  
  - Passwords are encrypted for safe storage.  

### 💳 Account Management  
- **Deposit, Withdraw, and Transfer Funds**  
  - Manage your balance with ease.  

### 📊 Transaction History  
- **Detailed and Organized History**  
  - Transaction data is displayed in a clean, sortable table format.  

### 🎨 Modern UI  
- **Responsive and Stylish Design**  
  - Features a linear gradient background, intuitive layout, and a professional look.  

---


### **1. Dashboard**  
The dashboard provides an overview of the user's account balance and quick access to banking operations.  

![image](https://github.com/user-attachments/assets/5ef7e542-170f-4dde-be0f-8781b41aa75a)

### **2. Login Page**  
A clean and simple login page for secure access to your account.  

![image](https://github.com/user-attachments/assets/257db65f-cd3a-4331-9c75-2bd247c5b21d)

### **3. Transaction History**  
All transactions are displayed in an elegant table for better visibility and tracking.  

![image](https://github.com/user-attachments/assets/960d50b2-8184-43a5-ae9d-59ebec90ee9a)

---

## 🛠️ Installation and Setup  

### 📋 Prerequisites  

- Python 3.8+  
- Pip (Python package manager)  
- A code editor (e.g., PyCharm, VS Code)  

### 📥 Steps  

1. **Clone the Repository**:  
   ```bash
   git clone git@github.com:ThakeerMoola/BankingWebApp.git
   ```  

2. **Create and Activate a Virtual Environment** (Optional but recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```  

3. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```  

4. **Run the Application**:  
   ```bash
   flask run
   ```  

5. **Access the App in Your Browser**:  
   Open your browser and navigate to `http://127.0.0.1:5000/`.  

---

## 📂 Project Structure  

```plaintext
moolavest-bank/
├── static/                 # Static files (CSS, images, etc.)
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── images/
│   │   └── background.jpg  # Background image
├── templates/              # HTML templates
│   ├── dashboard.html      # Dashboard page
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   └── transfer.html       # Transfer funds page
├── screenshots/            # Screenshots for the README
│   ├── dashboard.png
│   ├── login.png
│   └── transaction-history.png
├── app.py                  # Main Flask application
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## ✨ Key Design Details  

### 🎨 CSS Highlights  
- **Linear Gradient Background**:  
  ```css
  body {
      background: linear-gradient(to right, #1E3C72, #2A5298); /* Elegant gradient */
      background-size: cover;
      background-repeat: no-repeat;
  }
  ```  

- **Transaction Table Styling**:  
  A clean and modern look for transaction history.  
  ```css
  .transaction-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
      background-color: #fff;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  ```

---

## 🔧 Technologies Used  

- **Backend**: Flask (Python)  
- **Frontend**: HTML5, CSS3  
- **Database**: SQLite (or upgradeable to other DBs)  

---

## 📜 License  

This project is licensed under the **MIT License**. See the LICENSE file for more details.  

---

## 🙌 Contribution Guidelines  

1. Fork the repository.  
2. Create a new feature branch:  
   ```bash
   git checkout -b feature-name
   ```  
3. Commit your changes:  
   ```bash
   git commit -m "Add new feature"
   ```  
4. Push your branch:  
   ```bash
   git push origin feature-name
   ```  
5. Open a pull request.  

---

## 📧 Contact  

Feel free to reach out if you have any questions or suggestions:  
- **Email**: moolathakeer@gmail.com
- **GitHub**: (https://github.com/ThakeerMoola)

---

Let me know if you need help creating or editing screenshots for this project! 😊
