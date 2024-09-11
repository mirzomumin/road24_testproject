from datetime import timedelta
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.db.models import Case, When, CharField, F, Count, Q
from django.utils import timezone

from petrol_spy.serializers import LeaderboardSerializer

# Create your views here.

User = get_user_model()


class LeaderboardAPIView(generics.ListAPIView):
    serializer_class = LeaderboardSerializer

    def get_queryset(self):
        today = timezone.now()
        treshold = today - timedelta(days=30)
        queryset = User.objects.filter(
            Q(reports__created_at__gte=treshold)
        ).annotate(
            display_name=Case(
                When(
                    oneid_profile__isnull=True, then=F('username')
                ),
                default=F('oneid_profile__full_name'),
                output_field=CharField()
            ),
            reports_count=Count('reports')
        ).order_by('-reports_count').values(
            'id',
            'display_name',
            'reports_count')[:100]
        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'users': serializer.data})