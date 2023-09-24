from langchain.agents import Tool, load_tools, initialize_agent, AgentType
from langchain.tools import BaseTool, GoogleSearchResults, wikipedia, StructuredTool
from langchain.chat_models import ChatOpenAI
from constants import Constants
from langchain import LLMChain,PromptTemplate
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.output_parsers import OutputFixingParser
from args_shcema_collections import CalenderSend
from google_calender_function import GoogleCalender
import os


os.environ["OPENAI_API_KEY"] = Constants.ApiKey

llm = ChatOpenAI(temperature=0, max_retries=2, max_tokens=1000)

tools = [
    StructuredTool.from_function(
        name = "read_events",
        func=GoogleCalender().read_num_events,
        description="This function is used to read the upcoming events from the calender,input should be the num of events to be read deafult value should 0 if not given by the user,output will be the event time and event summary"
    ),
    StructuredTool.from_function(
        name = "create_event",
        func=GoogleCalender().create_event,
        description="This function is useful when user wants to create a event, here the input will be event_name in str, startTime, endTime in this format %Y-%m-%dT%H:%M:%S%z and finally emails which will be a list of object where key will be 'email' and value will be the attendees email id, in the output the link for the meet will be provided",
        args_schema=CalenderSend
    )
]

conversational_agents_calender = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors="Check your output and make sure it conforms!",
    verbose = True,
    max_iterations=3,
    max_execution_time=60, 
    early_stopping_method='generate',
)


# print("Hello how can I help you today")
# while True:
#     try:
#         input_user = input("Is there anything you want to ask or would you like me perform any task : ")
#         if input_user.lower() == "exit":
#             exit()
#         print(conversational_agents_calender.run(input_user))
#     except Exception as e:
#         print(f"\nSorry Exception Occurred please try again : {str(e)}")