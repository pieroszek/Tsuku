import os

def add_function_to_shell_profiles():
    # Define the function to add
    function_definition = '''
# Function to run main.py with arguments
t() {
    python3 "{path}/main.py" "$@"
}
'''.strip().format(path=os.path.abspath(os.path.dirname(__file__)))

    # Paths to shell profiles
    bash_profile = os.path.expanduser("~/.bash_profile")
    zshrc = os.path.expanduser("~/.zshrc")

    # Function to append to a profile if not already added
    def append_to_profile(profile_path):
        if os.path.exists(profile_path):
            with open(profile_path, "r") as file:
                content = file.read()
            if function_definition in content:
                print(f"The function is already in {profile_path}")
                return
        else:
            content = ""

        with open(profile_path, "a") as file:
            file.write("\n\n" + function_definition)
        print(f"Added the function to {profile_path}. Remember to source it!")

    # Append to bash_profile and zshrc
    append_to_profile(bash_profile)
    append_to_profile(zshrc)

if __name__ == "__main__":
    add_function_to_shell_profiles()

