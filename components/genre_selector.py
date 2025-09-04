"""
Visual genre selection component
"""
import streamlit as st
from utils.constants import GENRE_CONFIG

def display_genre_selector(available_genres: list) -> str:
    """Display visual genre selection cards and return selected genre"""
    
    st.markdown("### 🎭 Choose Your Movie Genre")
    st.markdown("Select a genre to discover amazing movies:")
    
    # Create genre selection in a grid layout
    cols = st.columns(3)  # 3 genres per row
    selected_genre = None
    
    for idx, genre in enumerate(available_genres):
        col_idx = idx % 3
        genre_info = GENRE_CONFIG.get(genre, {
            "icon": "🎬", 
            "color": "#888888", 
            "description": "Great movies"
        })
        
        with cols[col_idx]:
            # Create a visual button for each genre
            button_html = f"""
            <div style="
                background: linear-gradient(45deg, {genre_info['color']}, {genre_info['color']}44);
                padding: 20px;
                border-radius: 15px;
                text-align: center;
                margin: 10px 0;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                border: 2px solid transparent;
                transition: all 0.3s ease;
            ">
                <div style="font-size: 2.5rem; margin-bottom: 8px;">
                    {genre_info['icon']}
                </div>
                <div style="
                    font-size: 1.2rem; 
                    font-weight: bold; 
                    color: #ffffff;
                    margin-bottom: 5px;
                ">
                    {genre}
                </div>
                <div style="
                    font-size: 0.9rem; 
                    color: #ffffffcc;
                    font-style: italic;
                ">
                    {genre_info['description']}
                </div>
            </div>
            """
            
            st.markdown(button_html, unsafe_allow_html=True)
            
            # Use Streamlit button for functionality
            if st.button(f"Select {genre}", key=f"genre_{genre}", use_container_width=True):
                selected_genre = genre
                st.session_state.selected_genre = genre
                st.rerun()
    
    return selected_genre
