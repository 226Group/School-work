import subprocess
import sys

from libs.env_pointer import *

chosen_script = EnvVarPointer("CHOSEN_SCRIPT")

# Check for run arguments
if len(sys.argv) > 1:
    # Set the environment variable to the first argument
    chosen_script.value = sys.argv[1]

# Prompt the user for input with a timeout of 5 seconds
chosen_script = (get_input("Please enter the script name (you have 3 seconds): ", 3) 
    or chosen_script)
    #TODO bad cause shuts user

# Now, run the script based on the user's choice
if chosen_script.value is not None:
    subprocess.run(["python", chosen_script.value])
else:
    print("No script selected via env var, argument or user input. Please enter a script filename.")