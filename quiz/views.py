from django.shortcuts import render
from rest_framework import generics
from .models import Quizzes, Question
from .serializers import QuizSerializer, RandomQuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class Quiz(generics.ListAPIView):
    serializer_class= QuizSerializer
    queryset= Quizzes.objects.all()

class RandomQuestion(APIView):
    
    def get(self, request, format: None, *args, **kwargs):
        question= Question.objects.filter(quiz__title= kwargs['topic']).order_by('?')[:1]
        serializer= RandomQuestionSerializer(question, many= True)

        return Response(serializer.data)
# Create your views here.
