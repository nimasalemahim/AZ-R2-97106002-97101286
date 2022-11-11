# Calculator
Basic Calculator

## Project Report
First, We initialized the project with the .git file, main file, etc. After that, we created three branches, in order to implement different tasks and features. They were the master branch, develop branch, and develop-readme branch. We protected the main branch (Master) from being merged with other branches without any pull requests.
Furthermore, The class Calculator was initiated, and we implemented different methods like add, sub, multiply, and divide for the calculator, in multiple commits and merge requests. We faced some merge conflicts during these implementations. We tried to resolve them by reviewing the conflicts, and adding what we needed from each version. 

# Questions

## Q1
### What is the .git file? What is saved in it?
The .git folder contains all information that is necessary for the project and all information relating commits, remote repository address, etc. It also contains a log that stores the commit history. This log can help you to roll back to the desired version of the code.
For example, these are some major sub-directories, which their information is saved in .git file:
Hooks: This folder contains script files. Git hooks are the scripts that are executed before or after events like commit, push etc.
Objects: This folder represents an object database of Git.
HEAD: This file stores reference to the current branch. It points to the master branch by default.
...

## Q2
### What is atomic commit ?
Another way to define an atomic commit is one that can be reverted without any unwanted side effects or regressions, aside from what you'd expect based on its message. If a commit is removed from your git commit history but doing so removes other legitimate changes, then that commit wasn't atomic.
### What is pull request ?
A pull request is an event in Git where a contributor asks a maintainer of a Git repository to review code they want to merge into a project.

