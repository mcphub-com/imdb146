import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/Glavier/api/imdb146'

mcp = FastMCP('imdb146')

@mcp.tool()
def find(query: Annotated[str, Field(description='Search query')]) -> dict: 
    '''Find (Search)'''
    url = 'https://imdb146.p.rapidapi.com/v1/find/'
    headers = {'x-rapidapi-host': 'imdb146.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def title_details(id: Annotated[str, Field(description='Title ID')]) -> dict: 
    '''Title Details'''
    url = 'https://imdb146.p.rapidapi.com/v1/title/'
    headers = {'x-rapidapi-host': 'imdb146.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def name_details(id: Annotated[str, Field(description='Name ID')]) -> dict: 
    '''Name Details'''
    url = 'https://imdb146.p.rapidapi.com/v1/name/'
    headers = {'x-rapidapi-host': 'imdb146.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def video_details(id: Annotated[str, Field(description='Video ID')]) -> dict: 
    '''Video Details'''
    url = 'https://imdb146.p.rapidapi.com/v1/video/'
    headers = {'x-rapidapi-host': 'imdb146.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_details(id: Annotated[str, Field(description='News ID')]) -> dict: 
    '''News Details'''
    url = 'https://imdb146.p.rapidapi.com/v1/news/'
    headers = {'x-rapidapi-host': 'imdb146.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
