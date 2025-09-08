"""
Constants and configuration for the movie recommendation app with TMDB
"""

# API Configuration - Updated for deployed backend with TMDB
API_BASE_URL = "http://localhost:8000/api"

# Enhanced Genre Configuration
GENRE_CONFIG = {
    "Action": {"icon": "🎬", "color": "#FF6B6B", "description": "High-octane thrills"},
    "Adventure": {"icon": "🗺️", "color": "#FF8C42", "description": "Epic journeys"},
    "Animation": {"icon": "🎨", "color": "#6A4C93", "description": "Animated stories"},
    "Comedy": {"icon": "😂", "color": "#4ECDC4", "description": "Laugh out loud"},
    "Crime": {"icon": "🔫", "color": "#95A5A6", "description": "Criminal underworld"},
    "Documentary": {"icon": "📹", "color": "#7D4F73", "description": "Real-life stories"},
    "Drama": {"icon": "🎭", "color": "#45B7D1", "description": "Emotional stories"},
    "Family": {"icon": "👨‍👩‍👧‍👦", "color": "#96CEB4", "description": "Fun for everyone"},
    "Fantasy": {"icon": "🧙", "color": "#DDA0DD", "description": "Magical worlds"},
    "History": {"icon": "📜", "color": "#CD853F", "description": "Historical tales"},
    "Horror": {"icon": "👻", "color": "#8B5A3C", "description": "Spine-chilling scares"},
    "Music": {"icon": "🎵", "color": "#FFB6C1", "description": "Musical journeys"},
    "Mystery": {"icon": "🔍", "color": "#2F4F4F", "description": "Puzzling mysteries"},
    "Romance": {"icon": "💕", "color": "#F7B7A3", "description": "Love stories"},
    "Sci-Fi": {"icon": "🚀", "color": "#6C5CE7", "description": "Future fantasies"},
    "Thriller": {"icon": "🎯", "color": "#2D3436", "description": "Edge-of-seat suspense"},
    "War": {"icon": "⚔️", "color": "#A0522D", "description": "War stories"},
    "Western": {"icon": "🤠", "color": "#D2691E", "description": "Wild west adventures"},
}

# UI Configuration
MOVIES_PER_ROW = 3
DEFAULT_RECOMMENDATION_COUNT = 6
MAX_RECOMMENDATION_COUNT = 20
