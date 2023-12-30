from django.shortcuts import render,HttpResponse
from src.logger import logging
from src.exception import CustomException
import sys
from src.pipelines.training_pipeline import TrainingPipeline
from django.contrib import messages
from .forms import PredictionForm
from src.pipelines.prediction_pipeline import Predictionpipeline,CustomData

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
            fm=PredictionForm(request.POST)
            if fm.is_valid():
                carat=fm.cleaned_data['carat']
                depth=fm.cleaned_data['depth']
                table=fm.cleaned_data['table']
                x=fm.cleaned_data['x']
                y=fm.cleaned_data['y']
                z=fm.cleaned_data['z']
                cut=fm.cleaned_data['cut']
                color=fm.cleaned_data['color']
                clarity=fm.cleaned_data['clarity']
                customdata=CustomData(carat=carat,depth=depth,table=table,x=x,y=y,z=z,
                                      cut=cut,color=color,clarity=clarity)
                df=customdata.get_data_as_Dataframe()
                predictionpipeline=Predictionpipeline()
                output=predictionpipeline.predict(df)
                logging.info(f"Predicted price is ${output[0]}")
                messages.success(request,f"Predicted diamond price is ${output[0]} .")
        else:
            fm=PredictionForm()
        return render(request,"core/prediction.html",{'form':fm})
    except Exception as e:
        exc=CustomException(e,sys)
        logging.error(f"{exc.error_message}")
        return HttpResponse(f"{exc.error_message}")
    
