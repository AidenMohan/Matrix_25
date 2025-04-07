import subprocess
import time
import sys
import os
import shlex
import random
from screeninfo import get_monitors

NUM_TERMINALS = 5
DELAY_SECONDS = 0.3
SCRIPT_TO_RUN = "matrix_display.py"

if not os.path.exists(SCRIPT_TO_RUN):
    print(f"Error: The script '{SCRIPT_TO_RUN}' was not found in this directory.")
    print("Please make sure both 'launch_terminals.py' and 'matrix_display.py' are together.")
    sys.exit(1)

python_executable = sys.executable
script_path = os.path.abspath(SCRIPT_TO_RUN)
base_command = [python_executable, script_path]

def get_random_position():
    monitors = get_monitors()
    if not monitors:
        return 100, 100
    primary_monitor = None
    for monitor in monitors:
        if monitor.is_primary:
            primary_monitor = monitor
            break
    if not primary_monitor:
        primary_monitor = monitors[0]

    width = primary_monitor.width
    height = primary_monitor.height
    window_width = 600
    window_height = 400
    x = random.randint(50, width - window_width - 50)
    y = random.randint(50, height - window_height - 50)
    return x, y

for i in range(NUM_TERMINALS):
    try:
        if sys.platform == "win32":
            subprocess.Popen(['start', 'python', script_path], shell=True)

        elif sys.platform == "darwin":
            import random
            from screeninfo import get_monitors
            monitors = get_monitors()
            if monitors:
                primary_monitor = monitors[0]
                width = primary_monitor.width
                height = primary_monitor.height
                window_width = 600
                window_height = 400
                x = random.randint(50, width - window_width - 50)
                y = random.randint(50, height - window_height - 50)
                quoted_script_path = shlex.quote(script_path)
                osascript_command = f'tell app "Terminal" to do script "python {quoted_script_path}"\nset bounds of window 1 to {{{x}, {y}, {x + 600}, {y + 400}}}'
                subprocess.Popen(['osascript', '-e', osascript_command])
            else:
                quoted_command = " ".join(shlex.quote(part) for part in base_command)
                osascript_command = f'tell app "Terminal" to do script "{quoted_command}"'
                subprocess.Popen(['osascript', '-e', osascript_command])

        else:
            import random
            from screeninfo import get_monitors
            monitors = get_monitors()
            x = 100
            y = 100
            if monitors:
                primary_monitor = monitors[0]
                width = primary_monitor.width
                height = primary_monitor.height
                window_width = 600
                window_height = 400
                x = random.randint(50, width - window_width - 50)
                y = random.randint(50, height - window_height - 50)

            terminal_commands = [
                ['gnome-terminal', '--geometry', f'{window_width}x{window_height}+{x}+{y}', '--', '-e'],
                ['konsole', '--separate', '--geometry', f'{window_width}x{window_height}+{x}+{y}', '-e'],
                ['xfce4-terminal', '--geometry', f'{window_width}x{window_height}+{x}+{y}', '-x'],
                ['xterm', '-geometry', f'{window_width}x{window_height}+{x}+{y}', '-e']
            ]
            launched = False
            for term_cmd in terminal_commands:
                try:
                    full_cmd = term_cmd + base_command
                    subprocess.Popen(full_cmd)
                    launched = True
                    break
                except FileNotFoundError:
                    continue

            if not launched:
                print(f"Error: Could not find a known terminal emulator for random positioning.")
                subprocess.Popen(base_command)

    except Exception as e:
        print(f"Error launching terminal {i + 1}: {e}")

    time.sleep(DELAY_SECONDS)
