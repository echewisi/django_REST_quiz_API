from rest_framework import serializers
from .models import Quizzes, Question, Answer

class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Quizzes
        fields=[
            'title',
        ]
        
#serializer for answers:
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Answer
        fields= [
            'id',
            'answer_text',
            'is_right'
        ]
class QuestionSerialzer(serializers.ModelSerializer):
    quiz= QuizSerializer(read_only= True)
    answer= AnswerSerializer(many= True, read_only= True)   
    class Meta:
        model= Question
        fields= [ 'quiz', 'title', 'answer',]

class RandomQuestionSerializer(serializers.ModelSerializer):
    answer= AnswerSerializer(many= True, read_only= True) #the information from the answer serializer will be brought here and replace--
    class Meta:
        model= Question
        fields= [
            'title',
            'answer' #--this one here.
        ]