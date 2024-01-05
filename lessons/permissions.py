from rest_framework.permissions import BasePermission, IsAuthenticated


class IsOwnerOrModerator(BasePermission):
    def has_permission(self, request, view):
        if [IsAuthenticated]:
            print(request.user)
            print(view.get_object().owner)
            print(request.user.groups.filter(name='Moderator').exists())
            if request.user == view.get_object().owner:
                return True

            return request.user.groups.filter(name='Moderator').exists()
        return False


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if [IsAuthenticated]:
            return request.user == view.get_object().owner
        return False
class IsNotModerator(BasePermission):
    def has_permission(self, request, view):
        if [IsAuthenticated]:
            return not request.user.groups.filter(name='Moderator').exists()
        return True