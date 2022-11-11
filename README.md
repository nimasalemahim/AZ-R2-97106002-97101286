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

## Q3
### Fetch
Git Fetch is the command that tells the local repository that there are changes available in the remote repository without bringing the changes into the local repository.
### Pull
Git Pull on the other hand brings the copy of the remote directory changes into the local repository.
### Merge
Git merge command is the positive conclusion of your decision to incorporate the changes you saw using the Git fetch command.
![Alternate image text](https://res.cloudinary.com/practicaldev/image/fetch/s--MEKaM3dY--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://cl.ly/430Q2w473e2R/Image%25202018-04-30%2520at%25201.07.58%2520PM.png)
![alt text](https://i0.wp.com/kheri.net/wp-content/uploads/2020/11/image.png?resize=650%2C279&ssl=1)

## Q4
### Clone
git clone is primarily used to point to an existing repo and make a clone or copy of that repo at in a new directory, at another location.
![alter](https://bobbelderbos.com/assets/git-clone.png)
### Rebase
Rebasing is the process of moving or combining a sequence of commits to a new base commit. 
![alter](https://miro.medium.com/max/1400/1*K4anH9QzRcPqLCv-7HyiCQ.png)

## Q5
git reset and git revert are both useful commands for undoing changes that have been made in previous commits. While git reset does this by moving the current head of the branch back to the specified commit, thereby changing the commit history, git revert does this by creating a new commit that undoes the changes in the specified commit and so does not change the history. This means that when you want to undo the changes in multiple commits, git reset may be more useful but should mostly be used only when changes have not been made public, while git revert can be used when only a specific commit needs to be undone and can be used even when the changes have been made public. 
### Reset
At the commit level (where we change whole commits), resetting is a way to move the the current tip of a branch to a previous commit. This can be done to remove commits from the current branch that we no longer want, or to undo any changes that have been made. An example of this is moving the branch new-feature back two commits from the current HEAD using the following command:
``` git checkout new-feature reset HEAD~2 ```
![alter](https://res.cloudinary.com/practicaldev/image/fetch/s--x1oDKltr--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://cl.ly/063v3m0l2X3b/Image%25202018-05-21%2520at%252010.56.45%2520AM.png)
### Revert
While git reset should mostly be used on non-public branches of repositories there are times when you want to undo a change that has been made to a public repository. This could be because the changes made introduced an unexpected bug or the change itself wasn’t needed. In this scenario, git revert should be used instead of git reset .
This is because reverting undoes a commit by creating a new one. This makes it a safe way for undoing changes in a public commit history as it does not overwrite any of that history, rather it just undoes all of those changes in a new commit. An example of this is when you want to undo the changes made in commit B , you can use git revert B to create a new commit that undoes all of those changes. In doing so, git figures out the changes that were made in B , undoes all of those changes if possible, and then will add a new commit onto the existing project as follows:
```git revert B ```
![alter](https://s3.ap-south-1.amazonaws.com/s3.studytonight.com/tutorials/uploads/pictures/1625062814-103268.png)

## Q6
### Stage
Staged means that you have marked a modified file in its current version to go into your next commit snapshot.
### Snapshot
A snapshot is a representation of the current state of your tracked files in the form of a manifest, which can be compared with other manifests to see where the differences are. Git only tracks the differences between manifests from the first moment it was tracked.
