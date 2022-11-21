#!/usr/bin/env python3
"""
created: 2022-11-21
@author: seraph1001100
project: Ocean State Job Lot
"""

import datetime
import os.path
import re
import csv
import requests

PATH = os.path.join(os.getcwd(), 'data')
DATE_STAMP = f"{datetime.datetime.now().date().strftime('%Y-%m-%d')}"
TIME_STAMP = f"{datetime.datetime.now().time().strftime('%H:%M:%S')}"


def get_store_location_json():
    url = "https://www.oceanstatejoblot.com/ccstoreui/v1/locations"

    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'X-CCProfileType': 'storefrontUI',
        'X-CCPriceListGroup': 'defaultPriceGroup',
        'X-CCViewport': 'lg',
        'x-ccsite': 'boss_en_us',
        'X-CC-MeteringMode': 'CC-NonMetered',
        'X-CCVisitorId': '135Bp1_v6Wbn35QHJjBShgaxBOHZsXCcod1Fs0TrjCLFEvk9649',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://www.oceanstatejoblot.com/health-essentials/category/Health',
        'Cookie': 'ccstoreroute=4a19b21d9575c965affb768483937f5a; JSESSIONID=gfuXT5EBYXXxvTVBimYg_zYw4CzuGjL9kxSAfOeBs8ZgFsUl4RAP!-1910259826; ak_bmsc=408AB30183AE6FF34B37885E5B79123C~000000000000000000000000000000~YAAQNZQZuGuAt4OEAQAAF5FPlxEvPnqOrIgL9oMHnDznwM3YOfhFMdHtix2VT0EwOBnmvFBgJAQ5GfR6s0hMX3I4Nwj3VAhO+vklEa6AU27dXOanygwEkIjrRyG65p2Q0TQorsr2tUb/6KqjMyXxeNlSG761fFtKTJ1ElS6VThqNHKpA7aW8/tYweMD7zofNE/EHQRQfHd0E3ujTTvVlHQvSR4xprGkj3OwlR7tsHi8P5AvydsW486tdCvwpiSYf5BPYEvtaLAX7rbivd8pHsK1tU5lQBBXhwtGVwIkQNw7QsJkZjl++kWLCPZiO0FwY4DDLdiJ0Bkp5J1grX+Hl8xWlAtuJfYcDRIYTpUaX/JSfHfM1dD9AsIkqu+NQWzYlmG7C8IBN0EW4/lb4HxEc3N31cUJ/; _gcl_au=1.1.28010628.1668985888; _ga_CFSN9Q6R2X=GS1.1.1668985887.1.1.1668986063.0.0.0; _ga=GA1.1.149863111.1668985888; dtm_token_sc=AQEGE32sckjPbwF2ROO1AQEBAQA; dtm_token=AQEGE32sckjPbwF2ROO1AQEBAQA; BCSessionID=6f61a10e-56bf-4dcb-9d9e-b0f527fd9a06; xda1550007c1PRD_boss_en_us=135Bp1_v6Wbn35QHJjBShgaxBOHZsXCcod1Fs0TrjCLFEvk9649%3A1668985888271%3A1668985888271%3A1668985888271%3A1%3A1; xva1550007c1PRD_boss_en_us=238bb7a5%3A184971a89bc%3A-2a5-4094299398; atgRecVisitorId=135Bp1_v6Wbn35QHJjBShgaxBOHZsXCcod1Fs0TrjCLFEvk9649; _gid=GA1.2.1472035228.1668985890; _hjSessionUser_2770891=eyJpZCI6ImUwOTRiODA4LTc5NGUtNTE4MC1hNGE3LTFmMTk4ZTAzYTc0NiIsImNyZWF0ZWQiOjE2Njg5ODU4OTAwMTAsImV4aXN0aW5nIjp0cnVlfQ==; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_2770891=eyJpZCI6ImFjYmIyOTM5LTZiMDUtNDRmNS1hYTA4LTIxNjBmMWJlOTk0YSIsImNyZWF0ZWQiOjE2Njg5ODU4OTAwMTQsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _gat_gtag_UA_20664924_1=1; occsRecVisitorId=%22135Bp1_v6Wbn35QHJjBShgaxBOHZsXCcod1Fs0TrjCLFEvk9649%22; occsRecSessionId=%22151518994512042045140199451214004549529556485648%22',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'trailers'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def parse_store_locations():
    store_location_json = get_store_location_json()['items']
    headers = ['DateStamp','TimeStamp', 'StoreName', 'Address1', 'Address2', 'City', 'State', 'ZipCode', 'Phone']
    records = []

    for store in store_location_json:
        storeName = store['name']
        address1 = store['address2']
        address2 = store['address1']
        city = store['city']
        state = store['stateAddress']
        zipCode = store['postalCode']
        phone = store['phoneNumber']
        record = (DATE_STAMP,TIME_STAMP, storeName, address1, address2, city, state, zipCode, phone)
        records.append(record)
    return headers, records


def get_product_json():
    url = "https://www.oceanstatejoblot.com/ccstoreui/v1/products?"

    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'X-CCProfileType': 'storefrontUI',
        'X-CCPriceListGroup': 'defaultPriceGroup',
        'X-CCViewport': 'md',
        'x-ccsite': 'boss_en_us',
        'X-CC-MeteringMode': 'CC-NonMetered',
        'X-CCVisitId': '238bb7a5:184971a89bc:-2a5-4094299398',
        'X-CCVisitorId': '135Bp1_v6Wbn35QHJjBShgaxBOHZsXCcod1Fs0TrjCLFEvk9649',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://www.oceanstatejoblot.com/winter-hats-and-gloves/category/winter-hats-and-gloves',
        'Cookie': 'ccstoreroute=4a19b21d9575c965affb768483937f5a; JSESSIONID=L-WXqehFEKmfvMDYdldkdK_YSfP3ZSuOM91ZsXtqLE1SfuFTC9s3!-1910259826; ak_bmsc=408AB30183AE6FF34B37885E5B79123C~000000000000000000000000000000~YAAQNZQZuGuAt4OEAQAAF5FPlxEvPnqOrIgL9oMHnDznwM3YOfhFMdHtix2VT0EwOBnmvFBgJAQ5GfR6s0hMX3I4Nwj3VAhO+vklEa6AU27dXOanygwEkIjrRyG65p2Q0TQorsr2tUb/6KqjMyXxeNlSG761fFtKTJ1ElS6VThqNHKpA7aW8/tYweMD7zofNE/EHQRQfHd0E3ujTTvVlHQvSR4xprGkj3OwlR7tsHi8P5AvydsW486tdCvwpiSYf5BPYEvtaLAX7rbivd8pHsK1tU5lQBBXhwtGVwIkQNw7QsJkZjl++kWLCPZiO0FwY4DDLdiJ0Bkp5J1grX+Hl8xWlAtuJfYcDRIYTpUaX/JSfHfM1dD9AsIkqu+NQWzYlmG7C8IBN0EW4/lb4HxEc3N31cUJ/; _gcl_au=1.1.28010628.1668985888; _ga_CFSN9Q6R2X=GS1.1.1668989913.2.1.1668991808.0.0.0; _ga=GA1.2.149863111.1668985888; dtm_token_sc=AQEGE32sckjPbwF2ROO1AQEBAQA; dtm_token=AQEGE32sckjPbwF2ROO1AQEBAQA; BCSessionID=6f61a10e-56bf-4dcb-9d9e-b0f527fd9a06; xda1550007c1PRD_boss_en_us=135Bp1_v6Wbn35QHJjBShgaxBOHZsXCcod1Fs0TrjCLFEvk9649%3A1668985888271%3A1668985888271%3A1668985888271%3A1%3A1; xva1550007c1PRD_boss_en_us=238bb7a5%3A184971a89bc%3A-2a5-4094299398; atgRecVisitorId=135Bp1_v6Wbn35QHJjBShgaxBOHZsXCcod1Fs0TrjCLFEvk9649; _gid=GA1.2.1472035228.1668985890; _hjSessionUser_2770891=eyJpZCI6ImUwOTRiODA4LTc5NGUtNTE4MC1hNGE3LTFmMTk4ZTAzYTc0NiIsImNyZWF0ZWQiOjE2Njg5ODU4OTAwMTAsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample=0; _hjSession_2770891=eyJpZCI6ImI1M2VhZmZjLWE2NGUtNGI4NC04MDMxLTliNjlkNTM3ZjlmNiIsImNyZWF0ZWQiOjE2Njg5ODk5MTUyMDIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _dd_s=rum=0&expire=1668992220463; flipp-merchant-id=3056; flipp-id=8312a0c940a5dbdb810b36109923f00d; flipp-gid=16e7fcc111fc292cb8b7a082d7329276; flipp-sid=4f7e884026bc4b4729e3bb0ca56bb7cc; _gat_gtag_UA_20664924_1=1; occsRecVisitorId=%22135Bp1_v6Wbn35QHJjBShgaxBOHZsXCcod1Fs0TrjCLFEvk9649%22; occsRecSessionId=%22151518994512042045140199451214004549529556485648%22; JSESSIONID=aiiXv4hDmcYT7i77U1SqznvWIrwXLMUM1S9QSKZjNfQXoOJH5l5a!-1910259826',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'trailers'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()


def parse_products():
    headers = ['DateStamp','TimeStamp', 'Name', 'Category', 'Price', 'Description', 'SoldOut']
    product_json = get_product_json()['items']
    records = []
    for item in product_json:
        name = item['primaryImageAltText']
        category = item['parentCategory']['repositoryId']
        price = item['listPrices']['defaultPriceGroup']
        description = remove_html_tags(item['longDescription'])
        sold_out = item['soldOut']
        record = (DATE_STAMP,TIME_STAMP, category, name, description, price,sold_out)
        records.append(record)
    return headers, records


def remove_html_tags(text):
    """Remove html tags from a string"""
    pattern = re.compile('<.*?>')
    return ', '.join(re.sub(pattern, ' ', text).strip().split()[2:])


def save_to_csv(record_data, filename):
    headers, record = record_data
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    with open(os.path.join(PATH, filename), 'w', newline='', encoding='utf8') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(headers)
        writer.writerows(record)
