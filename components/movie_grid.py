# frontend/components/movie_grid.py
"""
Movie grid display component with poster placeholders
"""
import streamlit as st
from utils.constants import MOVIES_PER_ROW

def display_movie_grid(movies: list):
    """Display movies in a responsive grid with poster placeholders"""
    
    if not movies:
        st.warning("No movies found for this genre.")
        return
    
    st.subheader(f"🍿 Recommended Movies ({len(movies)} found)")
    st.write("Click 'See Details' to learn more about any movie:")
    
    # Display movies in rows of 3
    for i in range(0, len(movies), MOVIES_PER_ROW):
        cols = st.columns(MOVIES_PER_ROW)
        
        for j, movie in enumerate(movies[i:i+MOVIES_PER_ROW]):
            with cols[j]:
                # Use st.container for clean layout
                with st.container():
                    # Simple poster placeholder - NO HTML
                    st.markdown("🎬", help="Movie Poster Placeholder")
                    
                    # Movie title
                    st.subheader(movie['title'])
                    
                    # Movie info using simple text
                    st.write(f"**Year:** {movie['year']}")
                    st.write(f"**Genre:** {movie['genre']}")
                    
                    # Simple star rating
                    rating = movie['rating']
                    stars = "⭐" * int(rating // 2)
                    st.write(f"**Rating:** {stars} ({rating}/10)")
                    
                    # See details button
                    if st.button(
                        "👁️ See Details", 
                        key=f"details_{movie['id']}", 
                        use_container_width=True,
                        type="secondary"
                    ):
                        st.session_state.show_details_for = movie['id']
                        st.rerun()
                
                # Add some spacing
                st.write("")
