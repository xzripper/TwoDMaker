class CSS:
    """Blank CSS code."""

    wmodern = "font-family: 'Courier New', Courier, monospace;\nborder-radius: 2px;\nbackground-color: rgb(200, 200, 200);\n"
    dmodern = "font-family: 'Courier New', Courier, monospace;\nborder-radius: 2px;\nbackground-color: rgb(120, 120, 120);\ncolor: white;\n"
    bradiusw = "border-radius: 2px;\nbackground-color: rgb(200, 200, 200);\ncolor: black;\n"
    bradiusd = "border-radius: 2px;\nbackground-color: rgb(100, 100, 100);\ncolor: white;\n"
    bradiusg = "border-radius: 2px;\nbackground-color: rgb(108, 108, 108);\ncolor: white;\n"

    def add(self, name: str, code: str) -> None:
        """Add new css class."""
        self.__dict__.update({name: code})
