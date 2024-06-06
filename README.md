# Simple Chatbot

This is a simple chatbot created using Python and spaCy. The chatbot can respond to common questions and perform specific tasks.

## Features

- Responds to greetings like "hi", "hey", or "hello".
- Introduces itself and provides information about its creation.
- Handles user introductions.
- Ends the conversation when the user types "quit".
- Responds to questions about weather, jokes, age, music, and more.

## Requirements

- Python 3.x
- spaCy
- NLTK

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ShadBalti/simple-chatbot.git
   ```
2. Navigate to the project directory:
   ```sh
   cd simple-chatbot
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
4. Download the necessary NLTK data:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   nltk.download('averaged_perceptron_tagger')
   nltk.download('nps_chat')
   ```
5. Download the spaCy model:
   ```sh
   python -m spacy download en_core_web_sm
   ```

## Usage

Run the chatbot script:
```sh
python advanced_chatbot.py
```

## Example Interaction

```
You: Hi
Chatbot: Hello!
You: What is your name?
Chatbot: I am a chatbot created by you.
You: How are you?
Chatbot: I'm doing good, thank you for asking!
You: Tell me a joke.
Chatbot: Why don't scientists trust atoms? Because they make up everything!
You: quit
Chatbot: Bye, take care!
```

## License

This project is licensed under the MIT License.
