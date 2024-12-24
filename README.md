# Sentiment Analysis Web Application
## Demo

Here's how the application works:



![Demo GIF](![webapp](https://github.com/user-attachments/assets/998a60e0-83ea-4550-ad47-5c9e2db91bce)
)

## Overview
This project is a web-based sentiment analysis application that classifies text reviews as either positive or negative feedback. Built with Flask and machine learning, it provides real-time sentiment analysis of user input.

## Features
- Real-time sentiment analysis of text input
- Web interface for submitting reviews
- Display of sentiment statistics (positive/negative count)
- History of submitted reviews
- Preprocessing of text data
- Logging system for debugging and monitoring

## Tech Stack
- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn
- **Data Processing**: Pandas, NLTK
- **Logging**: Python's logging module

## Project Structure
sentiment-analysis-ml-project/
├── app.ipynb # Main Flask application
├── helper.py # Helper functions for text processing
├── logger.py # Logging configuration
├── modle/ # Directory containing ML models
│ ├── model.pkl # Trained model
│ └── vocabulary.txt # Vocabulary for vectorization
├── static/ # Static files
│ ├── main.css # CSS styles
│ └── gg.jpeg # Images
├── templates/ # HTML templates
│ └── index.html # Main page template
├── requirements.txt # Project dependencies
└── README.md # Project documentation

## Usage

1. Start the Flask application by running app.ipynb in Jupyter Notebook or JupyterLab
2. Open a web browser and navigate to `http://127.0.0.1:5000`
3. Enter text in the input field and submit to get sentiment analysis results
4. View the sentiment prediction (positive/negative) and statistics

## How It Works

1. **Text Preprocessing**:
   - Removes punctuation and special characters
   - Converts text to lowercase
   - Tokenizes the text
   - Applies stemming

2. **Sentiment Analysis**:
   - Vectorizes the preprocessed text using a pre-trained vocabulary
   - Uses a Logistic Regression model to classify the sentiment
   - Returns prediction as either "positive feedback" or "negative feedback"

3. **Logging**:
   - Tracks all operations for debugging
   - Records input text, preprocessing steps, and predictions

## File Descriptions

- `app.ipynb`: Main Flask application with routing and core functionality
- `helper.py`: Contains text preprocessing and model prediction functions
- `logger.py`: Configures logging for the application
- `model/vocabulary.txt`: Contains the vocabulary for text vectorization
- `model/model.pkl`: Trained Logistic Regression model

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Improvements
- Add support for multiple languages
- Implement more advanced ML models
- Add user authentication
- Improve UI/UX
- Add API endpoints for external integration

## License
This project is licensed under the MIT License.

## Contact
Your Name - vimukthixsandeepa
Project Link: https://github.com/vimukthixsandeepa/sentiment-analysis-ml-project
![Uploading webapp.PNG…]()

