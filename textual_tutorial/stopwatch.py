"""Stopwatch exercise with Textual."""

from time import monotonic

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.reactive import reactive
from textual.widgets import Button, Header, Footer, Static


class TimeDisplay(Static):
    """A widget to display elapsed time."""

    start_time = reactive(monotonic)
    time = reactive(0.0)
    total = reactive(0.0)

    def on_mount(self) -> None:
        """Call an event hadler when widget is added to the app."""
        self.update_timer = self.set_interval(1 / 60,
            self.update_time, pause = True)

    def update_time(self) -> None:
        """Update the time to the current time."""
        self.time = self.total + monotonic() - self.start_time

    def watch_time(self, time: float) -> None:
        """Change the displayed text when the time attribute changes."""
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{hours:02.0f}:{minutes:02.0f}:{seconds:05.2f}")

    def start(self) -> None:
        """Start or resume time updating."""
        self.start_time = monotonic()
        self.update_timer.resume()

    def stop(self) -> None:
        """Stop time updating."""
        self.update_timer.pause()
        self.total += monotonic() - self.start_time
        self.time = self.total

    def reset(self) -> None:
        """Reset time to zero."""
        self.total = 0
        self.time = 0


class Stopwatch(Static):
    """A stopwatch widget."""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Call an event handler when a button is pressed."""
        button_id = event.button.id
        time_display = self.query_one(TimeDisplay)
        if button_id == "start":
            time_display.start()
            self.add_class("started")
        elif button_id == "stop":
            time_display.stop()
            self.remove_class("started")
        elif button_id == "reset":
            time_display.reset()

    def compose(self) -> ComposeResult:
        """Create child widgets."""
        yield Button("Start", id = "start", variant = "success")
        yield Button("Stop", id = "stop", variant = "error")
        yield Button("Reset", id = "reset")
        yield TimeDisplay("00:00:00.00")


class StopwatchApp(App):
    """An app to manage stopwatches."""

    CSS_PATH = "stopwatch.css"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("a", "add_stopwatch", "Add"),
        ("r", "remove_stopwatch", "Remove"),
        ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(Stopwatch(), Stopwatch(), Stopwatch(),
            id = "stopwatches")

    def action_add_stopwatch(self) -> None:
        """Add a new stopwatch."""
        new_stopwatch = Stopwatch()
        self.query_one("#stopwatches").mount(new_stopwatch)
        new_stopwatch.scroll_visible()

    def action_remove_stopwatch(self) -> None:
        """Remove the last stopwatch."""
        stopwatches = self.query("Stopwatch")
        if stopwatches:
            stopwatches.last().remove()

    def action_toggle_dark(self) -> None:
        """Toggle dark mode."""
        self.dark = not self.dark


def main() -> None:
    """Execute the program."""
    app = StopwatchApp()
    app.run()

if __name__=="__main__":
    main()
