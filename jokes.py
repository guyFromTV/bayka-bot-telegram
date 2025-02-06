import requests


JOKES_API_BASE_URL = "https://v2.jokeapi.dev/joke/Programming,Dark,Pun"


def get_joke(joke_type) -> dict:
    params = {
        "lang": "en",
        "blacklistFlags": "sexist",
    }
    if joke_type:
        params['type'] = joke_type
    response = requests.get(JOKES_API_BASE_URL, params=params)

    if response.status_code != 200:
        return
    json_data = response.json()
    if json_data.get('error'):
        return
    
    return json_data


def get_random_joke():
    json_data = get_joke('single')
    if not json_data:
        return 'Error'
    
    return json_data['joke']


def get_random_two_part_joke():
    json_data = get_joke('twopart')
    if not json_data:
        return 'Error'
    
    return json_data['setup'], json_data['delivery']
    

