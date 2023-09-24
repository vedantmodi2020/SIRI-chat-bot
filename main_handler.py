from langchain.agents import Tool, load_tools, initialize_agent, AgentType
from langchain.tools import BaseTool, GoogleSearchResults, wikipedia,  StructuredTool
from langchain.chat_models import ChatOpenAI
from spotify import SpotifyControl
from constants import Constants
from notion import NotionClient
from langchain import LLMChain,PromptTemplate
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from open import open_app
from langchain.output_parsers import OutputFixingParser
from terminal import run_command
import os
from email_handler import conversational_agents_email
from whatsapp_function import send_whatsapp_message
from args_shcema_collections import WhatsappSend
from calender_handler import conversational_agents_calender


os.environ["OPENAI_API_KEY"] = Constants.ApiKey
os.environ["SERPAPI_API_KEY"] = Constants.Serapi_key

client = NotionClient(Constants.token, Constants.database_id)

llm = ChatOpenAI(temperature=0, max_retries=3, max_tokens=1000)
search = GoogleSearchResults

llm_chatChain = LLMChain(llm=llm ,prompt=PromptTemplate(template=Constants.conversational_chain_template, input_variables=["input"]))

tools = [ Tool.from_function(
        name="spotify_pause",
        func=SpotifyControl().pause_song,
        description="Useful for when the user want to pause the current song,direct call the function no input is required",
    ), Tool.from_function(
        name="spotify_play",
        func=SpotifyControl().play_song,
        description="Useful for when the user want to play a song ,input will be a song name or a song name  + artist name in a single string, for any other operation such as search or recommending it is not useful it will be only use to play the song, if you don't have song then search the song based on the user query and then execute this function"
    ), Tool.from_function(
        name="artist_songs",
        func=SpotifyControl().get_artist_top_tracks,
        description="Useful for when the user wants to know the songs for a particular artist,input will be the artist name and the output will be the list of objects with song name and their uri"
    ), Tool.from_function(
        name="write_notes",
        func=client.create_page,
        description="Useful when the user wants to write anything in the notion and save it, input will be the content mentioned by the user"
    ), Tool.from_function(
        name = "Open-APP",
        func=open_app,
        description = "Useful when the user wants to open a app in a system , input should be only the app name in lower case characters",
    ), Tool.from_function(
        name="Play_song_uri",
        func=SpotifyControl().play_song_uri,
        description="This Tool is used when you want to play a song directly using the uri,input will be the uri of the song the uri is type of a url not any simple string or an integer",
    ), Tool.from_function(
        name = "email handler",
        func=conversational_agents_email.run,
        description="This function will be useful when the user needs to perform any query related to the email, user input (directly no change in the input given by the user), the output will be directly the response given by the function",
    ), Tool.from_function(
        name = "Whatsapp messenger",
        func=send_whatsapp_message,
        description="This tool will be used to send the whatsapp message only to anyone, input will be to, message",
    ), Tool.from_function(
        name = "calender handler",
        func=conversational_agents_calender.run,
        description="This function will be useful when user wants to perform anything related to their calender or creating some events in their calender,user input (directly no change in the input given by the user), "
    ),
]

in_built_tools = load_tools(["serpapi", "llm-math","wikipedia","terminal"], llm=llm)


all_tools = tools + in_built_tools




