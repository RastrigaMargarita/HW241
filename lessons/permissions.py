from rest_framework.permissions import BasePermission


class IsOwnerOrModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user == view.get_object().owner:
            return True

        return not request.user.groups.filter(name='Moderator').exists()


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user == view.get_object().owner
