## Introduction

Shamsi Time is a simple Electron application that displays the current date in the Shamsi (Jalaali) calendar as a notification. It's designed to run on various operating systems and provides a convenient way to keep track of dates in the Jalaali calendar.

## Features

-   Displays the current Shamsi date as a system notification.
-   Runs in the system tray for easy access.
-   Customizable notification content with Shamsi date.
-   Simple and lightweight.

## Getting Started

### Prerequisites

-   Node.js (preferably the latest version)
-   npm (usually comes with Node.js)

### Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory in your terminal.
3. Run `npm install` to install the necessary dependencies.

### Running the App

-   Use `npm start` to run the application.

### Packaging the App

-   For packaging the application, you can use `npm run package`. This will create a distributable package in the output directory.

## Scripts

-   `"start": "electron-forge start"` - Starts the Electron app.
-   `"package": "electron-forge package"` - Packages the app into a distributable format.
-   `"make": "electron-forge make"` - Generates platform-specific make targets.

## Dependencies

-   `electron` - The core framework.
-   `jalaali-js` - A library for converting Gregorian dates to Jalaali.
-   `electron-squirrel-startup` - Handles startup events for Electron apps packaged for Windows.

## Development Notes

-   The app uses `electron-squirrel-startup` for handling startup events on Windows.
-   Jalaali date conversion is handled by the `jalaali-js` library.
-   The application is structured to quit when all windows are closed, except on macOS (Darwin platform).

## Contributions

Contributions are welcome. Please submit pull requests or issues to the GitHub repository.
