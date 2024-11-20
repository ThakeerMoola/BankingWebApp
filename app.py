from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import random
import os
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For flash messages

DATABASE_FILE = "database_gui.json"


# Helper Functions
def load_database():
    """Load user database."""
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)
    return {}


def save_database(database):
    """Save user database."""
    with open(DATABASE_FILE, "w") as file:
        json.dump(database, file)


def generate_account_number():
    """Generate a random account number."""
    return str(random.randint(1000000000, 9999999999))


# Routes
@app.route('/')
def home():
    """Home page with options to create account or login."""
    return render_template('index.html')


@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    """Create a new account."""
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        phone = request.form['phone']
        id_number = request.form['id_number']
        password = request.form['password']

        # Validate inputs
        if not (name and surname and phone and id_number and password):
            flash("All fields are required!", 'error')
            return redirect(url_for('create_account'))

        # Load the existing database
        database = load_database()

        if phone in database:
            flash("Account with this phone number already exists.", 'error')
            return redirect(url_for('create_account'))

        account_number = generate_account_number()

        # Save the new account data
        database[phone] = {
            "name": name,
            "surname": surname,
            "phone": phone,
            "id_number": id_number,
            "password": password,
            "account_number": account_number,
            "balance": 0.0,
            "transactions": [],
        }
        save_database(database)

        flash(f"Account created successfully! Your account number is: {account_number}", 'success')
        return redirect(url_for('home'))

    return render_template('create_account.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page."""
    if request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']

        # Load the existing database
        database = load_database()

        # Check if the user exists
        if phone in database and database[phone]['password'] == password:
            flash("Login successful!", 'success')
            return redirect(url_for('dashboard', phone=phone))

        flash("Invalid phone number or password.", 'error')
        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/dashboard/<phone>', methods=['GET', 'POST'])
def dashboard(phone):
    """User dashboard to view balance and transactions."""
    database = load_database()

    if phone not in database:
        flash("User not found.", 'error')
        return redirect(url_for('home'))

    user = database[phone]

    if request.method == 'POST':
        action = request.form['action']
        if action == 'deposit':
            amount = float(request.form['amount'])
            if amount <= 0:
                flash("Invalid amount.", 'error')
            else:
                user['balance'] += amount
                user['transactions'].append(f"Deposited ${amount:.2f}")
                save_database(database)
                flash(f"${amount:.2f} deposited successfully!", 'success')

        elif action == 'withdraw':
            amount = float(request.form['amount'])
            if amount <= 0 or amount > user['balance']:
                flash("Invalid or insufficient funds.", 'error')
            else:
                user['balance'] -= amount
                user['transactions'].append(f"Withdrew ${amount:.2f}")
                save_database(database)
                flash(f"${amount:.2f} withdrawn successfully!", 'success')

    return render_template('dashboard.html', user=user)


@app.route('/transaction_history/<phone>')
def transaction_history(phone):
    """Display transaction history."""
    database = load_database()

    if phone not in database:
        flash("User not found.", 'error')
        return redirect(url_for('home'))

    user = database[phone]
    transactions = user['transactions'] if user['transactions'] else ["No transactions yet."]
    return jsonify(transactions)


if __name__ == "__main__":
    app.run(debug=True)
