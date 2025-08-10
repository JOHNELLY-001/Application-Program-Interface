# import requests


# def get_romantic_movies_2024():
#     url = f'{BASE_URL}/discover/movie'
#     params = {
#         'api_key': API_KEY,
#         'with_genres': '10749',  # Genre ID for Romance
#         'primary_release_year': 2024,
#         'sort_by': 'popularity.desc',
#         'language': 'en-US',
#         'page': 1
#     }

#     response = requests.get(url, params=params)
#     data = response.json()

#     for movie in data.get('results', []):
#         print(f"{movie['title']} ({movie['release_date']}) - Rating: {movie['vote_average']}")

# get_romantic_movies_2024()

# def get_genres():
#     url  = f'{BASE_URL}/genre/movie/list'
#     params = {'api_key': API_KEY,
#               'language':'en-US'}
#     response = requests.get(url, params=params)
#     genres = response.json().get('genres',[])

#     for genre in genres:
#         print(f"{genre['name']}:{genre['id']}")

# get_genres()


import requests
import re

API_KEY = '113e3f0f19a6139a7ddbf3995ba366c7'  # Add your TMDB API key here
BASE_URL = 'https://api.themoviedb.org/3'

# Genre alias map for fuzzy matching
GENRE_ALIASES = {
    'romantic': 'romance',
    'sci fi': 'science fiction',
    'scifi': 'science fiction',
    'sci-fi': 'science fiction',
    'action-packed': 'action',
    'horror film': 'horror',
    'funny': 'comedy',
    'comic': 'comedy',
    'animated': 'animation',
    'adventure film': 'adventure',
    'war': 'war',
    'drama film': 'drama'
}

def get_genre_id():
    url = f"{BASE_URL}/genre/movie/list"
    params = {'api_key': API_KEY, 'language': 'en-US'}
    response = requests.get(url, params=params)
    genres = response.json().get('genres', [])
    return {genre['name'].lower(): genre['id'] for genre in genres}

def normalize_genres(message, genre_map):
    message = message.lower()
    found_genres = []
    for user_term in genre_map.keys() | GENRE_ALIASES.keys():
        if user_term in message:
            normalized = GENRE_ALIASES.get(user_term, user_term)
            if normalized in genre_map and normalized not in found_genres:
                found_genres.append(normalized)
    return found_genres

def extract_intent_and_entities(message, genre_map):
    message = message.lower()
    # Detect description intent
    if any(phrase in message for phrase in ['what is', 'about', 'description of', 'tell me about']):
        intent = 'get_description'
    else:
        intent = 'discover_movie'

    # Extract year
    year_match = re.search(r'\b(19|20)\d{2}\b', message)
    year = int(year_match.group()) if year_match else None

    # Extract genres using alias-aware logic
    genres = normalize_genres(message, genre_map)

    # Extract possible movie title
    title_match = re.search(r'about\s(.+)', message)
    title = title_match.group(1).strip() if title_match else None

    return {
        'intent': intent,
        'genre': genres,
        'year': year,
        'title': title
    }

def get_movie_description(title):
    search_url = f"{BASE_URL}/search/movie"
    params = {
        'api_key': API_KEY,
        'query': title,
        'language': 'en-US'
    }
    response = requests.get(search_url, params=params)
    results = response.json().get('results', [])
    if not results:
        return f"Sorry, I couldn't find any movie titled '{title}'."

    top_result = results[0]
    return f"**{top_result['title']}** ({top_result['release_date'][:4]}):\n{top_result.get('overview', 'No description available')}"

def get_movie_details_and_trailer(movie_id):
    details_url = f"{BASE_URL}/movie/{movie_id}"
    videos_url = f"{BASE_URL}/movie/{movie_id}/videos"
    params = {'api_key': API_KEY, 'language': 'en-US'}

    details_resp = requests.get(details_url, params=params).json()
    video_resp = requests.get(videos_url, params=params).json()

    trailer_url = None
    for video in video_resp.get('results', []):
        if video['site'].lower() == 'youtube' and video['type'].lower() == 'trailer':
            trailer_url = f"https://www.youtube.com/watch?v={video['key']}"
            break

    return {
        'overview': details_resp.get('overview', 'No overview available'),
        'trailer': trailer_url
    }

def discover_movies(genres=[], year=None):
    genre_map = get_genre_id()
    genre_ids = ','.join(str(genre_map[g]) for g in genres if g in genre_map)

    url = f"{BASE_URL}/discover/movie"
    params = {
        'api_key': API_KEY,
        'language': 'en-US',
        'with_genres': genre_ids,
        'sort_by': 'popularity.desc',
        'page': 1
    }
    if year:
        params['primary_release_year'] = year

    response = requests.get(url, params=params)
    results = response.json().get('results', [])

    return [(m['id'], m['title'], m.get('release_date', 'N/A')) for m in results]

def movie_reply(user_message):
    genre_map = get_genre_id()
    parsed = extract_intent_and_entities(user_message, genre_map)

    if parsed['intent'] == 'get_description' and parsed['title']:
        return get_movie_description(parsed['title'])

    movies = discover_movies(parsed['genre'], parsed['year'])

    if not movies:
        return "Sorry, I couldn't find matching movies."

    reply = "Here are some movies you might like:\n\n"
    for movie_id, title, release in movies[:3]:
        details = get_movie_details_and_trailer(movie_id)
        reply += f"**{title}** ({release[:4]})\n"
        reply += f"{details['overview']}\n"
        if details['trailer']:
            reply += f"Trailer: {details['trailer']}\n"
        reply += "\n"

    return reply
