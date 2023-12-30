from django.shortcuts import render,HttpResponse
from src.logger import logging
from src.exception import CustomException
import sys
from src.pipelines.training_pipeline import TrainingPipeline
from django.contrib import messages

def home(request):
    logging.info(f"user is hitting the homepage")
    try:
        return render(request,"core/home.html")
    except Exception as e:
        diamond_exception=CustomException(e,sys)
        logging.info(diamond_exception.error_message)
        return HttpResponse("Some error occurred !")
    
def training_view(request):
    try:
        if request.method=='POST':
            tp=TrainingPipeline()
            tp.start_training()
            messages.success(request,"Training has been started")
        else:
            pass
        return render(request,"core/training.html")
    except Exception as e:
        exc=CustomException(e,sys)
        logging.error(f"{exc.error_message}")
        return HttpResponse(f"{exc.error_message}")
    
    
def prediction_view(request):
    try:
        if request.method=='POST':
            pass
        else:
            pass
        return render(request,"core/prediction.html")
    except Exception as e:
        exc=CustomException(e,sys)
        logging.error(f"{exc.error_message}")
        return HttpResponse(f"{exc.error_message}")
    
