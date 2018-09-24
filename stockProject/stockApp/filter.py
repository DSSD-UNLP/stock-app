class ProductFilter(object):
    def __init__(self, queryset, request):
        self.queryset = queryset
        self.request = request

    def products(self):
        if self.request.GET.get('name') != None:
            self.queryset = self.queryset.filter(name__contains = self.request.GET.get('name'))
        if self.request.GET.get('price') != None:
            self.queryset = self.queryset.filter(cost_price= self.request.GET.get('price'))
        return self.queryset.order_by('name')