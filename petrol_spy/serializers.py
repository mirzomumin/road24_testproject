from rest_framework import serializers


class LeaderboardSerializer(serializers.Serializer):
    id = serializers.IntegerField(default='', read_only=True)
    display_name = serializers.CharField(default='', read_only=True)
    reports_count = serializers.IntegerField(default=0, read_only=True)
