#!/bin/bash

echo "Starting build process..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Package app (optional zip)
zip -r app.zip *.py

echo "Build complete. Application packaged as app.zip."
