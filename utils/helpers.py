"""
Helper functions for the movie recommendation app
"""
import streamlit as st

def display_rating_stars(rating):
    """Convert numeric rating to star display"""
    full_stars = int(rating // 2)
    half_star = 1 if (rating % 2) >= 1 else 0
    empty_stars = 5 - full_stars - half_star
    
    stars = "⭐" * full_stars
    if half_star:
        stars += "✨"
    stars += "☆" * empty_stars
    
    return f"{stars} ({rating}/10)"

def format_runtime(minutes):
    """Convert runtime minutes to hours and minutes"""
    if minutes < 60:
        return f"{minutes}min"
    else:
        hours = minutes // 60
        remaining_minutes = minutes % 60
        return f"{hours}h {remaining_minutes}min"

def reset_app_state():
    """Reset application state to start over"""
    keys_to_reset = [
        'selected_genre', 
        'current_recommendations', 
        'show_details_for',
        'recommendation_count'
    ]
    for key in keys_to_reset:
        if key in st.session_state:
            del st.session_state[key]
