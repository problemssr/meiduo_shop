from django.test import TestCase

# Create your tests here.
from urllib.request import urlopen

response = urlopen(
    'http://utf8.api.smschinese.cn/?Uid=YYTAAA&Key=2fb832d94687b0505392&smsMob=17396556501&smsText=验证码：您好今天16.30坐姿不标准')
print(response.read())
