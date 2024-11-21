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
    """Save user database in a neat and readable format."""
    with open(DATABASE_FILE, "w") as file:
        json.dump(database, file, indent=4)  # Add indent=4 for pretty formatting


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

        # Check if phone number or ID number already exists
        if phone in database:
            flash("An account with this phone number already exists.", 'error')
            return redirect(url_for('create_account'))

        if any(user['id_number'] == id_number for user in database.values()):
            flash("An account with this ID number already exists.", 'error')
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

@app.route('/transfer_funds/<phone>', methods=['GET', 'POST'])
def transfer_funds(phone):
    """Transfer funds from one account to another."""
    database = load_database()

    if phone not in database:
        flash("User not found.", 'error')
        return redirect(url_for('home'))

    user = database[phone]

    if request.method == 'POST':
        recipient_account_number = request.form['recipient_account_number']
        amount = float(request.form['amount'])

        # Find recipient by account number
        recipient = None
        for account in database.values():
            if account['account_number'] == recipient_account_number:
                recipient = account
                break

        # If recipient doesn't exist
        if not recipient:
            flash("Recipient account number not found.", 'error')
            return redirect(url_for('transfer_funds', phone=phone))

        # If amount is invalid or user has insufficient funds
        if amount <= 0 or amount > user['balance']:
            flash("Invalid amount or insufficient funds.", 'error')
            return redirect(url_for('transfer_funds', phone=phone))

        # Perform the transfer
        user['balance'] -= amount
        recipient['balance'] += amount

        # Add transaction details
        user['transactions'].append(f"Transferred R{amount:.2f} to account {recipient_account_number}")
        recipient['transactions'].append(f"Received R{amount:.2f} from account {user['account_number']}")

        save_database(database)

        flash(f"R{amount:.2f} transferred successfully to account {recipient_account_number}.", 'success')
        return redirect(url_for('dashboard', phone=phone))

    return render_template('transfer_funds.html', user=user)



@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page."""
    if request.method == 'POST':
        id_number = request.form['id_number']  # Get ID number instead of phone
        password = request.form['password']

        # Load the existing database
        database = load_database()

        # Check if the user exists using ID number
        for user in database.values():
            if user['id_number'] == id_number and user['password'] == password:
                flash("Login successful!", "login_success")
                return redirect(url_for('dashboard', phone=user['phone']))

        flash("Invalid ID number or password.", "login_error")
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
        try:
            amount = float(request.form['amount'])
            if action == 'deposit':
                if amount <= 0:
                    flash("Invalid amount.", 'error')
                else:
                    user['balance'] += amount
                    user['transactions'].append(f"Deposited R{amount:.2f}")
                    save_database(database)
                    flash(f"R{amount:.2f} deposited successfully!", 'success')

            elif action == 'withdraw':
                if amount <= 0 or amount > user['balance']:
                    flash("Invalid or insufficient funds.", 'error')
                else:
                    user['balance'] -= amount
                    user['transactions'].append(f"Withdrew R{amount:.2f}")
                    save_database(database)
                    flash(f"R{amount:.2f} withdrawn successfully!", 'success')

        except ValueError:
            flash("Please enter a valid amount.", 'error')

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
