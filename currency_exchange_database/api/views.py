from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import EurUsdCurrencies
from .serializers import EurUsdSerializer
from yfinance import Ticker



class Currency(APIView):
    def get(self, request):
        r"""returns history of exchange rate, supports following query parameters:
                - limit - how many results should be displayed
                - order - order by id, if not 'ASC' provided, it is 'DESC'
                - **kwargs - any other query parameters, if are valid django filters, then these are applied
                """
        # sets limit due to query parameter, if nothing is provided, then sets 500 as a limit
        try:
            limit = request.GET.get('limit')
            if limit == 'none':
                pass
            else:
                try:
                    limit = int(limit)
                except:
                    limit = 500
        except:
            limit = 500



        # sets order, if there's no 'order=asc' (value is case insensitive), sets 'DESC'
        order = request.GET.get('order')
        query_params = dict(request.GET)
        try:
            if order.upper() == 'ASC':
                order = order.upper()
            else:
                order = "DESC"
        except:
            order = "DESC"

        # select all objects from EurUsdCurrencies model and order them by utc_timestamp
        currencies = EurUsdCurrencies.objects.all()
        currencies = currencies.order_by(f'{"-" if order == "DESC" else ""}utc_timestamp')

        # user queries, goes through query paramters and if it can be used as filter, it does it
        for key, value in query_params.items():
            if key.lower() == "order" or key.lower() == "limit":
                continue
            try:
                kwargs = {f'{key}': f'{value[0]}'}
                currencies = currencies.filter(**kwargs)
            except:
               pass

        # at the end it sets the max number of records if limit was not set to 'none'
        if limit != 'none':
            currencies = currencies[:limit]

        # process data through model serializer and return it as JSON
        serializer = EurUsdSerializer(currencies, many=True)
        return Response(serializer.data)


class CurrencyEurUsd(APIView):
    def get_eurusd(self):
        r"""returns exchange rate for EURUSD from yahoo finance using yfinance
        and saves search record fo the EurUsdCurrencies model"""
        # gets data ticker for EURUSD=X query and assigns value form 'open'
        eur_usd = Ticker("EURUSD=X")
        eur_usd = eur_usd.info['open']

        # saves the record to EurUsdCurrencies
        record = EurUsdCurrencies(open_rate=eur_usd)
        record.save()

        # return newly created record in EurUsdCurrencies
        return EurUsdCurrencies.objects.get(id=record.id)

    def get(self, request):
        r"""fetches data from Yahoo finance using yfinance and returns it as json response.
            additionaly saves the EUR/USD exchange rate with UTC timestamp to the EurUsdCurrencies"""
        # try statement is used here in case of Yahoo failures
        #   e.g when Yahoo is down or there's problem with user location (user is not in USA)
        try:
            eur_usd_exchange_rate = self.get_eurusd()
            serializer = EurUsdSerializer(eur_usd_exchange_rate, many=False)
            return Response(serializer.data)
        # handle the exception, if 404 Client Error shown, indicate user that only US users are allowed
        # in any other cases return 500 server error
        except Exception as error:
            if '404 Client Error:' in str(error):
                return Response({'message': 'Only USA users are supported.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

