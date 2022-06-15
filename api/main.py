
from leanapi.server import ApiServer
from .app.core.app_config import AppConfig
from .routes.modules import modules


def start():
    server = ApiServer.config(configs=AppConfig.load()).loads(modules).server()
    server.start()


if __name__ == "__main__":
    start()
else:
    server = ApiServer.config(configs=AppConfig.load()).loads(modules).server()
    app = server.app
