from django.urls import path

from petrol_spy.views import LeaderboardAPIView


urlpatterns = [
    path('leaderboard/', LeaderboardAPIView.as_view()),
]