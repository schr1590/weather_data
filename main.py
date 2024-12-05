from datetime import time
import git
import os

def push_to_github(repo_path, commit_message="Update file", remote_name="origin", branch="main"):
    # Ensure the given path is a valid Git repository
    if not os.path.isdir(repo_path):
        print(f"{repo_path} is not a valid directory.")
        return

    try:
        # Initialize the repository using GitPython
        repo = git.Repo(repo_path)

        # Check if the repository is dirty (i.e., has changes to commit)
        if repo.is_dirty(untracked_files=True):
            print("Changes detected. Committing and pushing to GitHub...")

            # Stage all changes
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
    push_to_github(repo_path, commit_message)
    time.sleep(10)
