import os
import re

def list_py_files(directory):
    """ List all Python files in the specified directory, ignoring venv, .gitignore, and requirements.txt """
    excluded_dirs = {'venv', '.venv'}
    excluded_files = {'.gitignore', 'requirements.txt'}
    py_files = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in excluded_dirs]
        for file in files:
            if file.endswith(".py") and file not in excluded_files:
                py_files.append(os.path.join(root, file))
    return py_files

def extract_imports(files):
    """ Extract import statements from a list of file paths """
    import_statements = set()
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            imports = re.findall(r'^(?:from\s+[\w\.]+\s+import\s+[\w\*, ]+|import\s+[\w\., ]+)', content, re.M)
            import_statements.update(imports)
    return import_statements

def filter_standard_libraries(import_statements):
    """ Filter out standard library imports and map known imports to their pip package names """
    # A set of standard library modules (this list is not exhaustive and might need updating)
    standard_libs = {'os', 'sys', 're', 'time', 'datetime', 'subprocess', 'threading', 'socket'}
    non_standard_libs = set()
    # Mapping of importable modules to their pip package names
    package_mapping = {
        'serial': 'pyserial',
        'numpy': 'numpy',  # Add similar mappings as needed
        'pandas': 'pandas',
        'tkinter': 'tk'  # This is actually part of the standard library but needs to be installed on some platforms
    }
    for import_statement in import_statements:
        for key in package_mapping:
            if key in import_statement:
                non_standard_libs.add(package_mapping[key])
    return non_standard_libs

def create_requirements_file(packages, filename='requirements.txt'):
    """ Write the packages to a requirements.txt file """
    with open(filename, 'w') as f:
        for package in packages:
            f.write(f"{package}\n")
    print(f"requirements.txt created with {len(packages)} packages.")

# Main execution flow
if __name__ == '__main__':
    directory_path = os.path.dirname(os.path.abspath(__file__))  # Use the script's directory
    py_files = list_py_files(directory_path)
    imports = extract_imports(py_files)
    non_standard_packages = filter_standard_libraries(imports)
    create_requirements_file(non_standard_packages)
