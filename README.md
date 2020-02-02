# Text Preprocessing API

Text Preprocessing API memungkinkan anda melakukan Text Preprocessing tanpa melakukan code Preprocessing

# Fitur

  - Dinamis text preprocessing anda bisa memilih Parameters yang dibutuhkan

## Teknologi

Teknologi yang digunakan pada service ini adalah :

* [Django] - Python Framework
* [MySQL] - Database
* [NLTK] - Library platform untuk membangun program python dengan data bahasa manusia
* [pandas] - data analysis and manipulation tool

## Installation

Text Preprocessing API requires [Python] v3.6.x

langkah instalasi

1. clone repo :
```sh
$ git clone https://github.com/azizsembada/text-preprocessing-api.git
```
2. buka terminal pada repo program dan jalankan
 ```sh
$ Scripts\activate
```
3. Buat database MySQL dengan nama text_preprocessing_auth dan export file text_preprocessing_auth.sql yang ada di root directori
4. buka source code ke direktori src/textpreprocessing kemudian buka file settings.py dan cari code berikut
 ```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'text_preprocessing_auth',
        'USER': 'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
``` 
pastikan user, password, host dan port sesuai dengan server anda. Apabila anda ingin mengganti nama database setelah di save jangan lupa jalankan perintah 
 ```sh
$ python manage.py migrate  
```
4. kembali ke direktori src kemudian jalankan
 ```sh
$ python manage.py runserver  
```
jika proses berhasil akan tampil seperti ini pada terminal **Starting development server at http://127.0.0.1:8000/**

## Documentasi API
Untuk mengakses service ini silahkan ikuti dokumentasi berikut :
### HTTP Request
 ```sh
POST http://127.0.0.1:8000/api/ 
```
### Parameters
| Parameters | | Deskripsi |
| ------ | ------ | ------ |
| content | required | **content** adalah text yang akan di preprocessing |
| access_token | required | **access_token** adalah token yang digunakan agar dapat mengakses service |
| access_token_secret | required | **access_token_secret** adalah token yang digunakan agar dapat mengakses service |
| normalize_slang_word | optional | **normalize_slang_word** adalah fitur untuk menormalisasi kata slang|
| remove_sentence | optional | **remove_sentence** adalah fitur untuk menghapus kalimat|
| remove_url | optional | **remove_url** adalah fitur untuk menghapus URL|
| remove_digit | optional | **remove_digit** adalah fitur untuk menghapus digit|
| remove_non_ascii | optional | **remove_non_ascii** adalah fitur untuk menghapus karakter yang bukan ASCII|
| remove_html | optional | **remove_html** adalah fitur untuk menghapus code html dalam text|
| remove_mention | optional | **remove_html** adalah fitur untuk menghapus mention|
| remove_hashtag | optional | **remove_hashtag** adalah fitur untuk menghapus hashtag|
| remove_retweet | optional | **remove_retweet** adalah fitur untuk menghapus retweet|
| remove_punctuation | optional | **remove_punctuation** adalah fitur untuk menghapus tanda baca|
| remove_add_space | optional | **remove_add_space** adalah fitur untuk menghapus spasi berlebih|
| case_folding | optional | **case_folding ** adalah fitur untuk mungubah kata / kalimat menjadi huruf kecil atau huruf besar semua|
| remove_repeated_character | optional | **remove_repeated_character** adalah fitur untuk menghapus karakter yang sama dan berulang|
### Result
| Parameters | Deskripsi |
| ------ | ------ |
| code | **200** jika token valid **401** jika token tidak valid|
| title | Text Preprocessing Service|
| status | **success** jika text berhasil dipreprocessing **warning** jika token tidak valid|
| result | text berhasil dipreprocessing / tidak dipreprocessing|

### Example JSON data
 ```sh
{
    "content": "text yang akan dipreprocessing",
    "normalize_slang_word":"1",
    "remove_sentence":"1",
    "remove_url":"1",
    "remove_digit":"1",
    "remove_non_ascii":"1",
    "remove_html":"1",
    "remove_mention":"1",
    "remove_hashtag":"1",
    "remove_retweet":"1",
    "remove_punctuation":"1",
    "remove_add_space":"1",
    "case_folding":"uppercase",
    "remove_repeated_character":"1",
    "access_token": "token kamu",
    "access_token_secret": "token kamu",
}
``` 
### NOTE !
**1** untuk YA dan **2** untuk tidak

**Free Source code, Hell Yeah!**
please join to my circle [buruhkoding]

   [Django]: <https://www.django-rest-framework.org/r>
   [MySQL]: <https://www.mysql.com/>
   [NLTK]: <https://www.nltk.org/>
   [pandas]: <https://pandas.pydata.org/>
   [Python]: <python.org/downloads/release/python-3610/>
   [buruhkoding]: <https://www.linkedin.com/in/abdullah-aziz-sembada-29730088/>
