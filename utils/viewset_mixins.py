class DualViewSetMixin(object):
    """
    Use a different serializer and queryset for the 'retrieve' action
    """

    def get_queryset(self):
        if self.action == 'retrieve':
            return self.detail_queryset
        return self.queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return self.serializer_class
