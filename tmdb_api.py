import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"

def get_genres(media_type="movie"):
    url = f"{BASE_URL}/genre/{media_type}/list"
    params = {"api_key": API_KEY, "language": "en-US"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        genres = response.json()["genres"]
        return {genre["name"]: genre["id"] for genre in genres}
    return {}

def search_actor_id(name):
    url = f"{BASE_URL}/search/person"
    params = {"api_key": API_KEY, "query": name}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()["results"]
        return results[0]["id"] if results else None
    return None

def search_movies(media_type="movie", genre_id=None, min_rating=0, min_votes=0,
                  max_results=20, actor_ids=None, year=None,
                  language=None, country=None):
    results = []
    page = 1

    while len(results) < max_results:
        url = f"{BASE_URL}/discover/{media_type}"
        params = {
            "api_key": API_KEY,
            "sort_by": "vote_average.desc",
            "vote_average.gte": min_rating,
            "vote_count.gte": min_votes,
            "page": page,
            "language": "en-US"
        }
        if genre_id:
            params["with_genres"] = genre_id
        if actor_ids:
            params["with_cast"] = ",".join(map(str, actor_ids))
        if year:
            key = "first_air_date_year" if media_type == "tv" else "primary_release_year"
            params[key] = year
        if language:
            params["with_original_language"] = language
        if country:
            params["region"] = country

        response = requests.get(url, params=params)
        if response.status_code != 200:
            break

        data = response.json().get("results", [])
        for item in data:
            title = item.get("title") or item.get("name")
            date = item.get("release_date") or item.get("first_air_date")
            results.append({
                "Title": title,
                "Rating": item.get("vote_average"),
                "Votes": item.get("vote_count"),
                "Release Date": date,
                "Language": item.get("original_language"),
                "Overview": item.get("overview")
            })

            if len(results) >= max_results:
                break

        if page >= response.json().get("total_pages", 1):
            break

        page += 1

    return results