"""
Constants and configuration for the movie recommendation app
"""

# API Configuration
API_BASE_URL = "http://localhost:8000/api"

# Genre Icons and Colors
GENRE_CONFIG = {
    "Action": {"icon": "🎬", "color": "#FF6B6B", "description": "High-octane thrills"},
    "Comedy": {"icon": "😂", "color": "#4ECDC4", "description": "Laugh out loud"},
    "Drama": {"icon": "🎭", "color": "#45B7D1", "description": "Emotional stories"},
    "Horror": {"icon": "👻", "color": "#8B5A3C", "description": "Spine-chilling scares"},
    "Romance": {"icon": "💕", "color": "#F7B7A3", "description": "Love stories"},
    "Sci-Fi": {"icon": "🚀", "color": "#6C5CE7", "description": "Future fantasies"},
    "Thriller": {"icon": "🔍", "color": "#2D3436", "description": "Edge-of-seat suspense"},
}

# UI Configuration
MOVIES_PER_ROW = 3
DEFAULT_RECOMMENDATION_COUNT = 6
MAX_RECOMMENDATION_COUNT = 12
