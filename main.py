import time
import git
import os
import subprocess


def push_to_github(repo_path, commit_message="Update file", remote_name="origin", branch="main"):
    # Ensure the given path is a valid Git repository
    if not os.path.isdir(repo_path):
        print(f"{repo_path} is not a valid directory.")
        return

    try:
        # Initialize the repository using GitPython
        repo = git.Repo(repo_path)

        # Check the status using git status command
        status_output = subprocess.check_output(['git', 'status', '--porcelain'], cwd=repo_path).decode()

        if status_output:
            print("Changes detected. Committing and pushing to GitHub...")

            # Stage all changes (to be more comprehensive)
            repo.git.add(A=True)

            # Commit changes
            repo.index.commit(commit_message)

            # Push changes to the remote repository (GitHub)
            origin = repo.remote(name=remote_name)
            origin.push(branch)
            print(f"Changes pushed to {remote_name}/{branch}.")
        else:
            print("No changes detected.")

    except git.exc.InvalidGitRepositoryError:
        print(f"{repo_path} is not a valid Git repository.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage

while True:
    repo_path = r"C:\Users\ejsch\source\repos\MLDM_LABS\MLDM-Final\weather_data"  # Local path to your Git repository
    commit_message = "Updated the weather data"

    # Ensure that the files are updated
    touch_files = ["main.py", "weather_data.csv"]  # List of files to ensure are updated
    for file in touch_files:
        if os.path.exists(file):
            os.utime(file, None)  # Update the file timestamp to force Git to recognize the file change

    # Push changes to GitHub
    push_to_github(repo_path, commit_message)

    time.sleep(10)
