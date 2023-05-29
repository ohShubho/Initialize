# Initialize

# GitHub Repository Automation Script

The script will create a new folder with the repository name in your specified projects directory. It will initialize a Git repository, add a README file, and make an initial commit.
Additionally, the script will create a new repository on GitHub using the provided repository name and push the initial commit to the remote repository.

## Usage

Follow these steps to use the script:

1. Ensure that you have Python installed on your system.

2. Clone or download this repository to your local machine.

3. Open a terminal or command prompt and navigate to the directory where you saved the script.

4. Install the required dependencies by running the following command:__
pip install PyGithub__
pip install git__
pip install python

5. Generate a personal access token (PAT) from GitHub. The token should have the necessary permissions to create repositories.

6. Open the `initialize.py` script in a text editor and replace the `GITHUB_TOKEN` variable with your generated PAT.

7. Save the changes and return to the terminal or command prompt.

8. Run the script with the desired repository name as the argument. For example:
python initialize.py my-repo

## Feel free to customize the script to suit your specific needs, such as adding more files or modifying the initial commit.
