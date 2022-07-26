from models import Cars

class BaseSerializer:
    class Meta:
        fields = []
        queryset = []

    def serialize_obj(self, obj):
        fields = self.Meta.fields
        dict_ = {}
        for field in fields :
            dict_[field] = getattr(obj, field)
        return dict_
        
    def serialize_queryset(self, queryset = None):
        if queryset is None:
            queryset = self.Meta.queryset
        list_ = []
        for obj in queryset:
            dict_ = self.serialize_obj(obj)
            list_.append(dict_)
        return list_

class CarSerializer(BaseSerializer):
    class Meta:
        fields = ['id', 'brend', 'model', 'year', 'color', 'type_', 'engine', 'price', 'mileage']
        queryset = Cars.object
