from aiohttp import web

async def handle_root(request):
    return web.Response(text='Root page')

async def handle_about(request):
    return web.Response(text='About page')

app = web.Application()
app.router.add_get('/', handle_root)
app.router.add_get('/about', handle_about)

web.run_app(app)