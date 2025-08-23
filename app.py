from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'varsha'  # Set a secret key for session management

@app.route('/search.html', methods=['GET'])
def search():
    blood_type = request.args.get('blood_type', '')
    location = request.args.get('location', '')

    query = "SELECT id, name, blood_type, phone, location, last_donation_date FROM Donors WHERE 1=1"
    params = []

    if blood_type:
        query += " AND blood_type = %s"
        params.append(blood_type)
    if location:
        query += " AND location LIKE %s"
        params.append(f"%{location}%")

    connection = get_db_connection()
    donors = []
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        donors = cursor.fetchall()
        cursor.close()
        connection.close()

    return render_template('search.html', donors=donors)

# MySQL connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'varsha',
    'database': 'blood_donation'
}

def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/donors', methods=['GET'])
def donors():
    blood_type = request.args.get('blood_type', '')
    location = request.args.get('location', '')

    query = "SELECT id, name, blood_type, phone, location, last_donation_date FROM Donors WHERE 1=1"
    params = []
    

    if blood_type:
        query += " AND blood_type = %s"
        params.append(blood_type)
    if location:
        query += " AND location LIKE %s"
        params.append(f"%{location}%")

    connection = get_db_connection()
    donors = []
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        donors = cursor.fetchall()
        cursor.close()
        connection.close()

    return render_template('donors.html', donors=donors)

@app.route('/add_donor', methods=['POST'])
def add_donor():
    name = request.form['name']
    blood_type = request.form['blood_type']
    phone = request.form['phone']
    location = request.form['location']
    last_donation_date = request.form.get('last_donation_date', None)
    if last_donation_date == '':
        last_donation_date = None

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        insert_query = """
            INSERT INTO Donors (name, blood_type, phone, location, last_donation_date)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (name, blood_type, phone, location, last_donation_date))
        connection.commit()
        cursor.close()
        connection.close()

    return redirect(url_for('donor_list'))

@app.route('/requests', methods=['GET'])
def requests_view():
    return render_template('requests.html')

@app.route('/add_request', methods=['POST'])
def add_request():
    hospital_name = request.form['hospital_name']
    blood_type = request.form['blood_type']
    quantity = int(request.form['quantity'])
    request_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status = 'Pending'

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        # Count donors with the requested blood type
        cursor.execute("SELECT COUNT(*) FROM Donors WHERE blood_type = %s", (blood_type,))
        available_count = cursor.fetchone()[0]

        if available_count >= quantity:
            status = 'Fulfilled'
        else:
            status = 'Pending'

        insert_query = """
            INSERT INTO BloodRequest (hospital_name, blood_type, quantity, request_date, status)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (hospital_name, blood_type, quantity, request_date, status))
        connection.commit()
        cursor.close()
        connection.close()

    return redirect(url_for('request_list'))

@app.route('/request_list')
def request_list():
    connection = get_db_connection()
    requests = []
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, hospital_name, blood_type, quantity, request_date, status FROM BloodRequest")
        requests = cursor.fetchall()
        cursor.close()
        connection.close()
    return render_template('request_list.html', requests=requests)

@app.route('/donor_list')
def donor_list():
    connection = get_db_connection()
    donors = []
    if connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, name, blood_type, phone, location, last_donation_date FROM Donors")
        donors = cursor.fetchall()
        cursor.close()
        connection.close()
    return render_template('donor_list.html', donors=donors)

from flask import flash

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Here you can add logic to store the message or send an email
        # For now, just print to console or log
        print(f"Contact form submitted: Name={name}, Email={email}, Message={message}")

        # Flash a success message or redirect
        flash('Thank you for contacting us! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
