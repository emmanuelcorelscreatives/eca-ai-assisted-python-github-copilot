# 14. Read Status and Diffs Before Committing

Emmanuel Corels Academy

Inspect staged and unstaged changes and identify an unrelated edit or generated file.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

Use your isolated starter Git repository from lesson 13 with a clean tree.
Append `# Status practice` to its `.gitignore`, save, then inspect:

```sh
git status --short
git diff -- .gitignore
git add -- .gitignore
git diff --cached -- .gitignore
git diff -- .gitignore
```

Expect only the added comment in the staged diff and no remaining unstaged
diff. Append a second comment, `# Unstaged practice`, and compare both diffs:
the first comment is staged and the second is not. Unstage with
`git restore --staged -- .gitignore`; inspect the combined working-file diff
before discarding only this disposable edit with `git restore -- .gitignore`.
Do not restore unexplained pre-existing work.
