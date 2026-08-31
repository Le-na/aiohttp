from aiohttp import web


def create_app():
    app = web.Application()
    app.router.add_static("/static", "static")
    return app

if __name__ == "__main__":
    app = create_app()
    web.run_app(app)




