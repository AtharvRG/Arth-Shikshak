<div align="center">
  <img src="https://github.com/your-username/your-repo-name/blob/master/assets/arth_shikshak_logo.png?raw=true" alt="Arth Shikshak Logo" width="200"/>
  <h1 align="center">Arth Shikshak: Your AI-Powered Financial Guide 💰</h1>
</div>

<p align="center">
  <a href="https://streamlit.io/">
    <img src="https://img.shields.io/badge/Made%20with-Streamlit-brightgreen.svg" alt="Made with Streamlit">
  </a>
  <a href="https://pypi.org/project/google-generativeai/">
    <img src="https://img.shields.io/pypi/v/google-generativeai" alt="PyPI version">
  </a>
  <a href="https://github.com/your-username/your-repo-name/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  </a>
</p>

## Project Description

**Arth Shikshak** is a Streamlit application designed to provide users with personalized financial guidance and education. This AI-powered tool, built with Gemini, offers an interactive chat interface to discuss various financial topics, including budgeting, saving, investments, and more.  It aims to empower users to make informed financial decisions.

## Key Features

* **Interactive Chat with Gemini:** Engage in natural language conversations with an AI assistant (Arth Shikshak) to get answers to your financial questions.
* **Personalized Advice:** The application considers your unique financial situation (income, savings, expenses) to provide tailored recommendations.
* **Financial Education:** Learn about key financial concepts and strategies to improve your financial literacy.
* **Chat History:** Review past conversations to revisit previously discussed topics and advice.
* **User-Friendly Interface:** Streamlit provides a simple and intuitive interface for easy interaction.
* **Accessibility:** Designed to be accessible to a wide range of users, regardless of their technical expertise.

## Tech Stack

* [Streamlit](https://streamlit.io/): For building the web application.
* [Google Gemini](https://ai.google.com/): For the AI-powered chat functionality.
* [joblib](https://joblib.readthedocs.io/en/latest/): For efficient data persistence.

## Installation

1.  Clone this repository:

    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3.  Obtain a Google Gemini API key and set it in `main.py`:

    ```python
    # main.py
    GOOGLE_API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key
    ```

4.  Run the application using Streamlit:

    ```bash
    streamlit run main.py
    ```

## Usage

1.  Open the application in your web browser.
2.  On the input page, enter your financial details (income, expenses, etc.) to personalize the advice.
3.  Navigate to the chat page to start interacting with Arth Shikshak.
4.  Ask questions about any financial topic, and the AI will provide relevant information and guidance.

## Future Enhancements

* Integration with financial data providers for real-time market information.
* Implementation of more advanced financial planning tools (e.g., retirement calculators, investment portfolio optimizers).
* Support for multiple languages.
* Enhancements to the AI's knowledge base and conversational abilities.
* User authentication and account management.

## Contributions

Contributions are welcome! Feel free to submit pull requests to improve the application's functionality, add new features, or enhance the user experience. Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write your code and tests.
4.  Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
