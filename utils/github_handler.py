import requests
import pandas as pd
import base64
from io import StringIO  # Import StringIO from io module

from models.bayesian_model import logger

class PrivateGitHubCSV:
    """Handles fetching and reading private CSV files from GitHub using Fine-Grained PAT."""

    def __init__(self, token, repo_owner, repo_name):
        """
        Initialize with GitHub token, repo owner, and repo name.
        Args:
            token (str): Fine-Grained PAT.
            repo_owner (str): Owner of the repository.
            repo_name (str): Repository name.
        """
        self.token = token
        self.repo_owner = repo_owner
        self.repo_name = repo_name

    def fetch_file(self, file_path):
        """
        Fetch the content of a file from a private GitHub repository.
        Args:
            file_path (str): Path to the file in the repository.
        Returns:
            str: Decoded file content.
        """
        url = f"https://api.github.com/repos/{self.repo_owner}/{self.repo_name}/contents/{file_path}"
        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            content = response.json()["content"]
            return base64.b64decode(content).decode()
        else:
            raise requests.exceptions.RequestException(f"Failed to fetch file: {response.status_code}, {response.text}")

    def read_csv(self, file_path):
        """
        Read a CSV file from a private GitHub repository into a DataFrame.
        Args:
            file_path (str): Path to the CSV file in the repository.
        Returns:
            pd.DataFrame: The loaded DataFrame.
        """
        content = self.fetch_file(file_path)
        data = pd.read_csv(StringIO(content))  # Use StringIO here to parse the CSV string
        return data


# Usage example
if __name__ == "__main__":
    # Replace with your actual Fine-Grained PAT and repository details
    GITHUB_TOKEN = "your_fine_grained_pat"
    REPO_OWNER = "owner"
    REPO_NAME = "repo_name"
    FILE_PATH = "file_path"

    try:
        # Initialize handler
        github_handler = PrivateGitHubCSV(GITHUB_TOKEN, REPO_OWNER, REPO_NAME)

        # Fetch and load CSV
        df = github_handler.read_csv(FILE_PATH)
        logger.info("CSV file loaded successfully:")
        logger.info(df.head())
    except Exception as e:
        logger.info(f"Error: {e}")
