import streamlit as st
import pandas as pd
from tmdb_api import get_genres, search_movies, search_actor_id

st.set_page_config(page_title="TMDB Movie & TV Finder", layout="wide")

st.title("🎬 TMDB Movie & TV Show Finder")

media_type = st.radio("Select type", ["movie", "tv"], horizontal=True)

# Genre
genres = get_genres(media_type)
selected_genre = st.selectbox("Genre", ["Any"] + list(genres.keys()))
genre_id = genres.get(selected_genre) if selected_genre != "Any" else None

# Filters
min_rating = st.slider("Minimum IMDb Rating", 0.0, 10.0, 6.0, 0.1)
min_votes = st.number_input("Minimum Number of Votes", 0, 1000000, 1000)
max_results = st.slider("Maximum Results", 1, 100, 20)

# Actor input
actor_input = st.text_input("Search by Actor(s) (comma-separated)")
actors = [a.strip() for a in actor_input.split(",") if a.strip()]
actor_ids = [search_actor_id(a) for a in actors if search_actor_id(a)]

# Year range
st.markdown("📆 **Release Year Range (optional)**")
col1, col2 = st.columns(2)
with col1:
    min_year = st.number_input("From Year", min_value=1800, max_value=2100, value=2000)
with col2:
    max_year = st.number_input("To Year", min_value=1800, max_value=2100, value=2024)

# Language and Country
col3, col4 = st.columns(2)
with col3:
    lang_toggle = st.checkbox("Filter by Original Language?")
    language = st.text_input("Original Language Code (e.g. en, es)") if lang_toggle else None
with col4:
    country_toggle = st.checkbox("Filter by Country of Origin?")
    country = st.text_input("Country Code (e.g. US, FR)") if country_toggle else None

# Search button
if st.button("🔍 Search"):
    results = []
    for year in range(min_year, max_year + 1):
        partial_results = search_movies(
            media_type=media_type,
            genre_id=genre_id,
            min_rating=min_rating,
            min_votes=min_votes,
            max_results=max_results - len(results),
            actor_ids=actor_ids,
            year=year,
            language=language,
            country=country
        )
        results.extend(partial_results)
        if len(results) >= max_results:
            break

    if results:
        df = pd.DataFrame(results)
        st.success(f"Found {len(df)} results.")
        st.dataframe(df, use_container_width=True)
        st.download_button("⬇️ Download CSV", df.to_csv(index=False).encode("utf-8"), "results.csv", "text/csv")
    else:
        st.warning("No results found with those filters.")
