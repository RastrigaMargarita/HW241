from rest_framework import serializers

def validate_video_url(value):
    if not ("youtube.com" in value):
        raise serializers.ValidationError("Можно размещать ссылки только на youtube")
