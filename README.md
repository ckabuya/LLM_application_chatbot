# Integrating your Chatbot into a Web Interface

## Introduction
This project demonstrates how to set up a back-end server and integrate a chatbot into a web application. It provides a practical approach to creating a ChatGPT-like website by combining a Flask-based back-end with a front-end webpage. The chatbot uses the Hugging Face Transformers library with the BlenderBot model.

## Learning Objectives
After completing this project, you will be able to:
- Set up a back-end server using Flask
- Integrate a pre-trained chatbot model into a Flask server
- Implement communication between a web page and the back-end server
- Handle conversation history in a chatbot application
- Identify and address limitations in chatbot implementations

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
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```
   python app.py
   ```

5. Open your web browser and navigate to `http://localhost:5000` to interact with your chatbot.

## Project Files
- `app.py`: The main Flask application file containing the server logic and chatbot integration
- `templates/index.html`: The HTML template for the front-end
- `static/css/styles.css`: CSS file for styling
- `static/script.js`: JavaScript file for front-end functionality

## Original Implementation Limitations
The initial implementation of the chatbot based on the IBM Course forked from https://github.com/ibm-developer-skills-network/LLM_application_chatbot had several limitations:

1. **Conversation History Management**: The entire conversation history was stored in memory and included in each request to the model, leading to growing input sizes.

2. **Token Limit Exceeded**: As conversations grew longer, the input to the model would exceed its maximum token limit, causing the chatbot to crash after approximately 5 interactions.

3. **Memory Usage**: Storing the full conversation history in memory could lead to excessive memory usage over time.

4. **Error Handling**: The original implementation lacked robust error handling, making it difficult to diagnose and recover from issues.

5. **Scalability**: The approach of keeping the entire conversation history in memory is not scalable for long-running or multi-user scenarios.

## Improved Implementation
To address the limitations of the original implementation, the following improvements have been made:

1. **Truncated Conversation History**: The chatbot now keeps only the last few interactions (3-4 exchanges) in the history, maintaining recent context without overwhelming the model.

2. **Dynamic Input Length Management**: The code now respects the model's maximum input length, truncating the input when necessary to prevent crashes.

3. **Global Variable Usage**: The `conversation_history` is properly managed as a global variable, resolving scope-related errors.

4. **Error Handling**: A try-except block has been implemented to catch and handle exceptions gracefully, improving the chatbot's reliability.

5. **Debug Mode**: The Flask app now runs in debug mode during development, facilitating easier identification and resolution of issues.

6. **Conversation Management**: The overall length of the conversation history is now managed, preventing unbounded growth of the history list.

These improvements allow the chatbot to handle longer conversations without crashing and provide a more stable user experience.

## Future Enhancements
- Implement a database solution for storing conversation history
- Add user authentication and individual session management
- Explore more advanced language models for improved conversational abilities
- Implement more extensive logging and monitoring

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
- Thanks to Hugging Face for the Transformers library and pre-trained models, IBM Skills Network
- Inspired by ChatGPT and other conversational AI interfaces