# 16. Push and Open a Pull Request

Emmanuel Corels Academy

Publish a practice branch and describe its requirement, implementation and test evidence in a pull request.

[Course repository](https://github.com/emmanuelcorelscreatives/eca-ai-assisted-python-github-copilot)

- [pull_request_review_template.txt](resources/01-pull_request_review_template.txt)

Use your own isolated starter repository and a GitHub repository you own, never
the Academy source remote. Create an empty personal repository on GitHub without
initializing extra files. With a clean local tree, add a credential-free HTTPS
remote (replace OWNER and REPO with your own names):

```sh
git remote add student https://github.com/OWNER/REPO.git
git push -u student main
git switch feature/branch-practice
git push -u student feature/branch-practice
```

If `student` already exists, verify its owner/repository locally instead of
replacing it blindly. Authenticate through your credential manager, never a
token embedded in a URL. On your repository's GitHub Pull requests page choose
New pull request, base `main`, compare `feature/branch-practice`. Review the exact
one-file patch from lesson 15 and fill in the linked template with actual test
evidence or `Not run`. Open a draft if needed; do not merge unrelated changes.
