# frontend/components/movie_details.py
"""
Movie details component for displaying individual movie information
"""
import streamlit as st
from services.api_client import api_client

def handle_movie_details():
    """Handle movie details display logic"""
    
    # Only show details if we're not in the middle of loading new recommendations
    if (st.session_state.get('show_details_for') and 
        not st.session_state.get('need_new_recommendations', False)):
        
        movie_id = st.session_state.show_details_for
        cache_key = f"movie_details_{movie_id}"
        
        # Check if we have cached details
        if cache_key not in st.session_state:
            # Only load if we're not currently loading recommendations
            if not st.session_state.get('need_new_recommendations', False):
                with st.spinner("Loading movie details..."):
                    movie_details = api_client.get_movie_details(movie_id)
                    if movie_details:
                        st.session_state[cache_key] = movie_details
        
        # Display details if we have them
        movie_details = st.session_state.get(cache_key)
        if movie_details:
            display_movie_details_simple(movie_details)

def display_movie_details_simple(movie_details: dict):
    """Display detailed movie information in a simple, clean format"""
    
    if not movie_details:
        return
    
    # Create an expander for details to avoid layout conflicts
    with st.expander(f"🎬 {movie_details['title']} - Movie Details", expanded=True):
        
        # Create columns for organized info display
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("⭐ Rating", f"{movie_details['rating']}/10")
        
        with col2:
            st.metric("🎭 Genre", movie_details['genre'])
        
        with col3:
            st.metric("⏱️ Runtime", f"{movie_details['runtime']} min")
        
        # Description
        st.subheader("📝 Plot Summary")
        st.write(movie_details['description'])
        
        # Close button
        if st.button("✖️ Close Details", key="close_details_exp", type="secondary"):
            # Clear the details state
            if 'show_details_for' in st.session_state:
                del st.session_state.show_details_for
            cache_key = f"movie_details_{movie_details['id']}"
            if cache_key in st.session_state:
                del st.session_state[cache_key]
            st.rerun()
