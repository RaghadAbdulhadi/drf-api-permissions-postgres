from rest_framework import serializers
from perfumes_blog.models import Perfume

class PerfumeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'purchaser', 'perfume_name', 'perfume_description', 'perfume_price','perfume_price','perfume_edition', 'perfume_size',)
        model = Perfume