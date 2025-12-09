
# dashboard/models.py
from clients.models import Message as ClientsMessage

class DashboardMessage(ClientsMessage):
    class Meta:
        proxy = True
        verbose_name = "Message"
        verbose_name_plural = "Messages"
