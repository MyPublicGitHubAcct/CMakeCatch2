# Template for projects relying on CMake and Catch2

## Features and Intended Use

This template is intended to be a submodule of projects used to organize new Desktop, Embedded, Library, or Plugin (JUCE-based) projects.

Add this to your project like

```zsh
mkdir MyFancyNewProject && cd "$_"
git submodule add -b main https://github.com/MyPublicGitHubAcct/CMakeCatch2.git
python3 CMakeCatch2/scripts/setup_new_repository.py
```

## To start a new project

```zsh
python3 scripts/add_project.py ProjectName ProjectType
```

Run the command above and replace ProjectName with your project's name and ProjectType with one of choices below.

- __d__ = Desktop  
- __e__ = Embedded  
- __l__ = Library  
- __p__ = Plugin  

Once the project is generated, compile it with

```zsh
cd {NewProjectName}
cmake -H. -B build 
cmake --build build
```

Projects that are not of type Plugin can be tested with

```zsh
./build/{NewProjectName}
```

### Submodules

Use to update the Git submodules...

```zsh
git submodule init
git submodule update --remote
```

## Tools

Tools used to build and maintain this project and could be used on any child projects.

_Text Editor_: [Sublime Text](https://www.sublimetext.com)  
_Compiler_: [GCC](https://gcc.gnu.org)  
_Compiler for Embedded_: [ARM GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain)  
_IDE_ (not needed but a good to use for the actual projects created in this structure one is) : [Clion](https://www.jetbrains.com/clion/)   


## References

- [Example of Testing](https://github.com/cpp-for-yourself/lectures-and-homeworks/blob/main/lectures/googletest.md)
- [CMake/GoogleTest video](https://youtu.be/pxJoVRfpRPE?si=uQlkHhVwrA8shj2B)
- [Cpp for Yourself Github files](https://github.com/cpp-for-yourself/lectures-and-homeworks/)
- [Another testing article](https://interrupt.memfault.com/blog/unit-testing-basics)
- [Testing for Embedded](https://dev.blues.io/blog/embedded-c-unit-testing/)
- [Docker / STM32](https://www.beningo.com/using-docker-to-setup-an-stm32-build-environment/)
