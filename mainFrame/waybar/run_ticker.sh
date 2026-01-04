#!/bin/bash

source ~/.config/waybar/.venv/bin/activate
python3 ~/.config/waybar/ticker.py "$@"
