class ProductFilter(object):
    def __init__(self, queryset, request):
        self.queryset = queryset
        self.request = request

    def products(self):
        order = 'name';
        if self.request.GET.get('order') != None:
            order = self.request.GET.get('order')
        #Implementar de alguna manera un limite de cantidad de productos a devolver
        #if self.request.GET.get('limit') != None:
        #    self.queryset = self.queryset[:int(self.request.GET.get('limit'))]
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