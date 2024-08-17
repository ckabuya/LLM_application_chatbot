# Integrating your Chatbot into a Web Interface

## Introduction
This project demonstrates how to set up a back-end server and integrate a chatbot into a web application. It provides a practical approach to creating a ChatGPT-like website by combining a Flask-based back-end with a front-end webpage. The chatbot uses the Hugging Face Transformers library with the BlenderBot model.

## Learning Objectives
After completing this project, you will be able to:
- Set up a back-end server using Flask
- Integrate a pre-trained chatbot model into a Flask server
- Implement communication between a web page and the back-end server
- Handle conversation history in a chatbot application

## Prerequisites
- Python 3.7+
- Basic knowledge of Python programming
- Familiarity with Flask web framework
- Understanding of HTML, CSS, and JavaScript basics

## Project Structure
The project consists of two main components:
1. A Flask back-end server hosting the chatbot
2. A front-end webpage for user interaction

## Setup Instructions
1. Clone this repository:
   ```
   git clone https://github.com/ckabuya/LLM_application_chatbot.git
   cd LLM_application_chatbot
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install flask flask-cors transformers torch
   ```

4. Run the Flask server:
   ```
   python app.py
   ```

5. Open your web browser and navigate to `http://localhost:5000` to interact with your chatbot.

## Project Files
- `app.py`: The main Flask application file containing the server logic and chatbot integration
- `templates/index.html`: The HTML template for the front-end (not provided in the shared code)
- `static/css/styles.css`: CSS file for styling (not provided in the shared code)
- `static/script.js`: JavaScript file for front-end functionality (not provided in the shared code)

## Code Overview
The `app.py` file contains the following key components:

- Flask app initialization and CORS setup
- Loading of the BlenderBot model and tokenizer
- A route for serving the home page
- A `/chatbot` endpoint that handles POST requests for chatbot interactions
- Conversation history management

The chatbot uses the `facebook/blenderbot-400M-distill` model from Hugging Face Transformers. It maintains a conversation history to provide context for each interaction.

## Note on Scalability
The current implementation stores the entire conversation history in memory and includes it in each request to the model. This approach may lead to performance issues or crashes with very long conversations. For a production environment, consider implementing a more scalable solution for managing conversation history.

## Contributing
Contributions to improve the project are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to Hugging Face for the Transformers library and pre-trained models
- Inspired by ChatGPT and other conversational AI interfaces