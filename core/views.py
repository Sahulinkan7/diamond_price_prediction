from django.shortcuts import render,HttpResponse
from src.logger import logging
from src.exception import CustomException
import sys

def home(request):
    logging.info(f"user is hitting the homepage")
    try:
        i=10/0
        return render(request,"core/home.html")
    except Exception as e:
        diamond_exception=CustomException(e,sys)
        logging.info(diamond_exception.error_message)
        raise CustomException(e,sys) from e
    finally:
        return HttpResponse("Hello")
    
