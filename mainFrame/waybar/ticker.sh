
#!/bin/bash

# Define the list of elements
elements=("QQQ" "SPY" "SQQQ")

# File to keep track of the current index
index_file="current_index.txt"

# Check if the index file exists, if not create it and initialize with 0
if [ ! -f "$index_file" ]; then
  echo 0 > "$index_file"
fi

# Read the current index
current_index=$(cat "$index_file")

# Get the next element in the list
next_element=${elements[$current_index]}
source ~/.config/waybar/.venv/bin/activate
# Run the Python script with the next elements
python3 ~/.config/waybar/ticker.py "$next_element"

# Update the index for the next run
next_index=$(( (current_index + 1) % ${#elements[@]} ))
echo $next_index > "$index_file"
