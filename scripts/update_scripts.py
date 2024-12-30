from urllib.request import urlretrieve

"""
This script will download the current version of each script and replace the local file.

Run like $ python3 scripts/update_scripts.py
"""

scripts = ['add_project.py', 'helpers.py', 'submodules.py']

for file in scripts:
	url = str('https://raw.githubusercontent.com/MyPublicGitHubAcct/CMakeCatch2/refs/heads/main/scripts/' + file)
	filename = str('scripts/' + file)
	urlretrieve(url, filename)
