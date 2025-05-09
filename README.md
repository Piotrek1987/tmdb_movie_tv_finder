# 🎬 TMDB Movie & TV Finder

A user-friendly Streamlit web app that lets you discover movies and TV shows using [The Movie Database (TMDB)](https://www.themoviedb.org/) API.  
Filter by genre, rating, number of votes, release year, language, country, and even specific actors — all in one place!

---

## 🚀 Features

- Search for **movies or TV shows**
- Filter by:
  - Genre
  - Minimum rating
  - Minimum number of votes
  - Release year
  - Original language
  - Country of origin
  - One or more actors
- View results in a table
- **Download results as CSV**

---

## 🖼 Preview

<img src="preview.png" alt="App Preview" width="800"/>

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your `.env` file:**

   Create a `.env` file in the project root and add your TMDB API key:

   ```env
   TMDB_API_KEY=your_api_key_here
   ```

   You can get a free API key from [TMDB API](https://developer.themoviedb.org/).

---

## ▶️ Run the app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
tmdb_movie_tv_finder/
├── app.py               # Streamlit frontend
├── tmdb_api.py          # API interaction logic
├── .env                 # Contains your API key (DO NOT COMMIT!)
├── requirements.txt     # Project dependencies
└── README.md            # You are here :)
```

---

## 🛡 Notes

- Be sure to exclude the `.env` file from version control. It's already listed in `.gitignore`.
- The TMDB API has rate limits — keep usage reasonable to avoid blocking.

---

## 📄 License

This project is licensed under the MIT License.  
Feel free to fork and modify it to your needs.

---

## 🙌 Acknowledgements

- [TMDB](https://www.themoviedb.org/) for the awesome API
- [Streamlit](https://streamlit.io/) for making Python apps beautiful and fast

---

⭐ If you like it, consider starring the repo!