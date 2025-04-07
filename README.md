# Matrix_25
makes a funny matrix effect on win11 
## Use Guide for `launch_terminals.py`

This guide explains how to use the `launch_terminals.py` script to open multiple terminal windows and run another Python script (by default, `matrix_display.py`) in each.

**Prerequisites:**

* **Python Installation:** Ensure you have Python 3 installed on your system.
* **`screeninfo` Library (Optional for Random Positioning):** If you want the terminals to attempt to open in random positions (this works best on macOS and Linux), you need to install the `screeninfo` library. You can install it using pip:
   ```bash
   pip install screeninfo
## Troubleshooting Guide for `launch_terminals.py`

This guide provides steps to troubleshoot common issues you might encounter while running the `launch_terminals.py` script.

### 1. Script Not Found Errors

**Problem:** You see an error message like:
Error: The script 'matrix_display.py' was not found in this directory.
**Solution:**
* Ensure that both `launch_terminals.py` and `matrix_display.py` are located in the **exact same directory**.
* Double-check the spelling of `SCRIPT_TO_RUN` in `launch_terminals.py`. It must perfectly match the filename of your matrix display script (case-sensitive on some operating systems).

### 2. Terminals Not Opening (Windows)

**Problem:** When running on Windows, no new terminal windows appear.

**Possible Solutions:**
* **Check `matrix_display.py`:** Even if it works individually, ensure there are no errors that cause it to exit immediately when launched by `launch_terminals.py`. Try running `python matrix_display.py` from a command prompt in the same directory.
* **Permissions:** Ensure Python has the necessary permissions to execute scripts and open new processes.
* **Antivirus:** In rare cases, antivirus software might interfere with the script's ability to launch multiple processes. Temporarily disable it (with caution) to see if that resolves the issue. If it does, you might need to add an exception for your Python scripts.

### 3. Terminals Open and Crash Immediately (Windows)

**Problem:** New terminal windows appear briefly and then close.

**Possible Solutions:**
* **Error in `matrix_display.py` when run concurrently:** Even if it works alone, the script might have issues when multiple instances run simultaneously.
    * **Run manually:** Open multiple command prompts and run `python matrix_display.py` in each to see if they crash. This can help isolate if the issue is with concurrency.
    * **Resource contention:** The `matrix_display.py` script might be consuming too many resources (CPU, memory, output) when run multiple times. Try reducing `NUM_TERMINALS` in `launch_terminals.py`.
    * **Infinite loops/Rapid output:** If `matrix_display.py` has a very tight loop without delays, it could overwhelm the terminal. Try adding a small `time.sleep()` within its main loop for testing.
    * **Global variables/Shared state:** If `matrix_display.py` uses globals or shared resources unsafely, concurrent access could cause crashes.
