@echo off
echo.
echo ========================================
echo  Building YouTube Downloader .exe
echo ========================================
echo.

echo Step 1: Installing PyInstaller...
pip install pyinstaller

echo.
echo Step 2: Building .exe file...
pyinstaller --onefile --console --name "YouTube Downloader" youtube_downloader.py

echo.
echo ========================================
echo  Build complete!
echo ========================================
echo.
echo Your .exe file is ready at:
echo   dist\YouTube Downloader.exe
echo.
pause
