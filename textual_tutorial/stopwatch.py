"""Stopwatch exercise with Textual."""

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Header, Footer, Static

class TimeDisplay(Static):
    """A widget to display elapsed time."""

class Stopwatch(Static):
    """A stopwatch widget."""

    def compose(self) -> ComposeResult:
        """Create child widgets."""
        yield Button("Start", id = "start", variant = "success")
        yield Button("Stop", id = "stop", variant = "error")
        yield Button("Reset", id = "reset")
        yield TimeDisplay("00:00:00.00")

class StopwatchApp(App):
    """An app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(Stopwatch(), Stopwatch(), Stopwatch())

    def action_toggle_dark(self) -> None:
        """Toggle dark mode."""
        self.dark = not self.dark

def main() -> None:
    """Execute the program."""
    app = StopwatchApp()
    app.run()
