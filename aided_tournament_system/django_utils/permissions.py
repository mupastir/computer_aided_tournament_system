import participant
from participant.models import Referee
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class IsRefereeScorerOrAdmin(permissions.BasePermission):
    @staticmethod
    def _is_referee_scorer(request):
        try:
            Referee.objects.get(user_id=request.user.id, role="scr")
        except participant.models.Referee.DoesNotExist:
            return False
        else:
            return True

    def has_permission(self, request, view):

        return bool(
            self._is_referee_scorer(request) or (request.user and request.user.is_staff)
        )

    def has_object_permission(self, request, view, obj):

        return bool(
            self._is_referee_scorer(request) or (request.user and request.user.is_staff)
        )
