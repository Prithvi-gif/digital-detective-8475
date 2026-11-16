# Mission 6 — Git and GitHub

## Task 6.1 — Basic Git Workflow

This task demonstrates how to check repository status, stage changes, create commits, and inspect commit history.

### Git Operations

| Operation | Explanation |
|---|---|
| Check repository status | Shows modified, staged, and untracked files. |
| Stage changes | Selects changes to include in the next commit. |
| Create a commit | Saves the staged changes as a snapshot in Git history. |
| View commit history | Displays previous commits and their details. |

### Staging vs Committing

Staging prepares selected changes for a commit. Committing saves those staged changes as a permanent snapshot in the repository's local Git history.

## Task 6.3 — Branches and Pull Requests

### What is a Branch?

A branch is a separate line of development that allows developers to work on changes without directly modifying the main branch.

### What is a Pull Request?

A Pull Request (PR) is a request to review and merge changes from one branch into another branch on GitHub.

### Why are Branches and Pull Requests Useful?

- They allow developers to work independently.
- They keep the main branch protected from unfinished changes.
- Pull Requests make code review and collaboration easier.
- They help identify problems before changes are merged.

### Pull Request Evidence

- Branch: `update-about`
- Pull Request: #1
- Title: `docs: add my learning section`
- Status: Open — Not merged
- Merge conflicts: None

## Task 6.4 — Git Command Glossary

| Git command | Explanation |
|---|---|
| `git init` | Initializes a new Git repository. |
| `git status` | Shows the current state of the working directory and staging area. |
| `git add` | Stages selected changes for the next commit. |
| `git commit` | Saves staged changes in the local Git history. |
| `git log` | Displays the repository's commit history. |
| `git branch` | Lists existing branches. |
| `git switch -c branch-name` | Creates and switches to a new branch. |
| `git switch branch-name` | Switches to an existing branch. |
| `git push` | Publishes local commits to a remote repository. |
| `git pull` | Retrieves and integrates changes from a remote repository. |

## Conclusion

In this mission, I learned how Git tracks changes, how to stage and commit files, and how to create and publish branches. I also created Pull Request #1 on GitHub and reviewed its changes. The Pull Request remains open and has not been merged.