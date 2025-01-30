# Telegram AI Chatbot

This is a Telegram bot powered by Gemini AI, capable of responding to user queries, performing image/file analysis, and offering web search functionality. The bot allows users to interact with it in real-time while utilizing the Gemini API for natural language understanding and responses.

## Features
- **User Registration:** Secure registration for users before they can interact with the bot.
- **Gemini-powered Chat:** Provides AI-driven responses based on user input.
- **Image/File Analysis:** Users can send images or files for analysis via the bot.
- **Web Search Functionality:** The bot can fetch relevant web information based on queries.
- **Bonus Features (Under Development):**
  - Sentiment analysis for incoming messages.
  - Auto-translation for multilingual support.
  - User analytics dashboard to track interactions and behavior.

## Tech Stack
- **Programming Language:** Python
- **Framework:** `python-telegram-bot` (for Telegram bot functionality)
- **Database:** MongoDB (for storing user data and chat logs)
- **AI Model:** Gemini API (for chat and image analysis)
- **Libraries:** `httpx`, `requests`, `dotenv`
- **Environment:** VSCode, Telegram

## Setup Instructions

### Prerequisites
1. **Python 3.x**: Ensure that Python 3.x is installed on your system.
2. **Telegram Bot Token**: Create a bot using the [BotFather](https://core.telegram.org/bots#botfather) on Telegram and get the bot token.
3. **Gemini API Key**: Obtain an API key from Google’s Generative AI platform.

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/telegram_ai_chatbot.git
    ```

2. Navigate to the project directory:
    ```bash
    cd telegram_ai_chatbot
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables in a `.env` file:
    ```text
    TELEGRAM_API_KEY=<your-telegram-bot-token>
    GEMINI_API_KEY=<your-gemini-api-key>
    ```

5. Run the bot:
    ```bash
    python bot.py
    ```

### Running Locally
- Make sure that you have a stable internet connection to interact with the Telegram API and the Gemini API.
- The bot should now be live and ready to respond to user queries!

### Testing the Bot
- Open your Telegram app and search for your bot using the username you set with BotFather.
- Send messages to the bot, and it will reply based on the Gemini-powered responses.

## Troubleshooting
- **SSL Connection Issues:** If you encounter issues with connecting to Gemini API (e.g., SSL errors), ensure that your `httpx` and `requests` libraries are up-to-date.
- **Token Issues:** If you see an "InvalidToken" error, double-check your Telegram bot token and make sure it’s correctly set in your environment variables.

## Contributing
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Telegram API** for providing the framework for building chatbots.
- **Gemini API** for providing the AI-powered responses.
- **MongoDB** for storing user data and chat logs.
- **httpx** and **requests** for making HTTP requests to APIs.

---

Feel free to update the repository URL, license, and any other sections as needed!
