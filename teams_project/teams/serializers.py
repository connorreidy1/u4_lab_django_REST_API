from rest_framework import serializers
from .models import League, Team, Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name='team_detail',
        read_only=True
    )
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source='team'
    )
    class Meta:
        model = Player
        fields = ('id', 'team_id', 'team', 'name', 'position', 'age', 'injured', 'image_url')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = PlayerSerializer(
        many=True,
        read_only=True
    )
    league_id = serializers.PrimaryKeyRelatedField(
        queryset=League.objects.all(),
        source='league'
    )
    class Meta:
        model = Team
        fields = ('id', 'league_id', 'name', 'location',  'number_of_wins', 'number_of_draws', 'number_of_loses', 'team_logo', 'players')


class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    teams = TeamSerializer(
        many=True,
        read_only=True
    )
    league_url = serializers.HyperlinkedIdentityField(
        view_name='league_detail'
    )
    class Meta:
        model = League
        fields = ('id', 'league_url', 'name', 'country', 'number_of_teams', 'year_founded', 'teams')