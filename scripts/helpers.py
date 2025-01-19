import os
import shutil


def add_gitignore():
    src ='CMakeCatch2/.gitignore'
    dst = '.gitignore'
    shutil.copy2(src, dst)


def add_readme():
    text = str("# " + os.path.basename(os.getcwd()) + "\n")
    file = open("README.md","w")
    file.write(text)
    file.close()


def replace_words(path_to_file, replacements):
    """
    :param path_to_file: text like /foo/bar/filename
    :param replacements:dictionary like replacements: {'PROJECTNAME': str(project_name)}
    """
    if os.path.isfile(path_to_file):
        with open(path_to_file, 'r') as file:
            file_content = file.read()

        for old_word, new_word in replacements.items():
            file_content = file_content.replace(old_word, new_word)

        with open(path_to_file, 'w') as file:
            file.write(file_content)


def get_data(project_type):
    """
    :param project_type: The type of project being built.
    :return: A Python dictionary with information needed to build a new project.
    """
    parent_directory = ''
    templates_path = ''
    directory_names = ''
    submodules = ''
    project_cc_content = ''

    if project_type == 'd':
        project_type = 'Desktop'
        parent_directory = '/prj_desktop/'
        templates_path = '/templates/desktop'
        directory_names = ['cmake', 'docs', 'libs', 'python', 'resources', 'scripts', 'src', 'tests']
        submodules = [
            {'name': 'Catch2', 'path': '/libs/Catch2', 'repo': 'git submodule add -b devel https://github.com/catchorg/Catch2.git'},
        ]
        project_cc_content = ''

    elif project_type == 'e':
        project_type = 'Embedded'
        parent_directory = '/prj_embedded/'
        templates_path = '/templates/embedded'
        directory_names = ['bootloader', 'cmake', 'docs', 'drivers', 'dsp', 'hardware_design', 'libs', 'python',
                           'resources', 'scripts', 'tests']
        submodules = [
            {'name': 'Catch2', 'path': '/libs/Catch2', 'repo': 'git submodule add -b devel https://github.com/catchorg/Catch2.git'},
        ]
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
        parent_directory = '/prj_library/'
        templates_path = '/templates/library'
        directory_names = ['cmake', 'docs', 'libs', 'python', 'resources', 'scripts', 'src', 'tests']
        submodules = [
            {'name': 'Catch2', 'path': '/libs/Catch2', 'repo': 'git submodule add -b devel https://github.com/catchorg/Catch2.git'},
            {'name': 'JUCE', 'path': '/libs/juce', 'repo': 'git submodule add -b develop https://github.com/juce-framework/JUCE.git'}
        ]
        project_cc_content = ''

    elif project_type == 'p':
        project_type = 'Plugin'
        parent_directory = '/prj_plugin/'
        templates_path = '/templates/plugin'
        directory_names = ['cmake', 'docs', 'dsp', 'libs', 'python', 'resources', 'root', 'scripts', 'src', 'tests']
        submodules = [
            {'name': 'Catch2', 'path': '/libs/Catch2', 'repo': 'git submodule add -b devel https://github.com/catchorg/Catch2.git'},
            {'name': 'JUCE', 'path': '/libs/juce', 'repo': 'git submodule add -b develop https://github.com/juce-framework/JUCE.git'}
        ]
        project_cc_content = ''

    else:
        print("Error in get_data.")

    data = {
        'project_type': project_type,
        'parent_directory': parent_directory,
        'templates_path': templates_path,
        'directory_names': directory_names,
        'submodules': submodules,
        'project_cc_content': project_cc_content,
    }

    return data
