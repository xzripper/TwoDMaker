from PyQt5.QtWidgets import *


class Widget:
    """Tools for widget creation."""

    def new(self, wtype: QWidget, **settings: dict[object]) -> None:
        """Create new widget."""
        self.widget = wtype(**settings)

    def get(self) -> QWidget:
        """Get widget."""
        return self.widget

    def delete(self) -> None:
        """Delete widget data."""
        del self.widget
