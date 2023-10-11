from models import Grammar, Vocabulary, Text, Users
from rest_framework import serializers

class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['name', 'email', 'preferred_languages', 'skill_level', 'experience_level']

class TextSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Text
        fields = ['text', 'language', 'category']

class GrammarSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grammar
        fields = ['rule', 'explanation', 'examples']

class VocabularySerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ['word', 'translation']