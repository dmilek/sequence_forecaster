import pandas as pd

class HTMLGenerator:
    """Class to generate HTML report from predictions with styling."""

    @staticmethod
    def generate_html(predictions):
        """
        Generates a nicely styled HTML report based on predictions.

        Args:
            predictions (list or pd.DataFrame): The data to include in the report.
        """
        # Convert predictions to a DataFrame if it's not already
        if isinstance(predictions, list):
            predictions = pd.DataFrame(predictions, columns=["Predicted Numbers"])

        # Start building the HTML report with some nice styling
        html_content = f"""
        <html>
        <head>
            <title>Prediction Report</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    margin: 0;
                    padding: 20px;
                }}
                h1 {{
                    color: #333;
                    text-align: center;
                }}
                h2 {{
                    color: #555;
                    font-size: 1.5em;
                    margin-bottom: 10px;
                }}
                table {{
                    width: 100%;
                    margin-top: 20px;
                    border-collapse: collapse;
                    border: 1px solid #ddd;
                }}
                th, td {{
                    padding: 10px;
                    text-align: center;
                    border: 1px solid #ddd;
                }}
                th {{
                    background-color: #4CAF50;
                    color: white;
                }}
                tr:nth-child(even) {{
                    background-color: #f2f2f2;
                }}
                tr:hover {{
                    background-color: #ddd;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 40px;
                    color: #777;
                }}
            </style>
        </head>
        <body>
            <h1>Prediction Report</h1>
            <h2>Next Predicted Numbers</h2>
            {predictions.to_html(index=False, header=True)}
            <div class="footer">
                <p>Generated on {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
        </body>
        </html>
        """

        return html_content  # Return html content
