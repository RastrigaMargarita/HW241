from rest_framework import serializers

def validate_video_url(value):
    if not set(value) & set("youtube.com"):
        raise serializers.ValidationError("Можно размещать ссылки только на youtube")
