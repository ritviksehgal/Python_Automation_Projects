import json
import requests
import time
import pandas as pd
from datetime import datetime


current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d")

file_loc = f"<file_path>"
df = pd.read_excel(file_loc, index_col=None, usecols= 'A, B', header = None)
df = df.head(220)



api_key = "<API_key>"
base_url = "https://www.virustotal.com/api/v3/files/"
headers = {"accept": "application/json", 'X-Apikey': api_key}


for MD5_hash in df[1].to_list():
    headers = {"accept": "application/json", 'X-Apikey': api_key}
    if not pd.isna(MD5_hash):
        url = base_url + MD5_hash
        try:
            response = requests.get(url, headers=headers)
            response_json = json.loads(response.content)

            if response_json['data']['attributes']['last_analysis_stats']['malicious'] >=2:
                with open ('vt_results.txt', 'a') as vt:
                    vt.write(MD5_hash) and vt.write('-\tMalicious\n')


            if response_json['data']['attributes']['last_analysis_stats']['malicious'] <=1:
                with open ('vt_results.txt', 'a') as vt:
                    vt.write(MD5_hash) and vt.write(' -\tNot Malicious\n')
        except:
            with open ('vt_results.txt', 'a') as vt:
               vt.write(MD5_hash) and vt.write('-\tSecure score not found\n')
            time.sleep(20)
            continue
