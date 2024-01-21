from rest_framework.serializers import ModelSerializer

from .models import Post


class PostSerilazer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'text', 'publish_date', 'status')


