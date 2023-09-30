import sqlalchemy
from .data_save_interface import DataSaveInterface


class SQLFileStorage(DataSaveInterface):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.engine = sqlalchemy.create_engine(f"sqlite:///{file_path}")
        self.connection = self.engine.connect()
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """
        )
        self.connection.execute(
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

    def load(self):
        """Load raw data."""
        users = []
        pills = []
        for user_id, name, age in self.connection.execute("SELECT * FROM users"):
            users.append({"id": user_id, "name": name, "age": age})
        for pill_id, user_id, name, measure, description, frequency_day in self.connection.execute(
            "SELECT * FROM pills"
        ):
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

    def save(self, data: str):
        """Save raw data."""
        self.connection.execute("DELETE FROM users")
        self.connection.execute("DELETE FROM pills")
        for user in data["users"]:
            self.connection.execute(
                f"""
                INSERT INTO users (id, name, age)
                VALUES ({user["id"]}, "{user["name"]}", {user["age"]})
            """
            )
        for pill in data["pills"]:
            self.connection.execute(
                f"""
                INSERT INTO pills (id, user_id, name, measure, description, frequency_day)
                VALUES ({pill["id"]}, {pill["user_id"]}, "{pill["name"]}", "{pill["measure"]}", "{pill["description"]}", {pill["frequency_day"]})
            """
            )

    def update(self, data: str):
        self.connection.execute("DELETE FROM users")
        self.connection.execute("DELETE FROM pills")
        for user in data["users"]:
            self.connection.execute(
                f"""
                INSERT INTO users (id, name, age)
                VALUES ({user["id"]}, "{user["name"]}", {user["age"]})
            """
            )
        for pill in data["pills"]:
            self.connection.execute(
                f"""
                INSERT INTO pills (id, user_id, name, measure, description, frequency_day)
                VALUES ({pill["id"]}, {pill["user_id"]}, "{pill["name"]}", "{pill["measure"]}", "{pill["description"]}", {pill["frequency_day"]})
            """
            )
