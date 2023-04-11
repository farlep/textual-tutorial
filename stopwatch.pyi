from _typeshed import Incomplete
from textual.app import App, ComposeResult as ComposeResult
from textual.widgets import Static

class TimeDisplay(Static): ...

class Stopwatch(Static):
    def compose(self) -> ComposeResult: ...

class StopwatchApp(App):
    CSS_PATH: str
    BINDINGS: Incomplete
    def compose(self) -> ComposeResult: ...
    dark: Incomplete
    def action_toggle_dark(self) -> None: ...

def main() -> None: ...
