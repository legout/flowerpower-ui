from sanic import Sanic
from sanic.response import html, text, json, redirect
from sanic.request import Request
# from app.components import (
#     landing_page,
#     base_layout,
#     projects_page,
#     new_project_page,
#     project_card,
# )
from .setup import setup_project_manager
import htpy as h

def base_layout(content):
    pass



app = Sanic("FlowerPowerUI")

# Global project manager instance
@app.listener("before_server_start")
async def setup(app, loop):
    setup_project_manager(app)

@app.route("/")
async def index(request: Request):