import logging
import os
from typing import Optional
from datetime import datetime

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import google.generativeai as genai
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

# Direct configuration (temporary for testing)
TELEGRAM_TOKEN = "7304636626:AAGLX5PqRLK8GmpC7I2IRErvCPYhnCNDI2k"
GEMINI_API_KEY = "AIzaSyA-eiYwlDQ3R2_gEY_rAV8whjfQXi0tPoQ"
MONGO_URI = "mongodb://localhost:27017/telegram_bot"

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self):
        # Initialize Gemini
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-pro")
        
        # Initialize MongoDB
        self.db_client: Optional[MongoClient] = None
        self.db: Optional[Database] = None
        self.users: Optional[Collection] = None
        self.chats: Optional[Collection] = None
        self.setup_database()

    def setup_database(self):
        """Initialize database connections"""
        try:
            self.db_client = MongoClient(MONGO_URI)
            self.db = self.db_client.telegram_bot
            self.users = self.db.users
            self.chats = self.db.chats
            # Test the connection
            self.db_client.server_info()
            logger.info("Database connection established")
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            raise

    async def get_ai_response(self, user_input: str) -> str:
        """Get response from Gemini AI"""
        try:
            response = self.model.generate_content(user_input)
            return response.text
        except Exception as e:
            logger.error(f"Error getting AI response: {e}")
            return "Sorry, I encountered an error processing your request."

    async def store_message(self, user_id: int, message: str, response: str):
        """Store message in database"""
        try:
            self.chats.insert_one({
                "user_id": user_id,
                "message": message,
                "response": response,
                "timestamp": datetime.utcnow()
            })
        except Exception as e:
            logger.error(f"Error storing message: {e}")

    async def start_command(self, update: Update, context: CallbackContext) -> None:
        """Handle /start command"""
        try:
            user_id = update.effective_user.id
            self.users.update_one(
                {"_id": user_id},
                {
                    "$set": {
                        "username": update.effective_user.username,
                        "first_seen": datetime.utcnow()
                    }
                },
                upsert=True
            )
            await update.message.reply_text(
                'Welcome! I am your AI assistant powered by Gemini. Ask me anything!'
            )
        except Exception as e:
            logger.error(f"Error in start command: {e}")
            await update.message.reply_text(
                "Sorry, I encountered an error. Please try again later."
            )

    async def handle_message(self, update: Update, context: CallbackContext) -> None:
        """Handle incoming messages"""
        try:
            user_input = update.message.text
            user_id = update.effective_user.id
            
            # Get AI response
            response = await self.get_ai_response(user_input)
            
            # Store in database
            await self.store_message(user_id, user_input, response)
            
            # Send response
            await update.message.reply_text(response)
            
        except Exception as e:
            logger.error(f"Error handling message: {e}")
            await update.message.reply_text(
                "Sorry, I encountered an error processing your message."
            )

    def run(self):
        """Run the bot"""
        try:
            # Create application
            application = Application.builder().token(TELEGRAM_TOKEN).build()

            # Add handlers
            application.add_handler(CommandHandler("start", self.start_command))
            application.add_handler(MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                self.handle_message
            ))

            # Start the bot
            logger.info("Starting bot...")
            application.run_polling()
            
        except Exception as e:
            logger.error(f"Critical error: {e}")
            if self.db_client:
                self.db_client.close()

if __name__ == '__main__':
    bot = TelegramBot()
    bot.run()