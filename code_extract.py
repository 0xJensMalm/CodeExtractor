import os
import inquirer
import pyperclip

def display_ascii_title():
    title = """
                                                                                                       
 ,-----.          ,--.           ,------.            ,--.                         ,--.                 
'  .--./ ,---.  ,-|  | ,---.     |  .---',--.  ,--.,-'  '-.,--.--. ,--,--. ,---.,-'  '-. ,---. ,--.--. 
|  |    | .-. |' .-. || .-. :    |  `--,  \  `'  / '-.  .-'|  .--'' ,-.  || .--''-.  .-'| .-. ||  .--' 
'  '--'\' '-' '\ `-' |\   --.    |  `---. /  /.  \   |  |  |  |   \ '-'  |\ `--.  |  |  ' '-' '|  |    
 `-----' `---'  `---'  `----'    `------''--'  '--'  `--'  `--'    `--`--' `---'  `--'   `---' `--'    
                                                                                                       
    """
    print(title)

def get_folder_path():
    while True:
        folder_path = input("Input folder path: ")
        if os.path.isdir(folder_path):
            return folder_path
        else:
            print("Invalid folder path. Please try again.")

def select_file_types():
    print("Use the arrow keys to navigate, Spacebar to select, and Enter to confirm.")
    questions = [
        inquirer.Checkbox('file_types',
                          message="Select file types",
                          choices=['html', 'css', 'js', 'py'])
    ]
    answers = inquirer.prompt(questions)
    return answers['file_types']

def list_files(folder_path, file_types):
    output = "Folder structure:\n"
    folder_structure = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.endswith(f".{ext}") for ext in file_types):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                directory = os.path.dirname(relative_path)
                if directory not in folder_structure:
                    folder_structure[directory] = []
                folder_structure[directory].append(os.path.basename(file_path))
    
    for directory, files in folder_structure.items():
        output += f"{directory}:\n"
        for file in files:
            output += f"- {file}\n"
    
    return output

def run_script(folder_path, file_types):
    output = list_files(folder_path, file_types)
    selected_files = []
    code_output = "\nCode:\n\n"
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if any(file.endswith(f".{ext}") for ext in file_types):
                file_path = os.path.join(root, file)
                selected_files.append(file_path)
                relative_path = os.path.relpath(file_path, folder_path)
                code_output += f"{relative_path}:\n"
                with open(file_path, 'r') as file:
                    code_output += file.read() + "\n\n"
    
    output += code_output
    return output

def copy_to_clipboard(output):
    pyperclip.copy(output)
    print("Output copied to clipboard.")

def main():
    display_ascii_title()
    folder_path = get_folder_path()
    file_types = select_file_types()
    output = run_script(folder_path, file_types)
    print(output)

    # Prompt for copying to clipboard
    questions = [
        inquirer.Confirm('copy', message="Copy to clipboard?", default=True)
    ]
    answers = inquirer.prompt(questions)
    if answers['copy']:
        copy_to_clipboard(output)

if __name__ == "__main__":
    main()
