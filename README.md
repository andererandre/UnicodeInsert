UnicodeInsert
=============

UnicodeInsert is a Sublime Text package to insert special characters by either Unicode name or LaTeX command.

Default Hotkeys
---------------

- Mac OS X: **cmd+shift+c**
- Windows: **alt+shift+c**
- Linux: **super+shift+c**

How It Works
------------

Just open the input panel using the defined hotkey and enter either a valid Unicode character name (e.g. SQUARE ROOT) or a LaTeX command (e.g. \sqrt) and hit enter. The package then tries to replace your input with the corresponding Unicode character.

- If the entered string starts with a backslash:
  * Use a lookup table that contains some of the most commonly used LaTeX commands
- Otherwise:
  * Use the Python function unicodedata.lookup()

If you feel there's a LaTeX command missing, feel free add it to the lookup table and send me a pull request.

Screenshots
-----------

![screenshot-01.png](https://raw.github.com/modmonkeys/UnicodeInsert/master/img/screenshot-01.png "Screenshot 01")
