#!/bin/bash

# Build the executable
pyinstaller --onefile \
            --noconsole \
            script.py

# Rename the .exe file
mv dist/script.exe dist/shamsi-time.exe

# Create "Shamsi time" directory if it doesn't exist
mkdir -p "Shamsi time"

# Move the renamed .exe file to the "Shamsi time" directory
mv dist/shamsi-time.exe "Shamsi time"/

# Copy the icon.ico file to the "Shamsi time" directory
cp icon.ico "Shamsi time"/

# Cleanup
rm -rf build dist script.spec

echo "Build complete!"
