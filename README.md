<p align="center"><img src="https://user-images.githubusercontent.com/94743980/147131413-1a22c60d-e875-45ac-a63a-1854fcf64baa.png"></p>

# TwoDMaker (2DMaker) - Simple engine for 2D games making!
Create simple games (or ui) in one hour!

# About.
This is a simple engine for game or gui app creation.<br>
Haves many blankes, for fast developing.<br>
Inherits <a href="https://riverbankcomputing.com/software/pyqt/">PyQt5</a>, more precisely based on it.<br>

# Install.
Install code,<br>
Rename TwoDMaker-main to TwoDMaker,<br>
Move it to $PYTHON_PATH\lib\,<br>
Done!

# Example.
Lets make a simple app!
It's have infinity spinning animation in window!
Let's create main.py, and download <a href="https://i.gifer.com/XPFZ.gif">Animation.gif</a>

```python
# Importing engine classes.
from TwoDMaker.window import Window # For window.
from TwoDMaker.widgets import Widget, QLabel # For widgets.
from TwoDMaker.assets import Asset # For assets importing.


app_window = Window() # Create new window instance.
app_window.new() # Create new window.

app_window.title('Simple animation.') # Set title for window.
app_window.icon('EngineBlank') # Set engine icon.

app_window.size([400, 220]) # Set window size.
app_window.pos([1000, 400]) # Set window pos.

app_window.resizable([400, 220], [400, 220]) # Set window resizable frames.

app_window.window.setWindowFlag(Asset('Engine', 'QtCore').get().Qt.FramelessWindowHint, True) # Remove window hat.

animation = Asset('Engine', 'QtGui').get().QMovie(app_window.data()[1]) # Import movies class.
animation.setFileName('Animation.gif') # Set animation.
animation.setSpeed(100) # Set speed of animation.
animation.start() # Start animation.

animation_widget = Widget() # Creating new widget instance.
animation_widget.new(QLabel, parent=app_window.data()[1]) # Creating animation, but this anyway widget.
animation_widget.get().setMovie(animation) # Set animation to widget.

app_window.windraise() # Raise window.
app_window.windexec() # Execute window.

```

Result <a href="https://drive.google.com/file/d/196RAtbqFKqXR8rcnAubkFO32FElgoIaY/view?usp=sharing">is...</a>

# End.
Thanks for reading, have a good day, bye!
