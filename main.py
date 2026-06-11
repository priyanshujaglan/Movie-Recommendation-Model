import streamlit as st
import pickle
import requests

API_KEY = '75a42dc73351b8a50ff1c712d36c4106'
def fetch_movie_details(movie_id):

    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return {
                "poster": None,
                "rating": "N/A",
                "release_date": "N/A"
            }

        data = response.json()

        poster_path = data.get("poster_path")

        poster_url = (
            f"https://image.tmdb.org/t/p/w500{poster_path}"
            if poster_path else None
        )

        return {
            "poster": poster_url,
            "rating": data.get("vote_average", "N/A"),
            "release_date": data.get("release_date", "N/A")
        }

    except Exception as e:
        print("TMDB Error:", e)

        return {
            "poster": None,
            "rating": "N/A",
            "release_date": "N/A"
        }

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="CineMatch AI",
    page_icon="🎬",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
movies = pickle.load(open('movies.pkl', 'rb'))




print(loaded.columns)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.big-title {
    font-size: 3rem;
    font-weight: bold;
    color: #FF4B4B;
}

.sub-title {
    font-size: 1.2rem;
    color: #A0A0A0;
    margin-bottom: 20px;
}

.footer {
    text-align: center;
    color: gray;
    padding-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("🎬 About Project")

    st.write("""
    This Movie Recommendation System uses
    **Content-Based Filtering** and
    **Cosine Similarity** to suggest movies
    similar to the one selected by the user.
    """)

    st.markdown("---")

    st.subheader("🛠 Tech Stack")

    st.write("""
    ✅ Python  
    ✅ Pandas  
    ✅ Scikit-Learn  
    ✅ Streamlit  
    ✅ Machine Learning
    """)

    st.markdown("---")

    st.subheader("👨‍💻 Developer")

    st.write("""
    **Priyanshu Jaglan**  
    B.Tech CSE (AI)
    """)

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movies_list:

        row = movies.iloc[i[0]]

        details = fetch_movie_details(row.movie_id)

        recommendations.append({
            "title": row.title,
            "poster": details["poster"],
            "rating": details["rating"],
            "release_date": details["release_date"],
            "cast": row['cast'][:2] if isinstance(row['cast'], list) else [row['cast']],
            "overview": row.overview
        })

    return recommendations

# ---------------- HEADER ----------------
st.markdown(
    """
    <div style='text-align: center; padding: 20px;'>
        <h1 style='font-size: 55px; color: #E50914; margin-bottom: 10px;'>
            🎬 Movie Recommendation System
        </h1>
        <p style='font-size: 22px; color: #A0A0A0;'>
            Discover your next favorite movie with AI-powered recommendations
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown("## 🌟 Popular Hollywood Stars")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.image("ChrisHemsworth-2019_r2.jpg", use_container_width=True)
    st.caption("Chris Hemsworth")

with col2:
    st.image("34340015906178016.jpg", use_container_width=True)
    st.caption("Ben Affleck")

with col3:
    st.image("1477812372632811.jpg", use_container_width=True)
    st.caption("Tom Cruise")

with col4:
    st.image("80361174596095581.jpg", use_container_width=True)
    st.caption("Henry Cavill")

with col5:
    st.image("HDNiceWallpapers_com.jpg", use_container_width=True)
    st.caption("Daniel Craig")

with col6:
    st.image("Find all latest high-resolution wallpapers of….jpg", use_container_width=True)
    st.caption("Tom Cruise")


st.markdown("### 🔥 Trending Genres")

genres = ["Action", "Adventure", "Sci-Fi", "Comedy", "Drama"]

cols = st.columns(len(genres))

for col, genre in zip(cols, genres):
    col.info(genre)

st.markdown("---")

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📽 Movies Available", len(movies))

with col2:
    st.metric("🤖 Recommendation Engine", "AI")

with col3:
    st.metric("⭐ Suggestions", "Top 5")

st.markdown("---")

st.markdown("### 🤖 How It Works")

st.write("""
This recommendation system uses Content-Based Filtering
and Cosine Similarity to recommend movies based on
genres, cast, crew, keywords, and metadata similarity.
""")

st.markdown("---")

# ---------------- MOVIE SELECTION ----------------
selected_movie_name = st.selectbox(
    "🎞 Select a movie",
    movies['title'].values
)

# ---------------- BUTTON ----------------
if st.button("🚀 Recommend Movies", use_container_width=True):

    recommendations = recommend(selected_movie_name)

    st.markdown("## 🍿 Recommended Movies For You")

    cols = st.columns(5)

    for col, movie in zip(cols, recommendations):

        with col:

            if movie["poster"]:
                st.image(movie["poster"])

            st.markdown(
                f"### {movie['title']}"
            )

            st.write(
                f"⭐ {movie['rating']}"
            )

            st.write(
                f"📅 {movie['release_date'][:4] if movie['release_date'] else 'N/A'}"
            )

            st.write(
                f"🎭 {', '.join(movie['cast'])}"
            )

            overview_text = movie['overview']

            if isinstance(overview_text, list):
                overview_text = " ".join(overview_text)

            st.caption(
                overview_text[:120] + "..."
                if overview_text
                else "No overview available."
            )

# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown(
    """
    <div class='footer'>
        Built with ❤️ using Streamlit | Machine Learning Project by Priyanshu Jaglan
    </div>
    """,
    unsafe_allow_html=True
)