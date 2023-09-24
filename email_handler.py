from langchain.agents import Tool, load_tools, initialize_agent, AgentType
from langchain.tools import BaseTool, GoogleSearchResults, wikipedia, StructuredTool
from langchain.chat_models import ChatOpenAI
from constants import Constants
from notion import NotionClient
from langchain import LLMChain,PromptTemplate
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from open import open_app
from langchain.output_parsers import OutputFixingParser
from terminal import run_command
from email_function import GoogleEmail
from args_shcema_collections import SearchByDateInput,EmailSend,EmailSendAttachments
import os


os.environ["OPENAI_API_KEY"] = Constants.ApiKey

llm = ChatOpenAI(temperature=0, max_retries=2, max_tokens=1000)

tools = [
    StructuredTool.from_function(
        name = "read_email_by_subject",
        func = GoogleEmail().search_by_subject,
        description="This function is used to search any emails when user want to search the email by a particular subject,the input should be the subject mentioned by the user"
    ),
    StructuredTool.from_function(
        name="read_email_by_date",
        func = GoogleEmail().search_by_date,
        description="This function is used to search any email when the user ask to search emails based on any date range, the input for this function will be two date in string inside a list",
        args_schema= SearchByDateInput
    ),
    StructuredTool.from_function(
        name="read_email_by_sender",
        func =GoogleEmail().search_by_sender,
        description="This function is used when user wants to search the emails send by any particular email id which will be provided by the user, input should be the email-id provided by the user"
    ),
    StructuredTool.from_function(
        name="print_email_in_plain",
        func =GoogleEmail().print_message_content_plain,
        description="This function is used to print the email in plain text using the message id which is received after running any of the search function, input here should be the message id which needs to be printed"
    ),
    StructuredTool.from_function(
        name="print_email_in_html",
        func=GoogleEmail().print_message_content_html,
        description="This function is used to print the email in the html format using the message id received after running either any of the search function, input here should be the message id of the email which we want to print"
    ),
    StructuredTool.from_function(
        name="send_email_only",
        func=GoogleEmail().send_email,
        description="This function is used when the user wants to send a mail to someone but without any attachments,input here will be receiver email id, subject and message_body",
        args_schema= EmailSend
    ),
    StructuredTool.from_function(
        name="send_email_with_attachments",
        func=GoogleEmail().send_email_attachments,
        description="This function is used when the user wants to send the email to someone with any attachments, input here will be to_email, subject, message_body and file_path",
        args_schema=EmailSendAttachments
    )

]


conversational_agents_email = initialize_agent(
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
#         print(conversational_agents_email.run(input_user))
#     except Exception as e:
#         print(f"\nSorry Exception Occurred please try again : {str(e)}")