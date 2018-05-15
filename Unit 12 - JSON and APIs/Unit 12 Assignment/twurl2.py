#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:07:17 2017

@author: shareshianl
"""

import oauth2
import hidden

def oauth_req(url, key, secret, http_method, post_body="", http_headers=None):
    secrets = hidden.oauth()
    consumer = oauth2.Consumer(key=secrets['consumer_key'], secret=secrets['consumer_secret'])
    token = oauth2.Token(key=secrets['token_key'],secret=secrets['token_secret'])
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content



