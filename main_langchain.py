import langchain
import os
from langchain import OpenAI 
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory,ConversationSummaryMemory,CombinedMemory
from langchain.tools import YouTubeSearchTool
from langchain.agents import Tool,load_tools,initialize_agent
from langchain.tools import BaseTool
from langchain.agents import initialize_agent,AgentType
from bs4 import BeautifulSoup
import requests
from langchain.prompts.chat import SystemMessagePromptTemplate
from constants import Constants
from tools import all_tools


os.environ["OPENAI_API_KEY"] = Constants.ApiKey
os.environ["SERPAPI_API_KEY"] = Constants.Serapi_key


conv_memory = ConversationBufferWindowMemory(
    memory_key="Chat_History_lines",input_key="input",k=3
)
summary_memory = ConversationSummaryMemory(llm = OpenAI(),input_key="input")

main_memory = CombinedMemory(memories=[conv_memory,summary_memory])

llm = OpenAI(temperature=0)
turbo_llm = ChatOpenAI(
    temperature=0,
    model_name='gpt-3.5-turbo',
    max_retries=2,
    max_tokens=1000
)

conversational_agents = initialize_agent(
    all_tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors="Check your output and make sure it conforms!",
    verbose = True,
    max_iterations=3,
    max_execution_time=60, 
    early_stopping_method='generate',
    memory = conv_memory
)

print("Hello how can I help you today")
while True:
    try:
        input_user = input("Is there anything you want to ask or would you like me perform any task : ")
        if input_user.lower() == "exit":
            exit()
        print(conversational_agents.run(input_user))
    except Exception as e:
        print(f"\nSorry Exception Occurred please try again : {str(e)}")

