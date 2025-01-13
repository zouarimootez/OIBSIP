import sqlite3

class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)

    def initialize_database(self):
        """Initialize the database and create tables if they don't exist."""
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password TEXT UNIQUE,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.connection.commit()

    def save_password(self, password):
        """Save the generated password to the database."""
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO passwords (password) VALUES (?)", (password,))
        self.connection.commit()

    def get_password_history(self):
        """Retrieve the password history from the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT password, timestamp FROM passwords ORDER BY timestamp DESC")
        return cursor.fetchall()

    def password_exists(self, password):
        """Check if the password already exists in the database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT id FROM passwords WHERE password = ?", (password,))
        return cursor.fetchone() is not None