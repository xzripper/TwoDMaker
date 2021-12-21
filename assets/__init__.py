class Asset:
    engine = 'Engine'
    doall = '*'

    def __init__(self, source: str, do: str) -> None:
        """Import asset."""
        source = source.replace('Engine', 'PyQt5')

        if do == '*':
            self.imported = __import__(source)

        else:
            self.imported = getattr(__import__(source), do)

    def get(self) -> object:
        """Get imported asset."""
        return self.imported
