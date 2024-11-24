from dotenv import load_dotenv

from models.bayesian_model import BayesianModel
from utils.utility_functions import save_predictions
from utils.github_handler import PrivateGitHubCSV
from utils.logger import Logger
import os

# Initialize logger
logger = Logger.get_logger()
load_dotenv()
# GitHub and file paths configuration
GITHUB_TOKEN = os.getenv("FINE_GRAINED_PAT")  # Token stored in environment variables
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAME = os.getenv("REPO_NAME")
DATA_FILE_PATH = os.getenv("DATA_FILE_PATH")  # Path to CSV file in the repository

# Local paths for saving model and predictions
MODEL_FILEPATH = 'data/bayesian_model.pkl'
OUTPUT_FILEPATH = 'data/predicted_numbers.csv'

def main():
    """
    Main function to manage the Bayesian model workflow:
    - Fetch data from a private GitHub repository.
    - Train the Bayesian model with the fetched data.
    - Save the trained model state.
    - Predict the next sequence of numbers.
    - Save the predictions locally.
    """
    try:
        # Step 1: Fetch the CSV file from GitHub
        logger.info("Fetching data from GitHub...")
        github_handler = PrivateGitHubCSV(GITHUB_TOKEN, REPO_OWNER, REPO_NAME)
        data = github_handler.read_csv(DATA_FILE_PATH)
        logger.info("Data successfully fetched from GitHub.")

        # Step 2: Initialize the Bayesian model
        logger.info("Initializing Bayesian model...")
        model = BayesianModel()

        # Step 3: Load previous model state if available
        logger.info("Loading previous model state...")
        model.load_model(MODEL_FILEPATH)

        # Step 4: Train the model with new data
        logger.info("Training the model with new data...")
        model.train(data)

        # Step 5: Save the updated model state
        logger.info("Saving the updated model state...")
        model.save_model(MODEL_FILEPATH)

        # Step 6: Predict the next sequence of numbers
        logger.info("Predicting the next sequence of numbers...")
        predictions = model.predict_next()

        # Step 7: Save predictions to a local file
        logger.info("Saving predictions to file...")
        save_predictions(predictions, OUTPUT_FILEPATH)
        logger.info(f"Predicted numbers saved to {OUTPUT_FILEPATH}")

    except Exception as e:
        # Log any errors during the process
        logger.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
