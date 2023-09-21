import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode == 0:
        print("Command executed successfully")
        print("Output:\n", result.stdout)
        return result.stdout
    else:
        print("Command failed")
        print("Error:\n", result.stderr)
        return result.stderr