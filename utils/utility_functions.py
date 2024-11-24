import pandas as pd

def load_data(filepath):
    """
    Load the historical lottery data from a CSV file.
    Args:
        filepath (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded data.
    """
    return pd.read_csv(filepath)

def save_predictions(predictions, filepath):
    """
    Save the predicted numbers to a CSV file.
    Args:
        predictions (list): List of predicted numbers.
        filepath (str): Path to the output CSV file.
    """
    pd.DataFrame({'Predicted Numbers': predictions}).to_csv(filepath, index=False)
