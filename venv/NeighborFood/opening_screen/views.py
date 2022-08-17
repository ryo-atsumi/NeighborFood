from django.views.generic.edit import FormView
from django.db import models
from . models import Result
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from . import forms
import requests
import json

import os
from dotenv import load_dotenv

class Index(FormView):

    #フォームの設定
    form_class = forms.SearchForm
    template_name = "opening_screen/index.html"

    def form_valid(self, form):

        #フォームからデータの受取
        data = form.cleaned_data
        search_word = data['search_word']

        #GetLocationクラスをインスタンス化し、現在地を取得
        lc = GetLocation()
        lat = lc.latitude
        lng = lc.longitude


        #APIキーとURLの設定
        API_KEY = os.environ.get("API_KEY")
        url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

        #検索条件の設定
        query = {
            'key': API_KEY,
            'name': search_word,
            'lat': lat,
            'lng': lng,
            'range': '5',
            'count': 100,
            'format': 'json'
        }

        #APIを実行しリスト（result）に格納する
        response = requests.get(url, query)
        result = json.loads(response.text)['results']['shop']

        #検索結果が0の場合はデータエラーを投げる
        try:
            if not result:
                raise DataError("検索条件に一致するお店が見つかりませんでした")

        #エラーの場合は画面にエラーメッセージを返す
        except DataError as e:
            
            ctxt = self.get_context_data(data_error_message=e)
            return self.render_to_response(ctxt)
            
        #通常時の処理
        else:
            #DBのデータを削除する
            Result.objects.all().delete()

            #DBにお店情報を保存する
            for lists in result:
                Result.objects.create(
                    store_name = lists['name'],
                    distance = 0,
                    price = lists['budget']['average'],
                    review = '0',
                    phone_number = '????-???-???',
                    opening_flg = lists['open'],
                    type_of_cuisine = lists['genre']['name']
                )

            #検索結果画面にリダイレクトする
            return redirect(to='/result_screen')
             
#現在地取得クラス
class GetLocation():

    def __init__(self):

        geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
        data = requests.get(geo_request_url).json() 

        self.latitude = data['latitude']
        self.longitude = data['longitude']        

#データベースにデータが存在しない場合に呼び出すデータエラークラス
class DataError(Exception):
    pass




#    import googlemaps

#         #APIキーを設定
#         client = googlemaps.Client(API_KEY)

#         #検索条件を指定
#         nearby_spots = client.places_nearby(
#         location=(34.972187, 138.388901), #現在地
#         radius='10000', #距離（メートル）
#         language='ja', #言語
#         keyword=search_word #キーワード
#         )
        
#         #DBに保存する
#         for lists in nearby_spots['results']:
#             Result.objects.create(
#             store_name = lists.get('name','不明'),
#             distance = 1,
#             price = lists.get('price_level',0),
#             review = lists.get('rating',0),
#             phone_number = 54-0000-000,
#             opening_flg = lists.get('opening_now',False),
#             type_of_cuisine = lists.get('types',False)
#             )
            
#         return redirect(to='/result_screen')


  





    
 
    
 