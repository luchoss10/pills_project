from models.user import User
from models.pill import Pill
from models.register import Register

from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Button, Static, Input, Log, Header
from textual.reactive import Reactive


class CreateUser(Widget):
    
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
        yield Log()
        yield Button("Back", id="back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "create_user": 
            name = self.query_one("#name",Input).value
            age = int(self.query_one("#age",Input).value)
            user = create_user(name, age)
            self.query_one(Log).write(f"User created: {user}")
        elif event.button.id == "back":
            self.parent.remove(self)
            self.parent.mount(PillManagerApp())
        else:
            self.query_one(Log).write("Unknown button pressed.")

class PillManagerApp(App):
    #CSS_PATH = "pill_manager.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Pill Manager", id="title")
        yield Button("Create User", id="input_user")
        yield Log()
        yield Button("Exit", id="exit")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "input_user":
            self.mount(CreateUser())
        elif event.button.id == "exit":
            self.exit()
        else:
            self.query_one(Log).write("Unknown button pressed.")

def create_user(name: str, age:int) -> User:
    """
    Create a new user with the given name and age.
    """
    return User(name=name, age=age)

def create_pill(name: str, measure: int, description:str, frequency_day :int) -> Pill:
    """
    Create a new pill with the given name, measure, description and frequency day.
    """
    return Pill(name=name, measure=measure, description=description, frequency_day=frequency_day)

def create_register(pill: Pill, date: str, note: str) -> Register:
    """
    Create a new register with the given pill, date and note.
    """
    return Register(date=date, pill=pill, note=note)


if __name__ == "__main__":
    app = PillManagerApp()
    app.run()
