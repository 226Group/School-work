import os

import thread as threading


class EnvVarPointer:
    def __init__(self, var_name):
        self.var_name = var_name

    @property
    def value(self):
        return self.value

    @value.getter
    def value(self):
        return os.environ.get(self.var_name)
        
    @value.setter
    def value(self, new_value):
        os.environ[self.var_name] = new_value


# # Create a pointer to the environment variable
# chosen_script_pointer = EnvVarPointer("CHOSEN_SCRIPT")

# # Access the value through the pointer
# print(f"The chosen script is: {chosen_script_pointer.value}")

# # Update the environment variable through the pointer
# chosen_script_pointer.value = "new_script.py"
# print(f"The updated chosen script is: {chosen_script_pointer.value}")

# # Verify the change directly from os.environ
# print(f"Direct access: {os.environ['CHOSEN_SCRIPT']}")

def get_input(prompt, timeout):
    """Function to get user input with a timeout."""
    print(prompt)
    user_input = []

    def input_thread():
        user_input.append(input())  # Capture user input

    thread = threading.Thread(target=input_thread)
    thread.start()
    thread.join(timeout)  # Wait for the thread to finish or timeout

    if thread.is_alive():
        print("No input received, proceeding with default.")
        return None  # No input received
    else:
        return user_input[0]  # Return the input
