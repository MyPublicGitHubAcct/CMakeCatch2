import sys
from helpers import add_submodules, update_submodules

""" Run to update submodules as needed.  There are two options:

add = add submodules listed in the repos dictionary in add_submodules() below.
update = update all submodules.

So, it may look like $ python3 scripts/submodules.py update

The 'repos' dictionary can be updated if you want to change which external libraries should be in libs. 
"""

action_desired = sys.argv[1]

repos = {
    'Catch2': {'path': '/libs/Catch2', 'repo': 'git submodule add -b devel https://github.com/catchorg/Catch2.git'},
    'JUCE': {'path': '/libs/juce', 'repo': 'git submodule add -b develop https://github.com/juce-framework/JUCE.git'}
}


if action_desired == 'add':
    add_submodules(repos)
elif action_desired == 'update':
    update_submodules(repos)
else:
    print('Do you want to add, update, or both?  See submodules.py for more information.')
