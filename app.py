from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from apistar.backends import sqlalchemy_backend
from metadata import Base

# Controllers
from controllers.health import health
from controllers.event import *
from controllers.ticket import *


settings = {
  "DATABASE": {
    "URL": "postgresql://root:root@localhost:5432/api",
    "METADATA": Base.metadata
  }
}

routes = [
    Route('/health', 'GET', health),
    Route('/events', 'GET', list_events),
    Route('/tickets', 'GET', list_tickets),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

app = App(
    routes=routes,
    settings=settings,
    commands=sqlalchemy_backend.commands,  # Install custom commands.
    components=sqlalchemy_backend.components  # Install custom components.
)

if __name__ == '__main__':
    app.main()
