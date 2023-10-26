from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Currencies
from .serializers import CurrenciesSerializer
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
        currencies = Currencies.objects.all()
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
        serializer = CurrenciesSerializer(currencies, many=True)
        return Response(serializer.data)


class CurrencyConverter(APIView):
    def get_rate(self, base:str, quote:str):
        r"""returns exchange rate for {base}{quote} currency pair from yahoo finance using yfinance
        and saves search record to the Currencies model"""
        # gets data ticker for {base}{quote}=X query and assigns value form 'open' and ensure that values are uppercase
        rate = Ticker(f"{base.upper()}{quote.upper()}=X")
        rate = rate.fast_info['open']
        # saves the record to EurUsdCurrencies
        record = Currencies(base_currency=base.upper(),
                            quote_currency=quote.upper(),
                            open_rate=rate
                            #currency_pair=f"ABCDEF"
                            )
        record.save()
        # return newly created record in Currencies
        return Currencies.objects.get(id=record.id)

    def get(self, request, base, quote):
        r"""fetches data from Yahoo finance using yfinance and returns it as json response.
            additionaly saves the currency pair exchange rate with UTC timestamp to the Currencies"""
        # try statement is used here in case of failures
        #  e.g. when user provides not valid currency pair
        try:
            eur_usd_exchange_rate = self.get_rate(base.upper(),quote.upper())
            serializer = CurrenciesSerializer(eur_usd_exchange_rate, many=False)
            return Response(serializer.data)
        # handle the exception, if 404 Client Error shown, indicate user that currency pair is not found
        # in any other cases return 500 server error
        except Exception as error:
            print(error)
            if 'currentTradingPeriod' in str(error):
                return Response({'message': f'Didn\'t find currency pair with symbol {base}{quote}.'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message': f'Server Error - {error}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
