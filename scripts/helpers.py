import os


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


def add_submodules(repos):
    """
    :param repos: a dictionary like repos = { 'name': {'path': '/libs/foo', 'repo': 'git submodule add ...'},
    """
    path = 'libs'
    if not os.path.isdir(path):
        os.mkdir(path)

    for name, repo_info in repos.items():
        if not os.path.isdir(str(repo_info['path'])):
            cmd = "cd libs;" + str(repo_info['repo'])
            os.system(cmd)


def update_submodules(repos):
    """
    :param repos: a dictionary like repos = { 'name': {'path': '/libs/foo', 'repo': 'git submodule add ...'},
    """
    for name, repo_info in repos.items():
        if os.path.isdir(str(repo_info['path'])):
            cmd = "cd libs;" + \
                  "git submodule init;" + \
                  "git submodule update --remote;"
            os.system(cmd)
