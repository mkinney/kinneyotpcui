from textual.app import App, ComposeResult
from textual.widgets import Footer, Label, Markdown, TabbedContent, TabPane

ENCODE = """
Encode form goes here
"""

DECODE = """
Decode form goes here
"""

GENERATE = """
Generate form goes here
"""

SETTINGS = """
Settings goes here
"""

ABOUT = """
This code is similar to a 'one time pad' (aka Vernam Cipher) which can be used to encode/decode messages.

Tips:
- The key must be at least the same length as the uncoded text.
- The key must be truly random.
- The key must never be reused, in whole or in part.
- The key must be kept completely secret by the communicating parties.
- Consider adding (or using) a character (or phrase) that indicates that the message was sent under duress.
"""

class OTP(App):
    """One Time Pad"""

    BINDINGS = [
        ("1", "show_tab('encode')", "Encode"),
        ("2", "show_tab('decode')", "Decode"),
        ("3", "show_tab('generate')", "Generate"),
        ("4", "show_tab('settings')", "Settings"),
        ("5", "show_tab('about')", "About"),
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        """Compose app with tabbed content."""
        # Footer to show keys
        yield Footer()

        # Add the TabbedContent widget
        with TabbedContent(initial="encode"):
            with TabPane("Encode", id="encode"):  # First tab
                yield Markdown(ENCODE)  # Tab content
            with TabPane("Decode", id="decode"):
                yield Markdown(DECODE)
            with TabPane("Generate", id="generate"):
                yield Markdown(GENERATE)
            with TabPane("Settings", id="settings"):
                yield Markdown(SETTINGS)
            with TabPane("About", id="about"):
                yield Markdown(ABOUT)

    def action_show_tab(self, tab: str) -> None:
        """Switch to a new tab."""
        self.get_child_by_type(TabbedContent).active = tab


if __name__ == "__main__":
    app = OTP()
    app.run()
