#!/bin/bash

# Create a Python3 virtualenv called cosmocloud_anuj
python -m venv .cosmocloud_anuj

# Activate the virtualenv
source .cosmocloud_anuj/bin/activate

# Install requirements using pip
pip install -r requirements.txt

# populate products db
python populate_database.py

# run the server
uvicorn main:app --reload