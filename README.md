# Integrating your Chatbot into a Web Interface

## Introduction
This project demonstrates how to set up a back-end server and integrate a chatbot into a web application. It provides a practical approach to creating a ChatGPT-like website by combining a Flask-based back-end with a front-end webpage.

## Learning Objectives
After completing this project, you will be able to:
- Set up a back-end server
- Integrate a chatbot into a Flask server
- Implement communication between a web page and the back-end server

## Prerequisites
- Basic knowledge of Python programming
- Familiarity with building a simple terminal-based chatbot
- Understanding of HTML, CSS, and JavaScript basics

## Project Structure
The project consists of two main components:
1. A back-end server hosting the chatbot
2. A front-end webpage for user interaction

## Setup Instructions
1. Clone this repository:
   ```
   git clone https://github.com/ckabuya/chatbot-web-interface.git
   cd chatbot-web-interface
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
- `app.py`: The main Flask application file
- `templates/index.html`: The HTML template for the front-end
- `static/css/styles.css`: CSS file for styling
- `static/script.js`: JavaScript file for front-end functionality

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
- Thanks to IBM Skills for the initial chatbot implementation
- Inspired by ChatGPT and other conversational AI interfaces