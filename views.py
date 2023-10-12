from models.models import Grammar, Vocabulary, Text, Users
from rest_framework import viewsets
from rest_framework import permissions
from schemas.serializers import UserSerializer, GrammarSerializer, VocabularySerializer, TextSerializer 
import config.database as database


class GrammarViewSet(viewsets.ModelViewSet):
    
    queryset = database.client.CTGrammar.find()