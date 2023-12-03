@echo off
REM Build the executable using pyinstaller
pyinstaller --onefile --noconsole script.py

REM Delet build directory and script.spec
rmdir /s /q build
del script.spec

REM Rename the .exe file
rename dist\script.exe "Shamsi time".exe

REM Create build directory if it doesn't exist
if not exist build mkdir build

REM Move the Shamsi time.exe file to the build directory
move dist\"Shamsi time".exe build

REM Copy the icons to the build directory
copy config.txt build
xcopy assets build\assets /E /I

REM Delete dist file
rmdir /s /q dist

echo Build creation complete!
pause