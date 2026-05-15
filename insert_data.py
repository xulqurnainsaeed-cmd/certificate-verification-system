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
    'CERT-001',
    'Ali Khan',
    'Web Development',
    '2026-05-15',
    'Valid',
    'CERT-001.pdf'
)
''')

conn.commit()
conn.close()

print("Certificate Added Successfully")