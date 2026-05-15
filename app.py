from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# INITIALIZE DATABASE
def init_db():

    conn = sqlite3.connect('certificates.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS certificates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reference_number TEXT UNIQUE,
        student_name TEXT,
        course_name TEXT,
        completion_date TEXT,
        status TEXT,
        pdf_file TEXT
    )
''')

    conn.commit()
    conn.close()

# RUN DATABASE SETUP
init_db()

# GET CERTIFICATE FROM DATABASE
def get_certificate(reference):

    conn = sqlite3.connect('certificates.db')
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM certificates WHERE reference_number=?",
        (reference,)
    )

    certificate = cursor.fetchone()

    conn.close()

    return certificate

# HOME PAGE
@app.route('/')
def home():

    return render_template('index.html')

# VERIFY PAGE
@app.route('/verify/<reference>')
def verify(reference):

    certificate = get_certificate(reference)

    return render_template(
        'verify.html',
        certificate=certificate
    )
@app.route('/search')
def search():

    reference = request.args.get('reference')

    return verify(reference)

if __name__ == '__main__':
    app.run(debug=True)