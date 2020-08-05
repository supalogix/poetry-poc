from fastapi import FastAPI
from fastapi_utils.openapi import simplify_operation_ids
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from domain.security.command import login

app = FastAPI()


class Result(BaseModel):
    status: str

class Empty(BaseModel):
    pass

class AddTopicResultType(str, Enum):
    TOPIC_ADDED = "TOPIC_ADDED"
    DUPLICATE_TOPIC_ERROR = "DUPLICATE_TOPIC_ERROR"

class TopicAdded(BaseModel):
    id: str

class AddTopicResponse(BaseModel):
    result_type: AddTopicResultType
    TOPIC_ADDED: Optional[TopicAdded]
    DUPLICATE_TOPIC_ERROR: Optional[Empty]

app.include_router(login.router)

#@app.post(
#    "/api/inventory/command/get_available_topics",
#    tags=["inventory"]
#)
#async def getAvailableTopics():
#    pass
#
#@app.post(
#    "/api/identity/command/authenticate",
#    tags=["identity"]
#)
#async def authenticate():
#    pass
#
#@app.post(
#    "/api/access/query/get_actions",
#    tags=["access"]
#)
#async def getActions():
#    pass
#
#@app.post(
#    "/api/topic/command/add_topic",
#    description="".join([
#        "this is a description. this is a description. this is a description. this is a description. this is a description. ",
#        "<br />",
#        "this is a description. this is a description. this is a description. this is a description. this is a description. ",
#        "<br />",
#        "this is a description. this is a description. this is a description. this is a description. this is a description. "
#    ]),
#    tags=["topic"],
#    response_model=AddTopicResponse
#)
#async def addTopic():
#    pass
#
#@app.post(
#    "/api/topic/command/rename_topic",
#    tags=["topic"]
#)
#async def renameTopic():
#    pass
#
#@app.post(
#    "/api/topic/command/remove_topic",
#    tags=["topic"]
#)
#async def removeTopic():
#    pass


simplify_operation_ids(app)

