#!/bin/bash
echo "Setting up Django on PythonAnywhere..."

# Install mysqlclient dependencies
sudo apt-get update
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

# Create virtual environment
python3.13 -m venv venv
source venv/bin/activate

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Create directories
mkdir -p media media/uploads static staticfiles

echo "Setup complete! Don't forget to:"
echo "1. Create MySQL database in PythonAnywhere dashboard"
echo "2. Set environment variables in Web tab"
echo "3. Run: python manage.py migrate"
echo "4. Run: python manage.py collectstatic"