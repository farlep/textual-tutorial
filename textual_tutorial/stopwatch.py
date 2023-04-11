"""Stopwatch exercise with Textual."""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class StopwatchApp(App):
    """An app to manage stopwatches."""

    BINDINGS=[("d", "toggle_dark", "Toggle dark mode")]

def main() -> None:
    """Execute the program."""
    print("Here")
