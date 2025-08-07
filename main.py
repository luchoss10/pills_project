from models.user import User
from models.pill import Pill
from models.register import Register

from textual.app import App, ComposeResult
from textual.screen import Screen  
from textual.widgets import Button, Static, Input, Log, Header

from storage_modules.sqlite3_file_storage import Sqlite3Storage

squlite3 = Sqlite3Storage("pill_manager.db")

class CreateUser(Screen):

    DEFAULT_CSS = """
    CreateUser {
        background: $background;
        color: $primary;
    }
    CreateUser #name {
        background: $background;
        color: $primary;
    }
    CreateUser #age {
        background: $background;
        color: $primary;
    }
    CreateUser #create_user {
        background: $background;
        color: $primary;
    }
    CreateUser #back {
        background: $background;
        color: $primary;
    }
    """

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter your name", type="text", id="name")
        yield Input(placeholder="Enter your age", type="integer", id="age")
        yield Button("Create User", id="create_user") 
        yield Log(id="log")
        yield Button("Back", id="back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        log = self.query_one("#log", Log)
        if event.button.id == "create_user": 
            name = self.query_one("#name", Input).value
            age_str = self.query_one("#age", Input).value
            try:
                age = int(age_str)
                user = create_user(name, age)
                # Load existing users, append new one, and save
                data = squlite3.load()
                users = data[0] if data else []
                users.append({"name": user.name, "age": user.age})
                squlite3.save({"users": users})
                log.write(f"User created: {user.name}, Age: {user.age}")
                self.app.pop_screen()  # Go back to main screen
                self.app.query_one(PillManagerScreen).refresh_users()
            except Exception as e:
                log.write(f"Error creating user: {e}")
        elif event.button.id == "back":
            self.app.pop_screen()
        else:
            log.write("Unknown button pressed.")

class PillManagerScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Pill Manager", id="title")
        yield Button("Create User", id="input_user")
        yield Log(id="user_log")
        yield Button("Exit", id="exit")

    def on_mount(self):
        self.refresh_users()

    def refresh_users(self):
        log = self.query_one("#user_log", Log)
        log.clear()
        data = squlite3.load()
        users = data[0] if data else []
        if not users:
            log.write("No users found.")
        else:
            for user in users:
                log.write(f"User: {user['name']}, Age: {user['age']}\n")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "input_user":
            self.app.push_screen(CreateUser())
        elif event.button.id == "exit":
            self.app.exit()
        else:
            log = self.query_one("#user_log", Log)
            log.write("Unknown button pressed.")

def create_user(name: str, age: int) -> User:
    return User(name=name, age=age)

def create_pill(name: str, measure: int, description: str, frequency_day: int) -> Pill:
    return Pill(name=name, measure=measure, description=description, frequency_day=frequency_day)

def create_register(pill: Pill, date: str, note: str) -> Register:
    return Register(date=date, pill=pill, note=note)

class PillManagerApp(App):
    def on_mount(self):
        self.push_screen(PillManagerScreen())

if __name__ == "__main__":
    app = PillManagerApp()
    app.run()
