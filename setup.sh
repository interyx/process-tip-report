#! /bin/bash

python3 -m venv .venv
source .venv/bin/activate
python3 install -r requirements.txt
deactivate
echo "Tool installed successfully"
