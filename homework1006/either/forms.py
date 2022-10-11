from django import forms
from .models import Topic, Comment

class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        # fields = '__all__'
        exclude = ('user',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('article', 'user',)
