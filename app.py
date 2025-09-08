"""
Movie Recommendation System - Enhanced with Real TMDB Data and Posters
Frontend that connects to deployed TMDB-powered FastAPI backend
"""
import streamlit as st
from services.api_client import api_client
from components.movie_display import display_movie_grid_with_posters, show_enhanced_movie_details

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced CSS for professional movie app look
st.markdown("""
<style>
.main-header {
    text-align: center;
    padding: 3rem 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 20px;
    margin-bottom: 2rem;
    color: white;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.genre-card {
    background: linear-gradient(45deg, #667eea, #764ba2);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
    margin: 10px 0;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    cursor: pointer;
}

.genre-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.2);
}

.stButton > button {
    border-radius: 12px;
    border: none;
    transition: all 0.3s ease;
    font-weight: 600;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}

.movie-stats {
    background: #f8f9fa;
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

def main():
    # App Header with enhanced design
    st.markdown("""
    <div class="main-header">
        <h1 style="font-size: 3rem; margin-bottom: 10px; font-weight: 700;">🎬 CinemaScope</h1>
        <p style="font-size: 1.4rem; margin: 0; opacity: 0.9; font-weight: 300;">
            Discover Amazing Movies with Real Posters & Reviews
        </p>
        <p style="font-size: 1rem; margin-top: 10px; opacity: 0.7;">
            Powered by The Movie Database (TMDB)
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Backend connection status with better UX
    with st.spinner("🎬 Connecting to movie database..."):
        health_status = api_client.get_health()
    
    if health_status.get("status") != "healthy":
        st.error("⚠️ Movie database is starting up... Please wait 30-60 seconds and refresh.")
        st.info("🎬 Our backend is deployed on Render and may need a moment to wake up from sleep mode.")
        if st.button("🔄 Retry Connection", type="primary"):
            st.rerun()
        return
    
    st.success("✅ Connected to TMDB movie database! Ready to discover movies.")
    
    # Genre selection with enhanced UX
    st.markdown("### 🎭 What Kind of Movies Do You Love?")
    
    with st.spinner("Loading movie genres..."):
        available_genres = api_client.get_genres()
    
    if not available_genres:
        st.error("Could not load genres. Please refresh the page.")
        return
    
    # Enhanced genre selection with description
    selected_genre = st.selectbox(
        "Choose your favorite genre:",
        [""] + available_genres,
        help="Select a genre to discover popular movies in that category!"
    )
    
    if not selected_genre:
        # Show genre preview cards when no genre selected
        st.info("👆 Select a genre above to start your movie discovery journey!")
        
        # Display genre options in a grid
        st.markdown("### 🎬 Available Genres")
        genre_cols = st.columns(4)
        for i, genre in enumerate(available_genres[:12]):  # Show first 12 genres
            with genre_cols[i % 4]:
                st.markdown(f"""
                <div class="genre-card">
                    <div style="font-size: 2rem; margin-bottom: 8px;">
                        {['🎬', '🗺️', '🎨', '😂', '🔫', '📹', '🎭', '👨‍👩‍👧‍👦', '🧙', '📜', '👻', '🎵'][i % 12]}
                    </div>
                    <div style="font-weight: bold;">{genre}</div>
                </div>
                """, unsafe_allow_html=True)
        return
    
    # Movie count and search options
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"### 🍿 Exploring {selected_genre} Movies")
    with col2:
        count = st.selectbox("Movies to show:", [3, 6, 9, 12, 15], index=1)
    
    # Main action button
    if st.button("🎬 Discover Movies", type="primary", use_container_width=True):
        with st.spinner(f"🔍 Searching for amazing {selected_genre} movies..."):
            movies = api_client.get_movie_recommendations(selected_genre, count)
            if movies:
                st.session_state.current_movies = movies
                st.session_state.current_genre = selected_genre
                st.session_state.current_count = count
                st.balloons()
                st.success(f"🎊 Found {len(movies)} fantastic {selected_genre} movies!")
            else:
                st.error("No movies found! Try a different genre or refresh the page.")
    
    # Display movies if available
    if st.session_state.get('current_movies'):
        # Movie display section
        st.markdown("---")
        selected_movie_id = display_movie_grid_with_posters(st.session_state.current_movies)
        
        # Handle movie details display
        if st.session_state.get('selected_movie_id') or selected_movie_id:
            movie_id = st.session_state.get('selected_movie_id') or selected_movie_id
            st.session_state.selected_movie_id = movie_id
            
            st.markdown("---")
            st.markdown("## 🎬 Movie Details")
            
            with st.spinner("Loading detailed movie information..."):
                movie_details = api_client.get_movie_details(movie_id)
            
            if movie_details:
                show_enhanced_movie_details(movie_details)
                
                # Close details button
                if st.button("❌ Close Details", type="secondary"):
                    if 'selected_movie_id' in st.session_state:
                        del st.session_state.selected_movie_id
                    st.rerun()
            else:
                st.error("Could not load movie details. Please try again.")
        
        # Action buttons
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🎲 Get Different Movies", type="secondary", use_container_width=True):
                # Clear selected movie details
                if 'selected_movie_id' in st.session_state:
                    del st.session_state.selected_movie_id
                
                with st.spinner("Finding new movies..."):
                    movies = api_client.get_movie_recommendations(
                        st.session_state.current_genre, 
                        st.session_state.get('current_count', 6)
                    )
                    if movies:
                        st.session_state.current_movies = movies
                        st.success("🎊 Discovered new movies! Check them out above.")
                    else:
                        st.error("Could not find new movies. Please try again.")
        
        with col2:
            if st.button("🔄 Try Different Genre", type="secondary", use_container_width=True):
                # Clear all session state to restart
                keys_to_clear = ['current_movies', 'current_genre', 'current_count', 'selected_movie_id']
                for key in keys_to_clear:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()
        
        # App statistics
        st.markdown("---")
        st.markdown(f"""
        <div style="
            text-align: center; 
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
        ">
            <h4 style="color: #2c3e50; margin-bottom: 15px;">📊 Your Movie Discovery Session</h4>
            <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
                <div style="margin: 10px;">
                    <div style="font-size: 2rem; color: #3498db;">🎭</div>
                    <div style="font-weight: bold; color: #2c3e50;">Genre</div>
                    <div style="color: #7f8c8d;">{st.session_state.current_genre}</div>
                </div>
                <div style="margin: 10px;">
                    <div style="font-size: 2rem; color: #e74c3c;">🎬</div>
                    <div style="font-weight: bold; color: #2c3e50;">Movies Found</div>
                    <div style="color: #7f8c8d;">{len(st.session_state.current_movies)}</div>
                </div>
                <div style="margin: 10px;">
                    <div style="font-size: 2rem; color: #f39c12;">⭐</div>
                    <div style="font-weight: bold; color: #2c3e50;">Avg Rating</div>
                    <div style="color: #7f8c8d;">{round(sum(m['rating'] for m in st.session_state.current_movies) / len(st.session_state.current_movies), 1)}/10</div>
                </div>
                <div style="margin: 10px;">
                    <div style="font-size: 2rem; color: #9b59b6;">🎪</div>
                    <div style="font-weight: bold; color: #2c3e50;">Data Source</div>
                    <div style="color: #7f8c8d;">TMDB API</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #7f8c8d; padding: 20px;">
        <p><strong>🎬 CinemaScope</strong> - Your Personal Movie Discovery Platform</p>
        <p>Powered by <a href="https://www.themoviedb.org/" target="_blank">The Movie Database (TMDB)</a></p>
        <p>Built with ❤️ using FastAPI + Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
