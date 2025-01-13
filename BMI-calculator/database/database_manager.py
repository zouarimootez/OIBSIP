import sqlite3

class DatabaseManager:
    """Handles all database operations."""
    def __init__(self, db_name='bmi_database.db'):
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        """Initialize the database and create tables if they don't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_data (
                    id INTEGER PRIMARY KEY,
                    weight REAL,
                    height REAL,
                    bmi REAL,
                    category TEXT
                )
            ''')
            conn.commit()

    def save_bmi_data(self, weight, height, bmi, category):
        """Save BMI data to the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO user_data (weight, height, bmi, category)
                VALUES (?, ?, ?, ?)
            ''', (weight, height, bmi, category))
            conn.commit()

    def fetch_bmi_history(self):
        """Fetch all BMI data from the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT weight, height, bmi, category FROM user_data')
            return cursor.fetchall()