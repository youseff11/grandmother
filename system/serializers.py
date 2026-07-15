from rest_framework import serializers
from .models import Category, Phrase, Person


class CategorySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'image_url', 'order', 'created_at']
        read_only_fields = ['id', 'created_at']

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class PhraseSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    audio_url = serializers.SerializerMethodField()
    category_name = serializers.CharField(source='category.name', read_only=True)
    # علشان الأدمن يقدر يمسح التسجيل الصوتي ويرجع لصوت جوجل (TTS)
    remove_audio = serializers.BooleanField(write_only=True, required=False, default=False)

    class Meta:
        model = Phrase
        fields = [
            'id', 'text', 'category', 'category_name', 'image', 'image_url',
            'audio', 'audio_url', 'remove_audio', 'order', 'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'image': {'required': False},
            'audio': {'required': False},
        }

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    def get_audio_url(self, obj):
        if obj.audio:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.audio.url)
            return obj.audio.url
        return None

    def create(self, validated_data):
        validated_data.pop('remove_audio', False)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        remove_audio = validated_data.pop('remove_audio', False)
        if remove_audio and instance.audio:
            instance.audio.delete(save=False)
            instance.audio = None
        return super().update(instance, validated_data)


class PersonSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    audio_url = serializers.SerializerMethodField()
    remove_audio = serializers.BooleanField(write_only=True, required=False, default=False)

    class Meta:
        model = Person
        fields = [
            'id', 'name', 'relation', 'image', 'image_url',
            'audio', 'audio_url', 'remove_audio', 'order', 'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'image': {'required': False},
            'audio': {'required': False},
        }

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

    def get_audio_url(self, obj):
        if obj.audio:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.audio.url)
            return obj.audio.url
        return None

    def create(self, validated_data):
        validated_data.pop('remove_audio', False)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        remove_audio = validated_data.pop('remove_audio', False)
        if remove_audio and instance.audio:
            instance.audio.delete(save=False)
            instance.audio = None
        return super().update(instance, validated_data)