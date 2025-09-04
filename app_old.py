"""
Main Streamlit application for Movie Recommendation System
Frontend that connects to FastAPI backend
"""
import streamlit as st
import requests
from services.api_client import api_client
from components.genre_selector import display_genre_selector
from components.movie_grid import display_movie_grid
from components.movie_details import handle_movie_details
from utils.helpers import reset_app_state
from utils.constants import DEFAULT_RECOMMENDATION_COUNT, MAX_RECOMMENDATION_COUNT

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

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

div[data-testid="column"] {
    padding: 0 10px;
}
</style>
""", unsafe_allow_html=True)

def main():
    """Main application logic"""
    
    # App Header
    st.markdown("""
    <div class="main-header">
        <h1>🎬 Movie Recommendation System</h1>
        <p style="font-size: 1.2rem; margin: 0; opacity: 0.9;">
            Discover your next favorite movie with personalized recommendations
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Check backend health
    health_status = api_client.get_health()
    if health_status.get("status") != "healthy":
        st.error("⚠️ Backend API is not responding. Please make sure the FastAPI server is running on http://localhost:8000")
        st.info("💡 **How to start the backend:**\n\n1. Open terminal in backend folder\n2. Run: `python start_server.py`")
        return
    
    # Initialize session state
    if 'current_recommendations' not in st.session_state:
        st.session_state.current_recommendations = []
    if 'recommendation_count' not in st.session_state:
        st.session_state.recommendation_count = DEFAULT_RECOMMENDATION_COUNT
    if 'need_new_recommendations' not in st.session_state:
        st.session_state.need_new_recommendations = False
    
    # Main application flow
    if 'selected_genre' not in st.session_state or not st.session_state.selected_genre:
        # Step 1: Genre Selection
        available_genres = api_client.get_genres()
        
        if not available_genres:
            st.error("Could not load movie genres. Please check the backend connection.")
            return
        
        selected_genre = display_genre_selector(available_genres)
        
    else:
        # Step 2: Show Recommendations and Handle Details
        selected_genre = st.session_state.selected_genre
        
        # Header with selected genre
        st.markdown(f"""
        <div style="
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
            color: white;
        ">
            <h2>🎭 {selected_genre} Movies</h2>
            <p style="margin: 0; opacity: 0.9;">Here are some great {selected_genre.lower()} movies for you!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Action buttons
        col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
        
        with col1:
            if st.button("🔄 Get New Recommendations", type="primary", use_container_width=True, key="get_new_recs"):
                # Clear ALL related states
                st.session_state.current_recommendations = []
                if 'show_details_for' in st.session_state:
                    del st.session_state.show_details_for
                # Clear any cached movie details
                keys_to_delete = [key for key in st.session_state.keys() if key.startswith('movie_details_')]
                for key in keys_to_delete:
                    del st.session_state[key]
                
                # Force immediate rerun without API call first
                st.session_state.need_new_recommendations = True
                st.rerun()
        
        with col2:
            if st.button("🎭 Choose Different Genre", use_container_width=True, key="choose_genre"):
                reset_app_state()
                st.rerun()
        
        with col3:
            # Recommendation count selector
            new_count = st.selectbox(
                "Movies to show:",
                options=[3, 6, 9, 12],
                index=[3, 6, 9, 12].index(st.session_state.recommendation_count) if st.session_state.recommendation_count in [3, 6, 9, 12] else 1,
                key="count_selector"
            )
            if new_count != st.session_state.recommendation_count:
                st.session_state.recommendation_count = new_count
                # Clear current recommendations to force reload
                st.session_state.current_recommendations = []
                st.session_state.need_new_recommendations = True
                st.rerun()
        
        with col4:
            st.markdown("") # Empty space for alignment
        
        # Handle the actual API call after state is clean
        if st.session_state.get('need_new_recommendations', False):
            with st.spinner("Loading new recommendations..."):
                try:
                    recommendations = api_client.get_movie_recommendations(
                        selected_genre,
                        st.session_state.recommendation_count
                    )
                    
                    if recommendations:
                        st.session_state.current_recommendations = recommendations
                        st.success(f"✅ Found {len(recommendations)} new {selected_genre} movies!")
                    else:
                        st.error("No movies found. Please try again.")
                        
                except Exception as e:
                    st.error(f"Error loading recommendations: {str(e)}")
                
                # Clear the flag
                st.session_state.need_new_recommendations = False
        
        # Load initial recommendations if needed
        elif not st.session_state.current_recommendations:
            with st.spinner("Loading movie recommendations..."):
                recommendations = api_client.get_movie_recommendations(
                    selected_genre,
                    st.session_state.recommendation_count
                )
                st.session_state.current_recommendations = recommendations
        
        # Load recommendations if not already loaded
        if not st.session_state.current_recommendations:
            with st.spinner("Loading movie recommendations..."):
                recommendations = api_client.get_movie_recommendations(
                    selected_genre,
                    st.session_state.recommendation_count
                )
                st.session_state.current_recommendations = recommendations
        
        # Display movie grid
        if st.session_state.current_recommendations:
            display_movie_grid(st.session_state.current_recommendations)
        
        # Handle movie details
        handle_movie_details()
        
        # Footer with stats
        if st.session_state.current_recommendations:
            st.markdown("---")
            st.markdown(f"""
            <div style="text-align: center; color: #666; padding: 20px;">
                📊 Showing {len(st.session_state.current_recommendations)} {selected_genre} movies
                | 🎬 Powered by FastAPI & Streamlit
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
