#!/bin/bash

# Function to print the current keyboard layout in Hyprland with fixed length
function print_keymap() {
    current_keymap=$(hyprctl devices -j | jq -r '.keyboards[] | select(.main == true) | .active_keymap')
    printf " %-13s\n" "$current_keymap"
}

# Call the function
print_keymap

