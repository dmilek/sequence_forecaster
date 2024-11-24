import pandas as pd
import pickle
from collections import Counter

from utils.logger import Logger

logger = Logger.get_logger()
class BayesianModel:
    def __init__(self):
        self.number_probabilities = {}

    def train(self, data):
        """
        Train the model using historical lottery data.
        Args:
            data (pd.DataFrame): DataFrame containing historical numbers.
        """
        numbers = data.iloc[:, 1:].values.flatten()
        counts = Counter(numbers)

        # Calculate probabilities for each number
        for number, count in counts.items():
            # Update probabilities incrementally
            if number in self.number_probabilities:
                self.number_probabilities[number] += count
            else:
                self.number_probabilities[number] = count

        # Normalize probabilities
        total_counts = sum(self.number_probabilities.values())
        for number in self.number_probabilities:
            self.number_probabilities[number] /= total_counts

    def predict_next(self, top_n=11):
        """
        Predict the most probable numbers for the next draw.
        Args:
            top_n (int): Number of top probable numbers to return.
        Returns:
            list: List of the most probable numbers.
        """
        sorted_numbers = sorted(self.number_probabilities.items(), key=lambda x: x[1], reverse=True)
        return [num for num, prob in sorted_numbers[:top_n]]

    def save_model(self, filepath):
        """Save the model (probabilities) to a file."""
        with open(filepath, 'wb') as file:
            pickle.dump(self.number_probabilities, file)

    def load_model(self, filepath):
        """Load the model (probabilities) from a file."""
        try:
            with open(filepath, 'rb') as file:
                self.number_probabilities = pickle.load(file)
        except FileNotFoundError:
            logger.info(f"No saved model found at {filepath}. Starting fresh.")
