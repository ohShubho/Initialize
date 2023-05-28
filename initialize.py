import os
import subprocess
from github import Github
import sys

# GitHub API credentials
token = "YOUR_PERSONAL_ACCESS_TOKEN"

# Path to your projects directory
project_directory = "YOUR_PROJECTS_DIRECTORY"

# Get repository name from command-line argument
if len(sys.argv) != 2:
    print("Usage: python initialize.py [repository_name]")
    sys.exit(1)

repo_name = sys.argv[1]

# Create a new directory for the project if it doesn't exist
project_path = os.path.join(project_directory, repo_name)
if not os.path.exists(project_path):
    os.makedirs(project_path)

# Change to the project directory
os.chdir(project_path)

# Initialize Git repository locally if it's not already initialized
if not os.path.exists(".git"):
    subprocess.run(["git", "init"])

    # Set the remote origin URL
    remote_url = f"https://github.com/YOUR_USERNAME/{repo_name}.git"
    subprocess.run(["git", "remote", "add", "origin", remote_url])

# Create a README file if it doesn't exist
readme_path = os.path.join(project_path, "README.md")
if not os.path.exists(readme_path):
    readme_content = "# " + repo_name
    with open(readme_path, "w") as readme_file:
        readme_file.write(readme_content)

# Stage and commit the README file if there are changes
subprocess.run(["git", "add", "README.md"])
subprocess.run(["git", "commit", "-m", "Initial commit"])

# Create a new GitHub repository if it doesn't exist
g = Github(token)
user = g.get_user()
try:
    repo = user.get_repo(repo_name)
except:
    repo = user.create_repo(repo_name)

# Push to the repository
subprocess.run(["git", "push", "-u", "origin", "master"])
