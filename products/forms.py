from django import forms
from .models import *
# Эта формочка будет работать с моделью

# class SubscriberForm(forms.ModelForm):  # Название обычно дают по имени модели плюс Form
#
#     class Meta:  # В Meta-классе можем указать доп. настройки
#         model = Subscriber  # Скажем, с какой моделью мы работаем
#         exclude = [""]
#         # fields это список, в котороом мы указываем, какие поля (из модели) должны присутсвоватьв самой формочке
#         # exclude - это поля, которые нужно исключить. Или его, или предыдущих используют
