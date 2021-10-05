from django.urls import path
from ML import views

urlpatterns = [
    path('',views.home,name='home'),
    path('ml',views.MachineLearning,name='machineLearning'),
    path('lstm',views.LSTM,name='lstm'),
    path('ann',views.ANN,name='ann'),
    path('result', views.result,name='result'),
    path('annResult', views.resultAnn,name='resultann'),
    path('lstmResult', views.resultLSTM,name='resultlstm'),
]