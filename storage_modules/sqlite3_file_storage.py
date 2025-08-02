import sqlite3
from .data_save_interface import DataSaveInterface


class Sqlite3Storage(DataSaveInterface):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.connection = sqlite3.connect(file_path)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS pills (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                measure TEXT NOT NULL,
                description TEXT NOT NULL,
                frequency_day INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        """
        )
        self.connection.commit()


    def load(self):
        """Load raw data."""
        users = []
        pills = []
        self.cursor.execute("SELECT * FROM users")
        for user_id, name, age in self.cursor.fetchall():
            users.append({"id": user_id, "name": name, "age": age})
        self.cursor.execute("SELECT * FROM pills")
        for pill_id, user_id, name, measure, description, frequency_day in self.cursor.fetchall():
            pills.append(
                {
                    "id": pill_id,
                    "user_id": user_id,
                    "name": name,
                    "measure": measure,
                    "description": description,
                    "frequency_day": frequency_day,
                }
            )
        return users, pills

    def save(self, data:str):
        """Save raw data."""
        for user in data["users"]:
            self.cursor.execute(
                "INSERT INTO users (id, name, age) VALUES (?, ?, ?)",
                (user["id"], user["name"], user["age"]),
            )
        for pill in data["pills"]:
            self.cursor.execute(
                "INSERT INTO pills (id, user_id, name, measure, description, frequency_day) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    pill["id"],
                    pill["user_id"],
                    pill["name"],
                    pill["measure"],
                    pill["description"],
                    pill["frequency_day"],
                ),
            )
        self.connection.commit()

    def update(self, data: str):
        """Update raw data."""
        self.cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (data["name"], data["age"], data["id"]))
        self.cursor.execute(
            "UPDATE pills SET name = ?, measure = ?, description = ?, frequency_day = ? WHERE id = ?",
            (
                data["name"],
                data["measure"],
                data["description"],
                data["frequency_day"],
                data["id"],
            ),
        )
        self.connection.commit()
    
    def close(self):
        """Close the database connection."""
        self.connection.close()
