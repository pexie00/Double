
from aiohttp import web

routes = web.RouteTableDef()

# From chatGPT
home_template = """
2023
"""

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.Response(text=home_template, content_type='text/html')


