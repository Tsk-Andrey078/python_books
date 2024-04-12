from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .models import Book, UserProfile
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BooksDynamicSerializer(serializers.ModelSerializer):
    def __init__(self, fields=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in set(self.fields.keys()) - set(fields):
            del self.fields[field_name]
        
    class Meta:
        model = Book
        fields = '__all__'
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


