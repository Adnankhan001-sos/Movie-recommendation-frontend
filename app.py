"""
Main Streamlit application for Movie Recommendation System
Frontend that connects to FastAPI backend
"""
import streamlit as st
from services.api_client import api_client
from components.genre_selector import display_genre_selector
from utils.helpers import reset_app_state
from utils.constants import DEFAULT_RECOMMENDATION_COUNT

# Page configuration
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    text-align: center;
    padding: 2rem 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 15px;
    margin-bottom: 2rem;
    color: white;
}

.stButton > button {
    border-radius: 10px;
    border: none;
    transition: all 0.3s ease;
}
</style>
""", unsafe_allow_html=True)

def display_simple_movie_grid(movies):
    """Simple movie display"""
    if not movies:
        st.warning("No movies found.")
        return
    
    st.subheader(f"🍿 Found {len(movies)} movies")
    
    # Display 3 movies per row
    for i in range(0, len(movies), 3):
        cols = st.columns(3)
        for j, movie in enumerate(movies[i:i+3]):
            with cols[j]:
                st.markdown("🎬")  # Poster placeholder
                st.write(f"**{movie['title']}** ({movie['year']})")
                st.write(f"⭐ {movie['rating']}/10")
                st.write(f"Genre: {movie['genre']}")
                
                # Details button with unique key
                if st.button(f"See Details", key=f"btn_{movie['id']}_{i}_{j}"):
                    show_movie_details(movie['id'])
                st.write("---")

def show_movie_details(movie_id):
    """Show movie details in a simple way"""
    movie_details = api_client.get_movie_details(movie_id)
    if movie_details:
        st.info(f"""
        **🎬 {movie_details['title']} ({movie_details['year']})**
        
        **Rating:** ⭐ {movie_details['rating']}/10
        **Genre:** {movie_details['genre']}
        **Runtime:** {movie_details['runtime']} minutes
        
        **Plot:** {movie_details['description']}
        """)

def main():
    """Main application logic"""
    
    # App Header
    st.markdown("""
    <div class="main-header">
        <h1>🎬 Movie Recommendation System</h1>
        <p style="font-size: 1.2rem; margin: 0; opacity: 0.9;">
            Discover your next favorite movie
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Check backend health
    health_status = api_client.get_health()
    if health_status.get("status") != "healthy":
        st.error("⚠️ Backend API is not responding. Please make sure the FastAPI server is running.")
        return
    
    # Step 1: Genre Selection
    available_genres = api_client.get_genres()
    if not available_genres:
        st.error("Could not load genres.")
        return
    
    selected_genre = st.selectbox("🎭 Choose a genre:", [""] + available_genres)
    
    if not selected_genre:
        st.info("👆 Please select a genre to get movie recommendations!")
        return
    
    # Step 2: Count Selection
    count = st.selectbox("How many movies?", [3, 6, 9, 12], index=1)
    
    # Step 3: Get Recommendations Button
    if st.button("🎬 Get Recommendations", type="primary"):
        with st.spinner("Loading movies..."):
            movies = api_client.get_movie_recommendations(selected_genre, count)
            if movies:
                st.session_state.current_movies = movies
                st.session_state.current_genre = selected_genre
            else:
                st.error("No movies found!")
    
   # Step 4: Display Movies
    if st.session_state.get('current_movies'):
        st.success(f"🎊 Here are {len(st.session_state.current_movies)} {st.session_state.current_genre} movies:")
        display_simple_movie_grid(st.session_state.current_movies)
        
        # New recommendations button - FIXED VERSION
        if st.button("🔄 Get Different Movies", type="secondary", key="get_different"):
            # Don't use st.rerun() here - just update the session state
            with st.spinner("Finding new movies..."):
                movies = api_client.get_movie_recommendations(st.session_state.current_genre, count)
                if movies:
                    st.session_state.current_movies = movies
                    st.success("✅ Got new movies! Scroll up to see them.")
                else:
                    st.error("No new movies found!")

if __name__ == "__main__":
    main()
