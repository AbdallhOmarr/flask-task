import os

def list_files(startpath, exclude_folders, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(startpath):
            # Exclude specified folders
            dirs[:] = [d for d in dirs if d not in exclude_folders and not d.startswith('.')]
            
            level = root.replace(startpath, '').count(os.sep)
            indent = '-' * 4 * (level)
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))
            subindent = '-' * 4 * (level + 1)
            for file in files:
                f.write('{}{}\n'.format(subindent, file))

# Replace 'path/to/your/folder' with the path of the folder you want to explore
folder_path = '.'
exclude_folders = ['.git','myenv']  # Add more folders to exclude if needed
output_file = 'project_scheme.txt'

list_files(folder_path, exclude_folders, output_file)
