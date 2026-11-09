#!/bin/bash

set -e

if [ ! -d .venv ]; then
    python -m venv .venv
fi

source .venv/bin/activate
pip install -q -r requirements.txt
echo "All dependencies are ready"

python main.py
