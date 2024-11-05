# NihatGicikleme2000

This program creates pop-up messages that humorously poke fun at a user named "Nihat" with different messages based on the time of day. It also runs at startup, creating regular notifications using a graphical interface. The app was developed in Python and uses the `tkinter` library for its graphical interface, as well as Windows Registry modifications to add the app to startup.

## Features

- **Dynamic Pop-Ups**: Displays random, time-specific messages in a small pop-up window that follows the mouse cursor.
- **Auto Start**: The program automatically adds itself to the Windows startup list to run whenever the system starts.
- **Keyboard Control**: The program can be closed using the shortcut `CTRL+SHIFT+Q`.
- **Fun, Personalized Messages**: Randomized messages are selected from different categories like morning, class time, and evening.

## Requirements

- Python 3.x
- Libraries:
  - `tkinter` for GUI
  - `random`, `datetime`, `os`, `sys` (Python standard libraries)
  - `winreg` for Windows Registry access
  - `pywin32` (for managing window visibility)

### Installation

1. Clone the repository or download the `NihatGicikleme2000.py` file.
2. Install the required libraries:
    ```bash
    pip install pywin32
    ```
3. Run the program by executing:
    ```bash
    python NihatGicikleme2000.py
    ```

## How to Use

1. **Run the Program**: Launch `NihatGicikleme2000.py`.
2. **Control Pop-Ups**:
   - The program will display pop-ups every 0.5 seconds.
   - To close the program, press `CTRL+SHIFT+Q`.

### Important Notes

- **Startup**: The program registers itself to start automatically each time the computer boots. To disable this, manually remove the entry in the Windows Registry under `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`.
- **Platform**: This program is Windows-specific due to its dependency on the Windows Registry and Win32 API functions.

## License

This project is licensed under the MIT License.
