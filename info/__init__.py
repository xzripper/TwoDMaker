class Info:
    """Engine info."""

    author = 'Ivan Perzhinsky'
    licens = 'MIT License'
    version = 1.2
    cyear = 2021

    def get(self) -> str:
        """Get information."""
        return f'{self.author}, {self.licens}, {self.version}, {self.cyear}.'
