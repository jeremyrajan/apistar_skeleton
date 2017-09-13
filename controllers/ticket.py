from apistar.backends.sqlalchemy_backend import Session
from models.Ticket import Ticket


def list_tickets(session: Session):
    """
      Return a JSON response
    """
    queryset = session.query(Ticket).all()
    return [
        {'id': ticket.id, 'name': ticket.name}
        for ticket in queryset
    ]
