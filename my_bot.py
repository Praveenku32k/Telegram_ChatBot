from aiogram import Bot, Dispatcher,executor, types
from dotenv import load_dotenv
import os 
import logging
import openai


load_dotenv()
TOKEN=os.getenv("TOKEN")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

# connect with OpenAI

openai.api_key = OPENAI_API_KEY
# print("Connecting to OpenAI")

#setting the Model Name 
MODEL_NAME="gpt-3.5-turbo"

#Initilize the bot 
bot =Bot(token=TOKEN)
dispatcher =Dispatcher(bot)

class Reference:
    def __init__(self)->None:
        self.resource = ""



Reference = Reference()

def clear_paste():
    Reference.response = ""




@dispatcher.message_handler(commands=['start'])
async def command_start_handler(message : types.Message):

    """This is the handler receives message with '/start' or '/help' command 

    Args:
     message (types.Message): _description_

    """
    await message.reply("Hi!\n I am a chat bot! created by Praveen\n How can I assist you !")



@dispatcher.message_handler(commands=['help'])
async def helper(message : types.Message):

    """
    A Handler to display help information    
    """

 
    help_command ="""
    Hi There , I'm  a chat bot created by Praveen! Please follow this commands
    /start - To start the chatbot
    /clear - To clear the past conversation and context.
    /help - To display this message.
    I hope this helps. :)
    """

    await message.reply(help_command)




if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)



