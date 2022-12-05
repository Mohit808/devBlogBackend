# import requests
# import pandas as pd
# from pyfcm import FCMNotification
# import datetime
# from time import sleep


# print("running")


# push_service =FCMNotification(api_key="AAAAM32oE1s:APA91bFmnK3Hc3IpT9rWea1U-6spzFcXhXsLaVnIukDIS7iGmmTVObQEkwofuTsDUZc8577Jq9HWPeJ0S-YK-ZKCqbJYPZkJYmcDbQgbLkUR6m-MrjWZelBgQ_5T2baJA7_DjU_KXp7x")
# def send_message(data,df,querystring):
#     # registration_id = ""
#     message_title = f"{querystring['Indices']} {df.head(1)['lastPrice'].values[0]}"
#     # message_title="wertyu"
#     message_body = {
#         "data":data
#     }

#     push_service.notify_topic_subscribers(topic_name="T88WQM66syMtFHzzqjdNZEa8O2G3",message_title=message_title,message_body=message_body,data_message=message_body)
#     # result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

# dct={
#     "pivot":43152,
#     "first_reg":43423,
#     "second_reg":43600,
#     "first_support":42974,
#     "second_support":42703
# }
# dct_reached={
#     "pivot":False,
#     "first_reg":False,
#     "second_reg":False,
#     "first_support":False,
#     "second_support":False
# }


# def call_method():

#     url = "https://latest-stock-price.p.rapidapi.com/price"
#     querystring = {"Indices":"NIFTY BANK"}

#     headers = {
#         "X-RapidAPI-Key": "aa2d2b080amshefda4a4cc9da0dcp16eccejsna3bb5e58b96c",
#         "X-RapidAPI-Host": "latest-stock-price.p.rapidapi.com"
#     }

#     while True:
#         response = requests.request("GET", url, headers=headers, params=querystring)

#         df=pd.DataFrame(response.json())
#         df.head(1)
#         if not df.head(1).empty:
#             print(df.head(1)['lastPrice'])
#             if int(df.head(1)['lastPrice']) > dct['pivot']-10 and int(df.head(1)['lastPrice'])< dct['pivot']+10:
#                 print("Hai")
#                 if dct_reached['pivot']==False:
#                     dct_reached['pivot']=True
#                     send_message({"pivot":True},df,querystring)

#             if int(df.head(1)['lastPrice']) > dct['first_reg']-10 and int(df.head(1)['lastPrice'])< dct['first_reg']+10:
#                 print("Hai")
#                 if dct_reached['first_reg']==False:
#                     dct_reached['first_reg']=True
#                     send_message({"first_reg":True},df,querystring)

#             if int(df.head(1)['lastPrice']) > dct['second_reg']-10 and int(df.head(1)['lastPrice'])< dct['second_reg']+10:
#                 print("Hai")
#                 if dct_reached['second_reg']==False:
#                     dct_reached['second_reg']=True
#                     send_message({"second_reg":True},df,querystring)

#             if int(df.head(1)['lastPrice']) > dct['first_support']-10 and int(df.head(1)['lastPrice'])< dct['first_support']+10:
#                 print("Hai")
#                 if dct_reached['first_support']==False:
#                     dct_reached['first_support']=True
#                     send_message({"first_support":True},df,querystring)

#             if int(df.head(1)['lastPrice']) > dct['second_support']-10 and int(df.head(1)['lastPrice'])< dct['second_support']+10:
#                 print("Hai")
#                 if dct_reached['second_support']==False:
#                     dct_reached['second_support']=True
#                     send_message({"second_support":True},df,querystring)

#         dt=datetime.datetime.now()
#         if dt.hour >= 15  and dt.minute == 30:
#             return False

#         sleep(300)


# call_method()