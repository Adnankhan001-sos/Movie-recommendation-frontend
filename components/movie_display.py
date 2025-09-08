"""
Enhanced movie display components with real TMDB posters
"""
import streamlit as st

def display_movie_grid_with_posters(movies):
    """Display movies with real TMDB posters in a beautiful grid"""
    if not movies:
        st.warning("No movies found.")
        return
    
    st.subheader(f"🍿 Discovered {len(movies)} Amazing Movies")
    st.markdown("✨ Real movies with real posters from The Movie Database!")
    
    # Display 3 movies per row
    for i in range(0, len(movies), 3):
        cols = st.columns(3)
        
        for j, movie in enumerate(movies[i:i+3]):
            with cols[j]:
                # Movie card container
                with st.container():
                    # Real movie poster or elegant placeholder
                    if movie.get('poster_url'):
                        st.markdown(f"""
                        <div style="text-align: center; margin-bottom: 15px;">
                            <img src="{movie['poster_url']}" 
                                 style="width: 100%; max-width: 200px; border-radius: 12px; 
                                        box-shadow: 0 8px 24px rgba(0,0,0,0.15);
                                        transition: transform 0.3s ease;"
                                 alt="{movie['title']} poster"
                                 onmouseover="this.style.transform='scale(1.05)'"
                                 onmouseout="this.style.transform='scale(1)'">
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        # Elegant fallback for movies without posters
                        st.markdown(f"""
                        <div style="
                            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                            height: 280px;
                            border-radius: 12px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            margin-bottom: 15px;
                            box-shadow: 0 8px 24px rgba(0,0,0,0.15);
                        ">
                            <div style="text-align: center; color: white;">
                                <div style="font-size: 4rem; margin-bottom: 10px; opacity: 0.8;">🎬</div>
                                <div style="font-size: 0.9rem; opacity: 0.7;">No Poster Available</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Movie information with better styling
                    st.markdown(f"""
                    <div style="background: white; padding: 15px; border-radius: 8px; 
                                box-shadow: 0 2px 8px rgba(0,0,0,0.1); margin-bottom: 15px;">
                        <h4 style="margin: 0 0 8px 0; color: #2c3e50; font-size: 1.1rem;">
                            {movie['title']}
                        </h4>
                        <p style="margin: 5px 0; color: #7f8c8d; font-size: 0.9rem;">
                            📅 {movie['year']} • 🎭 {movie['genre']}
                        </p>
                        <p style="margin: 5px 0; color: #f39c12; font-weight: bold; font-size: 0.9rem;">
                            ⭐ {movie['rating']}/10
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # See details button
                    if st.button("🔍 See Details", key=f"btn_{movie['id']}_{i}_{j}", use_container_width=True):
                        st.session_state.selected_movie_id = movie['id']
                        return movie['id']  # Return the selected movie ID
                
    return None

def show_enhanced_movie_details(movie_details):
    """Enhanced movie details with large poster and comprehensive info"""
    if not movie_details:
        st.error("Could not load movie details.")
        return
    
    # Create layout with poster and details
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Large poster display
        if movie_details.get('poster_url'):
            st.markdown(f"""
            <div style="text-align: center;">
                <img src="{movie_details['poster_url']}" 
                     style="width: 100%; max-width: 300px; border-radius: 12px; 
                            box-shadow: 0 12px 32px rgba(0,0,0,0.2);"
                     alt="{movie_details['title']} poster">
            </div>
            """, unsafe_allow_html=True)
        else:
            # Large elegant placeholder
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                height: 400px;
                border-radius: 12px;
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 12px 32px rgba(0,0,0,0.2);
            ">
                <div style="text-align: center; color: white;">
                    <div style="font-size: 6rem; margin-bottom: 15px; opacity: 0.8;">🎬</div>
                    <div style="font-size: 1.1rem; opacity: 0.7;">No Poster Available</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # Movie details with rich formatting
        st.markdown(f"# 🎬 {movie_details['title']}")
        
        # Movie stats in columns
        stat_col1, stat_col2 = st.columns(2)
        with stat_col1:
            st.metric("📅 Year", movie_details['year'])
            st.metric("⭐ Rating", f"{movie_details['rating']}/10")
        with stat_col2:
            st.metric("🎭 Genre", movie_details['genre'])
            if movie_details.get('runtime'):
                hours = movie_details['runtime'] // 60
                minutes = movie_details['runtime'] % 60
                runtime_str = f"{hours}h {minutes}m" if hours > 0 else f"{minutes}m"
                st.metric("⏱️ Runtime", runtime_str)
        
        # Description with better formatting
        st.markdown("### 📝 Overview")
        st.markdown(f"""
        <div style="
            background: #f8f9fa; 
            padding: 20px; 
            border-radius: 8px; 
            border-left: 4px solid #667eea;
            font-size: 1rem;
            line-height: 1.6;
        ">
            {movie_details['description']}
        </div>
        """, unsafe_allow_html=True)
        
        # TMDB credit
        st.markdown("---")
        st.caption("🎬 Movie data and posters provided by The Movie Database (TMDB)")
