import sys
import os
import shutil
from helpers import replace_words, get_data


"""
This script sets up a new project contained in a chosen directory.

Run like python3 scripts/add_project.py ProjectName ProjectType

    ProjectName - Any text with no spaces.
    ProjectType - d for Desktop, e for Embedded, l for library, or p for Plugin.
"""

project_name = sys.argv[1]
project_type = sys.argv[2]

data = get_data(project_type)
data.update({'project_name': project_name})
data.update({'replacements': {'PROJECTNAME': str(project_name), 'PROJECT_TYPE': str(project_type)}})

new_project_path = str(os.getcwd()) + data['parent_directory'] + data['project_name']
templates_path = str(os.getcwd() + data['templates_path'])

# top level items
shutil.copytree(str(templates_path) + '/root', str(new_project_path), dirs_exist_ok=True)

file_path = str(new_project_path + "/README.md")
replace_words(file_path, data['replacements'])

file_path = str(new_project_path + "/CmakeLists.txt")
replace_words(file_path, data['replacements'])

if data['project_type'] == 'Embedded':
    new_cc = str(new_project_path + "/" + data['project_name'] + ".cc")
    f = open(str(new_cc), "w")
    f.write(data['project_cc_content'])
    f.close()

    file_path = str(new_cc)
    replace_words(file_path, data['replacements'])

# in directories
for name in data['directory_names']:
    new_path = str(new_project_path) + "/" + name

    os.makedirs(str(new_path), exist_ok=False)
    shutil.copytree(str(templates_path) + "/" + name, str(new_path), dirs_exist_ok=True)

for name in data['directory_names']:
    new_path = str(new_project_path) + "/" + name

    file_path = str(new_path + "/README.md")
    replace_words(file_path, data['replacements'])

    file_path = str(new_path + "/CmakeLists.txt")
    replace_words(file_path, data['replacements'])
