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
    '8D6R-02ZA-81UD',
    'WAEN N.A',
    'Digital Marketing',
    '2020-05-26',
    'Valid',
    '8D6R-02ZA-81UD.pdf'
)
''')

conn.commit()

conn.close()

print("Certificate inserted successfully")