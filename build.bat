@echo off
REM Build the executable using pyinstaller
pyinstaller --onefile --noconsole script.py

REM Rename the .exe file
rename dist\script.exe script.exe

REM Create "Shamsi time" directory if it doesn't exist
if not exist "Shamsi time" mkdir "Shamsi time"

REM Move the script.exe file to the "Shamsi time" directory
move dist\script.exe "Shamsi time"

REM Copy the icons to the "Shamsi time" directory
copy config.txt "Shamsi time"
xcopy assets "Shamsi time\assets" /E /I

REM Cleanup
rmdir /s /q build
rmdir /s /q dist
del script.spec

echo Build creation complete!
pause