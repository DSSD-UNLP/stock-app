class ProductFilter(object):
    def __init__(self, queryset, request):
        self.queryset = queryset
        self.request = request
        self.valid_orders = ['name', 'sale_price', 'cost_price']

    def products(self):
        order = 'name'
        if self.request.GET.get('order') != None:
            tmp_order = self.request.GET.get('order')
            if tmp_order in self.valid_orders:
                order = tmp_order
        if self.request.GET.get('name') != None:
            self.queryset = self.queryset.filter(name__contains = (self.request.GET.get('name')).strip())
        if self.request.GET.get('cost_price_less') != None:
            self.queryset = self.queryset.filter(cost_price__lte = self.request.GET.get('cost_price_less'))
        if self.request.GET.get('cost_price_more') != None:
            self.queryset = self.queryset.filter(cost_price__gte = self.request.GET.get('cost_price_more'))
        if self.request.GET.get('sale_price_less') != None:
            self.queryset = self.queryset.filter(sale_price__lte = self.request.GET.get('sale_price_less'))
        if self.request.GET.get('sale_price_more') != None:
            self.queryset = self.queryset.filter(sale_price__gte = self.request.GET.get('sale_price_more'))
        return self.queryset.order_by(order)

class TypeFilter(object):
    def __init__(self, queryset, request):
        self.queryset = queryset
        self.request = request

    def types(self):
        if self.request.GET.get('name') != None:
            self.queryset = self.queryset.filter(name__contains = (self.request.GET.get('name')).strip())
        if self.request.GET.get('description') != None:
            self.queryset = self.queryset.filter(description__contains = self.request.GET.get('description'))
        return self.queryset.order_by('name')