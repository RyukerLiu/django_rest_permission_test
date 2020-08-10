from rest_framework import permissions


class ObjectPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print('Has Permission Function')
        print(request)
        print(view)

        return True


    def has_object_permission(self, request, view, obj):
        print('Has Object Permission Function')
        print(request)
        print(view)
        print(obj)


        return False