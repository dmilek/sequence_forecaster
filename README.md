# Daily Sequence Forecaster
This project predicts the next sequence of numbers using a Bayesian probability model, automates fetching data from a private GitHub repository, and generates daily reports in both CSV and HTML formats. The project is integrated with GitHub Actions for automated workflows, including model updates, predictions, and email notifications.

# Features
- **Prediction Model**: Bayesian probability-based model for predicting the most likely numbers in a sequence.
- **Data Fetching**: Securely fetches historical data from a private GitHub repository.
- **Model Persistence**: Updates and saves the model state (bayesian_model.pkl) after every prediction run.
- **Automated Reports**: Generates a CSV file of predictions and an HTML report with styled output.
- **GitHub Integration**: Commits predictions and model updates to the repository, with optional artifact storage.
- **Email Notifications**: Sends daily prediction reports via email using GitHub Actions.

# Technologies Used
- **Python**: Core programming language.
- **GitHub Actions**: CI/CD for automation.
- **Libraries**:
  - **pandas**: Data manipulation.
  - **requests**: Fetching data from the GitHub API.
  - **pickle**: Saving and loading model states.
  - **logging**: Custom logging for debugging and tracking.

# Setup Instructions
## 1. Clone the Repository
```
git clone https://github.com/<your-repo-owner>/<your-repo-name>.git
cd <your-repo-name>
```

## 2. Install Dependencies
Ensure you have Python 3.13 installed. Then, install required libraries:

```
pip install -r requirements.txt
```

## 3. Configure Environment Variables
Create a .env file in the root directory and add the following:

```
FINE_GRAINED_PAT=your_github_pat
REPO_OWNER=your_repo_owner
REPO_NAME=your_repo_name
DATA_FILE_PATH=path/to/data.csv
EMAIL_USERNAME=your_email@example.com
EMAIL_PASSWORD=your_email_password
EMAIL_RECIPIENT=recipient@example.com
```

## 4. Run the Project
To manually run the project, use:

```
python main.py
```

# GitHub Actions Workflow
The GitHub Actions workflow automates the following:

- Fetching data from the private GitHub repository.
- Training the Bayesian model and saving updates.
- Generating predictions and HTML reports.
- Committing updated files to the repository.
- Sending email notifications.

# Triggering the Workflow
The workflow is scheduled to run daily at 3:00 AM UTC or can be manually triggered.

# Key Workflow Steps
- **Checkout Code**: Fetches the repository files.
- **Install Dependencies**: Sets up the Python environment.
- **Run Script**: Executes the prediction script and generates the report.
- **Commit Updates**: Saves predictions and model updates to the repository.
- **Send Email**: Emails the HTML report to the recipient.

# Project Structure
```
├── data/
│   ├── bayesian_model.pkl       # Trained model file
│   ├── predicted_numbers.csv    # Latest predictions
├── utils/
│   ├── logger.py                # Logger setup
│   ├── github_handler.py        # GitHub API interaction
│   ├── html_report_generator.py # HTML report generation
│   ├── utility_functions.py     # Common utilities
├── models/
│   ├── bayesian_model.py        # Bayesian model implementation
├── main.py                      # Main script
├── requirements.txt             # Python dependencies
├── README.md                    # Project documentation
└── .github/
    ├── workflows/
        └── daily_forecaster.yml # GitHub Actions workflow
```

# Classes and Modules

## 1. BayesianModel
- **Purpose**: Implements the Bayesian probability-based prediction model.
- **Key Methods**:
  - **train(data)**: Trains the model with historical data.
  - **predict_next(top_n=11)**: Predicts the top probable numbers.
  - **save_model(filepath)**: Saves the model state to a file.
  - **load_model(filepath)**: Loads the model state from a file.

## 2. PrivateGitHubCSV
- **Purpose**: Fetches CSV data from a private GitHub repository.
- **Key Methods**:
- **fetch_file(file_path)**: Fetches raw file content.
- **read_csv(file_path)**: Parses the file into a DataFrame.
- 
## 3. HTMLGenerator
- **Purpose**: Creates an HTML report for predictions.
- **Key Methods**:
  - **generate_html(predictions)**: Converts predictions into a styled HTML report.

## 4. Logger
- **Purpose**: Provides a singleton logger for consistent logging.
- **Key Methods**:
  - **get_logger(log_file, level)**: Configures and retrieves the logger.

# Future Enhancements
- Add a user interface for non-technical users.
- Implement advanced models using machine learning.
- Optimize model storage to reduce repository size.

# License
![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey)
