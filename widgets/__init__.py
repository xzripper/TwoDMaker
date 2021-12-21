from PyQt5.QtWidgets import *


class Widget:
    """Tools for widget creation."""

    def new(self, wtype: QWidget, **settings: dict[object]) -> None:
        """Create new widget."""
        assert None if wtype.__bases__ == () else None if wtype.__bases__[0].__bases__ == () else wtype.__bases__[0].__bases__[0] == QWidget, 'not widget'

        self.widget = wtype(**settings)

    def get(self) -> QWidget:
        """Get widget."""
        return self.widget

    def delete(self) -> None:
        """Delete widget data."""
        del self.widget
