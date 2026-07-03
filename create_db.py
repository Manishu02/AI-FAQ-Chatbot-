import sqlite3

conn = sqlite3.connect("faq.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS faq (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
)
""")
cursor.execute("DROP TABLE IF EXISTS logs")

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute(""" INSERT INTO faq (question, answer) VALUES ('What are your working hours?', 'We are open from 9 AM to 6 PM') """) 

cursor.execute(""" INSERT INTO faq (question, answer) VALUES ('What is your return policy?', 'Returns accepted within 30 days') """)

cursor.execute("""
INSERT INTO faq (question, answer)
VALUES
('How can I contact support?', 'You can email us at support@company.com')
""")

cursor.execute("""
INSERT INTO faq (question, answer)
VALUES
('Where are you located?', 'We are located in New Delhi, India')
""")

cursor.execute("""
INSERT INTO faq (question, answer)
VALUES
('Do you provide refunds?', 'Yes, refunds are available according to our policy')
""")

cursor.execute("""
INSERT INTO faq (question, answer)
VALUES
('What services do you offer?', 'We offer software development and consulting services')
""")

cursor.execute("""
INSERT INTO faq (question, answer)
VALUES
('What is your email address?', 'contact@company.com')
""")

cursor.execute("""
INSERT INTO faq (question, answer)
VALUES
('What is your phone number?', '+91 9876543210')
""")

cursor.execute("""
INSERT INTO faq (question, answer)
VALUES
('What payment methods do you accept?', 'We accept cards, UPI and net banking')
""")

cursor.execute("""
INSERT INTO faq (question, answer)
VALUES
('How long does delivery take?', 'Delivery usually takes 3 to 5 business days')
""")

conn.commit()
conn.close()

print("Database Created Successfully")