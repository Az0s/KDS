'''
Date: 2022-03-26 16:49:36
LastEditors: Azus
LastEditTime: 2022-09-08 17:06:04
FilePath: /KDS/backend/reverseProxy.py
'''
# backend/reverseProxy.py

from requests import get

# Simple reverse proxy for use with webpack-dev-server.
def proxyRequest(host, path):
    response = get(host + path)

    excluded_headers = [
        "content-encoding",
        "content-length",
        "transfer-encoding",
        "connection",
    ]
    headers = {
        name: value
        for name, value in response.raw.headers.items()
        if name.lower() not in excluded_headers
    }
    return (response.content, response.status_code, headers)