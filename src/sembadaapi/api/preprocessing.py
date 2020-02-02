import json
from rest_framework import generics,mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import SembadaapiSerializer
from sembadaapi.models import Sembadaapi
from django.core import serializers

import re
import string
import unicodedata
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import pandas as pd
import os

def is_json(json_data):
    try:
        real_json   = json.loads(json_data)
        is_valid    = True
    except ValueError:
        is_valid = False
    return is_valid

class PreprocessingAPIView(APIView):
    permission_classes      = []
    authentication_classes  = []

    serializer_class = SembadaapiSerializer

    def post(self, request, *args, **kwargs):
        data = {}
        post_data = json.loads(request.body)
        obj = Sembadaapi.objects.filter(access_token__exact=post_data["access_token"])&Sembadaapi.objects.filter(access_token_secret__exact=post_data["access_token_secret"])
        str = post_data["content"]
        if obj:
            # def remove_stopword
            if post_data["remove_stopword"]=="1":
                stop_words = set(stopwords.words('stopwordID.csv'))
                word_tokens = word_tokenize(str)
                filtered_sentence = [w for w in word_tokens if not w in stop_words]
                str = ' '.join(filtered_sentence)

            # def normalize_slang_word
            if post_data["normalize_slang_word"]=="1":
                text_list = str.split(' ')
                slang_words_raw = pd.read_csv('../slang_word_list.csv', sep=',', header=None)
                slang_word_dict = {}

                for item in slang_words_raw.values:
                    slang_word_dict[item[0]] = item[1]

                    for index in range(len(text_list)):
                        if text_list[index] in slang_word_dict.keys():
                            text_list[index] = slang_word_dict[text_list[index]]

                str = ' '.join(text_list)
            # remove_sentence
            if post_data["remove_sentence"]=="1":
                word = str.split()
                wordCount = len(word)
                if(wordCount <= 1):
                    str = ''
            # remove_url
            if post_data["remove_url"]=="1":
                str = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', str)

            # remove_digit
            if post_data["remove_digit"]=="1":
                str = re.sub(r'[^a-z ]*([.0-9])*\d', '', str)

            # remove_non_ascii
            if post_data["remove_non_ascii"]=="1":
                str = unicodedata.normalize('NFKD', str).encode('ascii', 'ignore').decode('utf-8', 'ignore')

            # remove_twitter_char 
            # html
            if post_data["remove_html"]=="1":
                str = re.sub(r'<[^>]+>', ' ', str) 
            # mention
            if post_data["remove_mention"]=="1":
                str = re.sub(r'(?:@[\w_]+)', ' ', str)
            # hashtag
            if post_data["remove_hashtag"]=="1":
                str = re.sub(r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", " ", str)
            # RT/cc
            if post_data["remove_retweet"]=="1":
                str = str = re.sub('RT', '', str)

            # def remove_punctuation
            if post_data["remove_punctuation"]=="1":
                str = re.sub(r'[^\s\w]', ' ', str)

            # def remove_add_space
            if post_data["remove_add_space"]=="1":
                str = re.sub('[\s]+', ' ', str)

            # def casefolding 
            if post_data["case_folding"]=='uppercase':
                str = str.upper()
            else:
                str = str.lower()   

            # def remove_repeated_character
            if post_data["remove_repeated_character"]=="1":
                str = re.sub(r'(.)\1{2,}', r'\1', str)
            
            # send JSON 
            data['code'] = 200
            data['title'] = 'Text Preprocessing Service'
            data['status'] = 'success'
            data['text'] = 'Data Berhasil DiPreprocessing'
            data['result'] = str

            return Response(data)
        else:
            data['code'] = 401
            data['title'] = 'Text Preprocessing Service'
            data['text'] = 'Token akses tidak valid'
            data['status'] = 'warning'
            data['result'] = str

            return Response(data)