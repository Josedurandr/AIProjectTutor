from models.models import GrammarModel, VocabularyModel, TextModel, UserModel
from rest_framework import serializers

class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['name', 'email', 'preferred_languages', 'skill_level', 'experience_level']

class TextSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TextModel
        fields = ['text', 'language', 'category']

class GrammarSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GrammarModel
        fields = ['rule', 'explanation', 'examples']

class VocabularySerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VocabularyModel
        fields = ['word', 'translation']