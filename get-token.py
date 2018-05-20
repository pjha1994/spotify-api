#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 23:41:11 2018

@author: Abhishek Jha
"""

import credentials
import requests
import base64
def get_spotify_access_token():
    client_credentials = credentials.cred['client_id'] + ':' + credentials.cred['client_secret']
    encoded = base64.b64encode(bytes(client_credentials,'utf-8'))
    encoded = str(encoded.decode('utf-8'))
    
    #print(encoded)
    
    url = "https://accounts.spotify.com/api/token"
    
    #body
    payload = "grant_type=client_credentials"
    
    #headers
    headers = {
            'Authorization': "Basic "+ encoded,
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }
    
    response = requests.request("POST", url, data=payload, headers=headers)
    
    print(response.text)

get_spotify_access_token()