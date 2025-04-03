import subprocess

def select_folder():
    result = subprocess.run(['zenity', '--file-selection', '--directory'], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else None
    print(result)

select_folder()

