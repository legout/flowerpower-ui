from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from htmy import render_template
import os
from datastar_py import Datastar, DatastarSSE

app = FastAPI()

# Initialize Datastar and store
datastar = Datastar()
store_name = "counter"
datastar.create_store(store_name, initial_value=0)

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/page", response_class=HTMLResponse)
async def render_htmy_page(request: Request):
    html = render_template(
        os.path.join(TEMPLATES_DIR, "index.htmy"),
        {
            "title": "Welcome Page",
            "heading": "Hello from htmy + FastAPI!"
        }
    )
    return HTMLResponse(content=html)

# SSE endpoint for Datastar
@app.get("/datastar/sse")
async def datastar_sse(request: Request):
    sse = DatastarSSE(datastar, request)
    return await sse.stream()

# Endpoint to increment the counter store (for testing real-time updates)
@app.post("/datastar/increment")
async def increment_counter():
    value = datastar.get(store_name)
    new_value = value + 1
    datastar.set(store_name, new_value)
    return {"counter": new_value}