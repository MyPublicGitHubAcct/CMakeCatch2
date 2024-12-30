import sys
import os
import shutil
from helpers import replace_words

"""
This script sets up a new project contained in a chosen directory.

Run like python3 scripts/add_project.py ProjectName ProjectType

    ProjectName - Any text with no spaces.
    ProjectType - e for Embedded, d for Desktop, or p for Plugin.
    Embedded:
        Directories: cmake, cmake, docs, drivers, dsp, hardware_design, libs, python, resources, scripts, src, tests
        Files:
            {project-name}.cc, CMakeLists.txt, and README.md at the top level.
    Desktop:
        Directories: cmake, docs, libs, python, resources, scripts, src, tests
        Files:
            CMakeLists.txt and README.md at the top level.
    Library:
        Directories: cmake, docs, libs, python, resources, scripts, src, tests
        Files:
            CMakeLists.txt and README.md at the top level.
    plugin:
        Directories: cmake, docs, libs, python, resources, scripts, src, tests
        Files:
            CMakeLists.txt and README.md at the top level.
"""

project_name = sys.argv[1]
project_type = sys.argv[2]
directory_names = ''
project_cc_content = ''

if project_type == 'd':
    project_type = 'Desktop'
    directory_names = ['cmake', 'docs', 'libs', 'python', 'resources', 'scripts', 'src', 'tests']
    project_cc_content = ''

elif project_type == 'e':
    project_type = 'Embedded'
    directory_names = ['bootloader', 'cmake', 'docs', 'drivers', 'dsp', 'hardware_design', 'libs', 'python',
                       'resources', 'scripts', 'tests']
    project_cc_content = '#include <cstdio>' + '\n' + \
                         'extern "C" {' + '\n' + \
                         '#include "drivers/driver.h"' + '\n' + \
                         '}' + '\n' + \
                         '\n' + \
                         'int main()' + '\n' + \
                         '{' + '\n' + \
                         '    int var = driver();' + '\n' + \
                         '    printf(\"Hello PROJECTNAME %d \\n\", var);' + '\n' + \
                         '    return 0;' + '\n' + \
                         '}' + '\n'

elif project_type == 'l':
    project_type ='Library'
    directory_names = ['cmake', 'docs', 'libs', 'python', 'resources', 'scripts', 'src', 'tests']
    project_cc_content = ''

elif project_type == 'p':
    project_type = 'Plugin'
    directory_names = ['cmake', 'docs', 'dsp', 'libs', 'python', 'resources', 'scripts', 'src', 'tests']
    project_cc_content = ''

else:
    print("I can't make that type of a project, Dave.")

data = {
    'project_name': project_name,
    'project_type': project_type,
    'directory_names': directory_names,
    'project_cc_content': project_cc_content,
    'replacements': {'PROJECTNAME': str(project_name), 'PROJECT_TYPE': str(project_type)}
}

new_project_path = ''
templates_path = ''

if data['project_type'] == 'Desktop':
    new_project_path = str(os.getcwd()) + '/prj_desktop/' + data['project_name']
    templates_path = str(os.getcwd() + '/templates/desktop')
elif data['project_type'] == 'Embedded':
    new_project_path = str(os.getcwd()) + '/prj_embedded/' + data['project_name']
    templates_path = str(os.getcwd() + '/templates/embedded')
elif data['project_type'] == 'Library':
    new_project_path = str(os.getcwd()) + '/prj_library/' + data['project_name']
    templates_path = str(os.getcwd() + '/templates/library')
elif data['project_type'] == 'Plugin':
    new_project_path = str(os.getcwd()) + '/prj_plugin/' + data['project_name']
    templates_path = str(os.getcwd() + '/templates/plugin')
else:
    print("Error in make_new_directories.")

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
