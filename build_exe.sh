#!/bin/bash
# Build script for Linux/Mac

echo "================================"
echo "  Building YouTube Downloader"
echo "================================"
echo ""

echo "Step 1: Installing PyInstaller..."
pip install pyinstaller

echo ""
echo "Step 2: Building executable..."
pyinstaller --onefile --console --name "youtube_downloader" youtube_downloader.py

echo ""
echo "================================"
echo "  Build complete!"
echo "================================"
echo ""
echo "Your executable is ready at:"
echo "  dist/youtube_downloader"
echo ""
