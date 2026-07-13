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
    'YOKME2KHUNOA6C5TTK-101647',
    'HASSAN NAGY HASSAN ABDELHAMID KHEDR',
    'Lisans diplomasi',
    '2026-07-10',
    'Valid',
    'YOKME2KHUNOA6C5TTK-101647.pdf'
)
''')

conn.commit()

conn.close()

print("Certificate inserted successfully")