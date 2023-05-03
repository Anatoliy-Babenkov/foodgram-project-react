from rest_framework import permissions as p


class IsAdminOrReadOnly(p.BasePermission):

    def has_permission(self, request, view):
        return (request.method in p.SAFE_METHODS
                or request.user.is_staff)


class IsAuthorOrReadOnly(p.BasePermission):
    """Разрешение:

    Изменение и дополнение разрешены только автору.
    """

    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return (request.method in p.SAFE_METHODS
                or obj.author == request.user)
