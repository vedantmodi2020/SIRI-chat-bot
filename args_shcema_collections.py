from pydantic import BaseModel

class SearchByDateInput(BaseModel):
    date: list

class EmailSend(BaseModel):
    data: dict

class EmailSendAttachments(BaseModel):
    data: dict

class WhatsappSend(BaseModel):
    data: list