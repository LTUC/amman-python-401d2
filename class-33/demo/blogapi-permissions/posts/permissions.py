from rest_framework import permissions

class PermissionsClass(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Admin Permissions
        if request.user.id == 1:
            return True
        # Prevent users from delete except admin
        if request.method == 'DELETE' and request.user.id != 1:
            return False
        print(request.method)
        # READ ONLY
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write Permission for author of blog
        if request.user == obj.author:
            return True


