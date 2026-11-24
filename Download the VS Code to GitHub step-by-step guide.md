# Upload the Student Grade Manager to GitHub Using VS Code

## Purpose

This guide explains how to upload the **Student Grade Manager** project from Visual Studio Code to GitHub.

The project folder used in this guide is:

```text
F:\.SocialEagal\Day2
```

The files currently visible in Visual Studio Code are:

```text
grade_manager.py
Week1_Day2_Student_Grade_Manager.pdf
```

The current Git branch is:

```text
main
```

---

## 1. Confirm that Visual Studio Code opened the correct folder

The correct project folder must be open before uploading the code.

In Visual Studio Code:

1. Select **File**.
2. Select **Open Folder**.
3. Browse to:

   ```text
   F:\.SocialEagal\Day2
   ```

4. Choose **Select Folder**.

The Visual Studio Code Explorer should display `grade_manager.py`.

The terminal prompt should show:

```powershell
PS F:\.SocialEagal\Day2>
```

This confirms that terminal commands will run inside the correct project folder.

---

## 2. Confirm that Git is installed

Open the Visual Studio Code terminal:

1. Select **Terminal** from the top menu.
2. Select **New Terminal**.
3. Enter:

   ```powershell
   git --version
   ```

A successful result looks similar to:

```text
git version 2.53.0.windows.1
```

If a Git version appears, Git is installed correctly.

---

## 3. Initialize the Day2 folder as a Git repository

This step creates a separate Git repository inside the `Day2` folder.

Run:

```powershell
git init -b main
```

A successful result looks similar to:

```text
Initialized empty Git repository in F:/.SocialEagal/Day2/.git/
```

The `-b main` option creates the repository with `main` as its first branch.

### Verify the repository

Run:

```powershell
git status
```

Expected output:

```text
On branch main

No commits yet

Untracked files:
  grade_manager.py
  Week1_Day2_Student_Grade_Manager.pdf
```

**Untracked** means that the files exist but have not yet been added to Git.

---

## 4. Review the files before uploading

In the Visual Studio Code **Source Control** panel, the files appear under **Changes**.

A letter `U` beside a file means:

```text
U = Untracked
```

Review every file before staging it.

Recommended files:

- `grade_manager.py`: required project source code.
- `README.md`: recommended project documentation, if available.
- `Week1_Day2_Student_Grade_Manager.pdf`: optional assignment document. Upload this only if sharing the assignment PDF is permitted.

Do not upload:

- Passwords
- Personal access tokens
- API keys
- Confidential company documents
- Files containing private information

If only the Python program is required, stage only `grade_manager.py`.

---

## 5. Stage the project files in Visual Studio Code

Staging selects the files that will be included in the next Git commit.

### Stage all displayed files

1. Open **Source Control** by clicking the branch-shaped icon on the left.
2. Find the **Changes** heading.
3. Move the pointer over **Changes**.
4. Click the **+** button labelled **Stage All Changes**.

The files will move from **Changes** to **Staged Changes**.

### Stage only the Python file

If the PDF should not be uploaded:

1. Move the pointer over `grade_manager.py`.
2. Click the **+** button beside `grade_manager.py`.
3. Leave the PDF under **Changes**.

### Terminal alternative

To stage only the Python program:

```powershell
git add grade_manager.py
```

To stage every file in the folder:

```powershell
git add .
```

### Verify staged files

Run:

```powershell
git status
```

Staged files will appear under:

```text
Changes to be committed:
```

---

## 6. Create the first commit

A commit is a saved version or snapshot of the project.

In the Source Control panel:

1. Click the message box at the top.
2. Enter:

   ```text
   Initial Student Grade Manager project
   ```

3. Click **Commit**.

The keyboard shortcut shown by Visual Studio Code may also allow the commit after entering the message.

### If Git asks for an author name and email

Open the terminal and run:

```powershell
git config --global user.name "Prabaharan Ganesan"
```

Then configure the email address associated with the GitHub account:

```powershell
git config --global user.email "YOUR-GITHUB-EMAIL"
```

Replace `YOUR-GITHUB-EMAIL` with the actual GitHub email address.

Example:

```powershell
git config --global user.email "example@email.com"
```

Then return to Source Control and click **Commit** again.

### Verify the commit

Run:

```powershell
git status
```

If all staged files were committed, Git should report:

```text
nothing to commit, working tree clean
```

To view the commit:

```powershell
git log --oneline
```

The output should contain a line similar to:

```text
abc1234 Initial Student Grade Manager project
```

The characters at the beginning are the unique commit identifier.

---

## 7. Publish the repository to GitHub

After the first commit, Visual Studio Code should display one of these buttons:

- **Publish Branch**
- **Publish to GitHub**

Click the available publishing button.

### Sign in to GitHub

If Visual Studio Code asks for authentication:

1. Select **Sign in with GitHub**.
2. Allow Visual Studio Code to open the browser.
3. Sign in to the correct GitHub account.
4. Approve or authorize Visual Studio Code.
5. Return to Visual Studio Code.

### Choose repository visibility

Visual Studio Code may ask whether the repository should be public or private.

Choose:

```text
Publish to GitHub public repository
```

A public repository is normally appropriate when an assignment must be shared through a GitHub link. Use a private repository if the instructor requires private submission.

### Choose the repository name

Use:

```text
student-grade-manager
```

The final GitHub address will look similar to:

```text
https://github.com/YOUR-USERNAME/student-grade-manager
```

Wait until Visual Studio Code confirms that publishing has completed.

---

## 8. Verify the upload on GitHub

After publishing, Visual Studio Code may display **Open on GitHub**.

1. Click **Open on GitHub**.
2. Confirm that the repository page opens in the browser.
3. Confirm that `grade_manager.py` appears in the repository.
4. Click `grade_manager.py`.
5. Confirm that the complete Python program is visible.

Copy the repository URL from the browser address bar.

Example format:

```text
https://github.com/YOUR-USERNAME/student-grade-manager
```

This is the link to submit or share.

Do not submit the editing URL or an individual commit URL unless specifically requested. Submit the main repository URL.

---

## 9. Test the uploaded Python project

Before submitting the GitHub link, test the local program again from the Visual Studio Code terminal:

```powershell
python .\grade_manager.py
```

The program should display:

```text
Student Grade Manager
1. Add student
2. Show results
3. Quit
Choose an option (1-3):
```

Test at least:

- A valid mark such as `80`
- A negative mark such as `-25`
- A mark above 100 such as `150`
- Non-numeric input such as `abc`
- An empty input
- The **Show results** option
- The **Quit** option

The negative and above-100 marks should be rejected without crashing.

---

## 10. Upload future changes

After the first publication, do not create another repository for each update.

When `grade_manager.py` is modified:

1. Save the file with **Ctrl+S**.
2. Open **Source Control** with **Ctrl+Shift+G**.
3. Review the modified file.
4. Click the **+** button to stage it.
5. Enter a meaningful commit message, for example:

   ```text
   Improve mark validation
   ```

6. Click **Commit**.
7. Click **Sync Changes** or **Push**.

### Terminal alternative

```powershell
git add grade_manager.py
git commit -m "Improve mark validation"
git push
```

GitHub will then show the latest version.

---

## 11. Common problems and solutions

### Problem: Only `Changes` and `U` are visible

This means files have not been staged.

Solution:

- Click the **+** beside each required file, or
- Run:

  ```powershell
  git add grade_manager.py
  ```

### Problem: `nothing added to commit but untracked files present`

This means the files were not staged before committing.

Solution:

```powershell
git add .
git commit -m "Initial Student Grade Manager project"
```

### Problem: Git cannot detect the author identity

Solution:

```powershell
git config --global user.name "Prabaharan Ganesan"
git config --global user.email "YOUR-GITHUB-EMAIL"
```

Then commit again.

### Problem: No **Publish Branch** button appears

First confirm that a commit exists:

```powershell
git log --oneline
```

If no commit appears, stage and commit the files first.

If a commit exists, open the Command Palette using **Ctrl+Shift+P**, search for:

```text
Git: Publish Branch
```

and select it.

### Problem: Visual Studio Code opens the wrong parent repository

Confirm that the terminal path is:

```powershell
PS F:\.SocialEagal\Day2>
```

Then confirm that `Day2` contains its own `.git` folder:

```powershell
Get-ChildItem -Force
```

The output should include:

```text
.git
```

### Problem: GitHub repository already exists and is not empty

If a GitHub repository was manually created with a README before publishing, local and remote histories may differ.

For a beginner project, the simplest approach is usually:

1. Delete the empty or unnecessary GitHub repository.
2. Publish again from Visual Studio Code.

Alternatively, an existing remote can be connected manually, but that workflow requires careful pull and merge handling.

---

## 12. Current-state checklist

Based on the current Visual Studio Code screen, the following steps are already complete:

- [x] The `Day2` folder is open.
- [x] Git is installed.
- [x] The Git repository has been initialized.
- [x] The current branch is `main`.
- [x] Visual Studio Code detects two untracked files.

Complete the remaining steps:

- [ ] Decide whether to upload the PDF.
- [ ] Stage `grade_manager.py` and any permitted documentation.
- [ ] Enter `Initial Student Grade Manager project` as the commit message.
- [ ] Click **Commit**.
- [ ] Configure the Git name and email if requested.
- [ ] Click **Publish Branch** or **Publish to GitHub**.
- [ ] Sign in to GitHub.
- [ ] Choose public or private visibility.
- [ ] Use `student-grade-manager` as the repository name.
- [ ] Open the repository on GitHub.
- [ ] Confirm that `grade_manager.py` is visible.
- [ ] Copy and submit the repository URL.

---

## Quick workflow summary

```text
Open Day2 in Visual Studio Code
        ↓
Confirm Git installation
        ↓
Initialize repository on main
        ↓
Review project files
        ↓
Stage required files
        ↓
Enter commit message
        ↓
Commit
        ↓
Publish Branch
        ↓
Sign in to GitHub
        ↓
Choose repository visibility
        ↓
Name it student-grade-manager
        ↓
Open on GitHub
        ↓
Verify grade_manager.py
        ↓
Copy the repository link
```

## Recommended immediate next action

In the current Source Control panel, click the **+** beside `grade_manager.py`. Stage the PDF only if sharing the assignment document is allowed. Then enter:

```text
Initial Student Grade Manager project
```

and click **Commit**.
