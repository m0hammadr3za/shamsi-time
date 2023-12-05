# Shamsi Time

Shamsi Time is a straightforward application designed to display the current date in the Persian calendar (Jalali calendar) as a system notification on your desktop. This utility provides an easy way to view the current Persian day of the week, month, and date.

## Features

-   Displays the Persian date in the system tray.
-   Provides easy access to the current day of the week, month name, and date in Persian.
-   Clicking the tray icon shows a notification with the full date.
-   Right-click menu with an exit option.

## Pre-built Executable

For simplicity, a pre-built executable is available in the Releases section of this repository.

1. Go to the [Releases](https://github.com/m0hammadr3za/shamsi-time/releases) section.
2. Download the latest version of `Shamsi time.exe`.
3. Optionally, to run the application at startup, follow the instructions in the 'Running on Startup' section.

## Building from Source

If you prefer building from source or contributing to the project, follow these steps:

1. Clone this repository or download the source code.
2. Navigate to the downloaded folder and run the build.bat script. This uses PyInstaller to create a standalone executable from `script.py`.
   Prerequisites

## Dependencies

-   Python
-   PyQt5
-   jdatetime
-   PyInstaller

## Running on Startup

On startup, you can run the `script.py` file if you have the dependencies installed, or you can run the executable that was built from `script.py`.

## Windows

To run Shamsi Time on startup in Windows:

1. Press Win+R, type shell:startup, and press Enter. This opens the Startup folder.
2. Create a shortcut to the `Shamsi time.exe` file in this folder.

## Linux

For Linux systems using a graphical desktop environment:

1. Open the Startup Applications Preferences window.
2. Click Add and then Choose File. Navigate to the `Shamsi time.exe` file.
3. Add a name and comment and click Add.
