import sqlite3

conn = sqlite3.connect('certificates.db')

cursor = conn.cursor()

cursor.execute(
    "DELETE FROM certificates WHERE reference_number=?",
    ('CERT-010',)
)

conn.commit()

conn.close()

print("Certificate deleted successfully")