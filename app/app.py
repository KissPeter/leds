import os
import time
from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.datastructures import MutableHeaders
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from starlette.types import ASGIApp, Message, Receive, Scope, Send
from fastapi.responses import ORJSONResponse, UJSONResponse, JSONResponse
import json

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI(debug=False
              )

@app.post("/sync/items/")
def create_item(item: Item):
    return Response(status_code=208)
