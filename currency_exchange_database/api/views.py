from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from yfinance import Ticker

class Currency(APIView):
    def get(self, request):
       pass


class CurrencyEurUsd(APIView):
    def convert_currency_to_eurusd(self, request):
        pass

    def get(self, request):
        pass
