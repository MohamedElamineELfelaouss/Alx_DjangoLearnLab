from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Notification


class NotificationListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.all().order_by("-timestamp")
        data = [
            {
                "id": notification.id,
                "actor": notification.actor.username,
                "verb": notification.verb,
                "target": str(notification.target),
                "timestamp": notification.timestamp,
                "read": notification.read,
            }
            for notification in notifications
        ]
        return Response(data, status=status.HTTP_200_OK)
