from apistar.backends.sqlalchemy_backend import Session
from models.Event import Event


def list_events(session: Session):
    """
      Return a JSON response
    """
    queryset = session.query(Event).all()
    return [
        {'id': event.id, 'name': event.name}
        for event in queryset
    ]
