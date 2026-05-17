import sqlite3

conn = sqlite3.connect('certificates.db')

cursor = conn.cursor()

cursor.execute('''
INSERT INTO certificates
(
    reference_number,
    student_name,
    course_name,
    completion_date,
    status,
    pdf_file
)

VALUES
(
    'CERT-002',
    'Zulqurnain Saeed',
    'Digital Marketing',
    '2020-05-26',
    'Valid',
    'CERT-002.pdf'
)
''')

conn.commit()

conn.close()

print("Certificate inserted successfully")