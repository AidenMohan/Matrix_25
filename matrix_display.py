# matrix_display.py
import time
import random
import os
import sys

# --- Configuration ---
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()[]{};:'\",.<>/?"
DENSITY = 0.04  # Lower value = fewer characters starting per frame (adjust for speed/look)
FALL_SPEED = 0.08 # Base delay between screen updates (lower = faster)
RANDOM_SPEED_ADD = 0.05 # Add random amount to delay for variation

# --- Platform Specific Setup ---
if sys.platform == "win32":
    # On Windows, try to set console color to green on black
    os.system('color 0A')
    # ANSI escape codes for color might not work reliably in standard cmd.exe
    # but might work in Windows Terminal or other emulators.
    GREEN = ''
    RESET = ''
    # Try to enable ANSI support on newer Windows versions
    os.system('') # This can enable ANSI processing in some environments
    # If colors dont work in cmd, GREEN/RESET below might help in WT/others
    # GREEN = '\033[92m'
    # RESET = '\033[0m'

else:
    # On Linux/macOS, use ANSI escape codes for green text
    GREEN = '\033[92m'
    RESET = '\033[0m'

# --- Main Loop ---
try:
    # Get terminal dimensions (best effort)
    try:
        width, height = os.get_terminal_size()
    except OSError:
        width = 80  # Default fallback width
        height = 24 # Default fallback height

    # Initialize columns with random starting points for the "drops"
    columns = [random.randint(-height * 2, height // 2) for _ in range(width)]

    while True:
        output = ""
        for x in range(width):
            # Select a random character
            char = random.choice(CHARS)

            # Current position in the column
            current_pos = columns[x]

            # Add character if it's within the visible height range
            if 0 <= current_pos < height:
                # Move cursor to position (ANSI escape), print char
                # This avoids printing the whole screen line by line, looks better
                output += f"\033[{current_pos + 1};{x + 1}H{GREEN}{char}{RESET}"

            # Update column position
            columns[x] += 1

            # Reset column if it goes way past the bottom or randomly
            if columns[x] > height + random.randint(5, 20) or random.random() < DENSITY / 5:
                 columns[x] = random.randint(-height, 0) # Reset to top or above

        # Print all characters for this frame at once
        print(output, end='', flush=True)

        # Small delay
        time.sleep(FALL_SPEED + random.uniform(0, RANDOM_SPEED_ADD))

# ... code before ...
except Exception as e: # This is line 72
    # Lines below MUST be indented
    print(f"\nAn error occurred: {e}") # Indented 4 spaces
    if sys.platform == "win32":        # Indented 4 spaces
        # This line belongs to the 'if', so it's indented more
        os.system('color')           # Indented 8 spaces total
    print("\033[?25h" + RESET)        # Indented 4 spaces
# ... code after ...