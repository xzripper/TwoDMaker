from typing import Union

from configparser import ConfigParser

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Window:
    """Tools for window creation."""

    path = (('\\'.join(__file__.split('\\')[:-2])) + '\\')

    def new(self, *args: tuple[object]) -> None:
        """Create new window."""
        self.application = QApplication(list(args))
        self.window = QWidget()

    def size(self, appsize: list[int]=None) -> Union[None, tuple[int]]:
        """Get size or set size of app."""
        if appsize is None:
            return (self.window.frameGeometry().width(), self.window.frameGeometry().height())

        elif appsize is not None:
            self.window.resize(*appsize)

    def pos(self, windpos: list[int]=None) -> Union[None, tuple[int]]:
        """Get or set position of app."""
        if windpos is None:
            return (self.window.frameGeometry().x(), self.window.frameGeometry().y())

        elif windpos is not None:
            self.window.move(*windpos)

    def resizable(self, maxres: list[int]=None, minres: list[int]=None) -> Union[None, tuple[int]]:
        """Set or get resizable geometry of app."""
        if maxres is None and minres is None:
            return (self.window.maximumWidth(), self.window.maximumHeight())

        elif maxres is not None and minres is not None:
            self.window.setMaximumSize(*maxres)
            self.window.setMinimumSize(*minres)

    def title(self, title: str=None) -> Union[None, str]:
        """Set or get title of app."""
        if title is None:
            return self.window.windowTitle()

        elif title is not None:
            self.window.setWindowTitle(title)

    def icon(self, icon: str=None) -> Union[None, str]:
        """Set or get icon of app."""
        if icon is None:
            return self.window.windowIcon()

        elif icon is not None:
            if icon == 'EngineBlank':
                self.window.setWindowIcon(QIcon(f'{self.path}window\\Icon.png'))

            else:
                self.window.setWindowIcon(QIcon(icon))

    def fromini(self, file: str) -> None:
        """Set up window from ini."""
        if file == 'EngineBlank':
            file = f'{self.path}window\\Window.ini'

        parsed = ConfigParser()
        parsed.read(file)

        if hasattr(self, 'application') and hasattr(self, 'window'):
            self.delete()

        self.new()

        self.title(parsed['Window']['Title'])
        self.icon(parsed['Window']['Icon'])
        self.size([int(parsed['Geometry']['Width']), int(parsed['Geometry']['Height'])])
        self.pos([int(parsed['Positions']['DotX']), int(parsed['Positions']['DotY'])])
        self.resizable([int(parsed['GeometrySettings']['MaxWidth']), int(parsed['GeometrySettings']['MaxHeight'])], [int(parsed['GeometrySettings']['MinWidth']), int(parsed['GeometrySettings']['MinHeight'])])

    def data(self) -> tuple:
        """Get window and app."""
        return (self.application, self.window)

    def delete(self) -> None:
        """Delete window data."""
        del self.application, self.window

    def windraise(self) -> None:
        """Raise window."""
        self.window.show()

    def windexec(self) -> None:
        """Execute window."""
        exit(self.application.exec_())

    def windrun(self) -> None:
        """Run window."""
        self.windraise()
        self.windexec()
