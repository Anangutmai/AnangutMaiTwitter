import requests

def getSection(proxy = None):
    session = requests.session()
    if proxy is not None:
        session.proxies = proxy
    return session
        

def Twitter_hashtag_function(hashtag, first, cursor = '', mode  = 0, proxy = None):
    session = getSection(proxy)

    access_token = 'AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
    get_token_header = {'authorization': f'Bearer {access_token}',
    'content-type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'x-csrf-token': 'fc22ac90c8ecd0781542ca01e4784874',
    'x-twitter-active-user': 'yes',
    'x-twitter-client-language': 'en',
    }
    
    get_token_url = 'https://api.twitter.com/1.1/guest/activate.json'
    
    try:
        res = requests.post(get_token_url, headers = get_token_header)
        guest_token = res.json()['guest_token']
    except Exception as err:
        return {'code':400,'error': "Can't get token", "message": str(err)}
    header = {'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'Bearer {access_token}',
        'origin': 'https://twitter.com',
                
        'cookie': 'personalization_id="v1_d9R0Ut3mXg43yLyYcYGyeA=="; guest_id=v1%3A159160237633318066; gt=1269898523991924736; ct0=fc22ac90c8ecd0781542ca01e4784874; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCAvz5JJyAToMY3NyZl9p%250AZCIlNWNkNjUzYTc3MDVhNjk1MDFlN2FmZGE5ZGExNjNjOTU6B2lkIiVlOWRh%250ANjYzOGIxODNjMzQwZTA1OWFkMmY1OWRlZTBkYw%253D%253D--d08ee4dfe07b7731d9f334bd9c9ea12d7013ea54; _ga=GA1.2.185405471.1591602378; _gid=GA',
        'referer': 'https://twitter.com/search?q=%23%E0%B8%A1%E0%B8%B2%E0%B8%A3%E0%B8%B5%E0%B8%8D%E0%B8%B2&src=trend_click',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
        'x-csrf-token': 'oTW8srKgVTLQ56CfhYMt6I7aW',
        'x-guest-token': f'{guest_token}',
        'x-twitter-active-user': 'yes',
        'x-twitter-client-language': 'en'
    }


    payload = {'q': f'#{hashtag}',
    'count': f'{first}',
    'query_source': 'trend_click',
    'tweet_mode':'extended',
    'cursor': f'scroll:"{cursor}"'}
    if mode == 1:
        payload['tweet_search_mode'] = 'live'

    URL = 'https://api.twitter.com/2/search/adaptive.json'
    
    res = session.get(URL, params = payload, headers = header)
    data = res.json()
    
    return data
