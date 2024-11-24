from pywinauto import Application
from pywinauto.keyboard import send_keys
import time
import os
import shutil
import textwrap

def main():
    while True:
        title = input("Please enter the title of your game as shown in the FrankenDrift window. Upper- and lower case matters. For example, if the title bar says \"My Game - FrankenDrift\", you have to type \"My Game\"\ntitle: ")
        if title == "quit":
            return
        try:
            app = Application().connect(title=title + " - FrankenDrift")
            break
        except:
            print("An error occured. Please try again.")
    main_window = app.window(title=title + " - FrankenDrift")
    controls = main_window.descendants()
    inputField = controls[4]
    outputField = controls[3]
    statusField = controls[5]
    showOutput = True
    while True:
        try:
            columns, _ = shutil.get_terminal_size(fallback=(80, 24))  # Fallback to 80x24 if size cannot be determined
            result = outputField.window_text()
            new = result.split("Ø")[-1].strip()
            lines = new.splitlines()
            new = "\n".join(lines[1:])
            if showOutput:
                print(textwrap.fill(new, width=columns))
            showOutput = True
            command = input(">")
            if command == "quit":
                return
            if command == "stats":
                print(statusField.window_text().strip())
                showOutput = False
                continue
            inputField.set_text(command)
            inputField.send_keystrokes("{ENTER}")
            time.sleep(0.1)
        except:
            input("Connection to FrankenDrift lost. Press enter to quit.")
            return

if __name__ == "__main__":
    main()