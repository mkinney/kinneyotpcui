from textual.app import App, ComposeResult
from textual.widgets import Footer, Input, Label, Markdown, TabbedContent, TabPane
from textual.widget import Widget
from textual.reactive import reactive

from kinneyotp import OTP

# TODO: generate form
GENERATE = """
Generate form goes here
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

class Form(App):
    """One Time Pad"""

    otp = OTP()

    # Note: Using numbers to switch tabs quickly since the default alphabet does not contain numbers.
    BINDINGS = [
        ("1", "show_tab('encode')", "Encode"),
        ("2", "show_tab('decode')", "Decode"),
        ("3", "show_tab('generate')", "Generate"),
        ("4", "show_tab('settings')", "Settings"),
        ("5", "show_tab('about')", "About"),
        ("6", "quit", "Quit"),
    ]


    def render(self) -> str:
        return f"Hello, {self.who}!"

    def compose(self) -> ComposeResult:
        """Compose app with tabbed content."""
        # Footer to show keys
        yield Footer()

        # Add the TabbedContent widget
        with TabbedContent(initial="encode"):
            with TabPane("Encode", id="encode"):
                yield Input(placeholder="Text", id="text")
                yield Input(placeholder="Key", id="key")
                yield Input(placeholder="Encoded", disabled=True, id="encoded")
                yield Input(placeholder="", disabled=True, id="message")
            with TabPane("Decode", id="decode"):
                yield Input(placeholder="Text to decode", id="dtext")
                yield Input(placeholder="Key", id="dkey")
                yield Input(placeholder="Decoded", disabled=True, id="decoded")
                yield Input(placeholder="", disabled=True, id="dmessage")
            with TabPane("Generate", id="generate"):
                yield Markdown(GENERATE)
            with TabPane("Settings", id="settings"):
                yield Input(placeholder="Alphabet", disabled=True, id="alphabet")
            with TabPane("About", id="about"):
                yield Markdown(ABOUT)

    def on_mount(self) -> None:
        """Set the alphabet when the form starts."""
        alphabet = self.query_one("#alphabet")
        alphabet.value = "Alphabet: " + self.otp.alphabet

    def update_encoded(self):
        # Update the encoded value
        text = self.query_one("#text")
        key = self.query_one("#key")
        encoded = self.query_one("#encoded")
        message = self.query_one("#message")

        # force upper
        text.value = text.value.upper()
        key.value = key.value.upper()

        # TODO: only limit to what is in the otp.alphabet()?

        if len(text.value) <= len(key.value):
            self.otp.key = key.value
            message.value, encoded_text = self.otp.encode(text.value)
            encoded.value = encoded_text
        else:
            message.value = "The length of the text must be shorter or the same length as the key."
            encoded.value = ""

    def update_decoded(self):
        # Update the decoded value
        text = self.query_one("#dtext")
        key = self.query_one("#dkey")
        decoded = self.query_one("#decoded")
        message = self.query_one("#dmessage")

        # force upper
        text.value = text.value.upper()
        key.value = key.value.upper()

        # TODO: only limit to what is in the otp.alphabet()?

        if len(text.value) <= len(key.value):
            self.otp.key = key.value
            message.value, decoded_text = self.otp.decode(text.value)
            decoded.value = decoded_text
        else:
            message.value = "The length of the text must be shorter or the same length as the key."
            decoded.value = ""

    def on_input_changed(self, event: Input.Changed) -> None:
        if event.input.id == "text" or event.input.id == "key":
            self.update_encoded()
        if event.input.id == "dtext" or event.input.id == "dkey":
            self.update_decoded()

    def action_show_tab(self, tab: str) -> None:
        """Switch to a new tab."""
        self.get_child_by_type(TabbedContent).active = tab


if __name__ == "__main__":
    app = Form()
    app.run()
