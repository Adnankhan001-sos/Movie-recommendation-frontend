"""
API client for communicating with the deployed TMDB-powered FastAPI backend
"""
import requests
import streamlit as st
from typing import List, Dict, Optional
from utils.constants import API_BASE_URL

class MovieAPIClient:
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url
        self.timeout = 30  # Longer timeout for deployed backend
    
    def get_health(self) -> Dict:
        """Check if the API is healthy"""
        try:
            response = requests.get(f"{self.base_url.replace('/api', '')}/", timeout=self.timeout)
            response.raise_for_status()
            return {"status": "healthy"}
        except requests.exceptions.RequestException as e:
            st.error(f"Backend API is not responding: {e}")
            return {"status": "unhealthy"}
    
    def get_genres(self) -> List[str]:
        """Get all available movie genres"""
        try:
            response = requests.get(f"{self.base_url}/genres", timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get("genres", [])
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to fetch genres: {e}")
            return []
    
    def get_movie_recommendations(self, genre: str, count: int = 6) -> List[Dict]:
        """Get movie recommendations for a specific genre"""
        try:
            params = {"genre": genre, "count": count}
            response = requests.get(f"{self.base_url}/movies/recommendations", params=params, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data.get("movies", [])
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to fetch recommendations: {e}")
            return []
    
    def get_movie_details(self, movie_id: int) -> Optional[Dict]:
        """Get detailed information about a specific movie"""
        try:
            response = requests.get(f"{self.base_url}/movies/{movie_id}", timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to fetch movie details: {e}")
            return None

# Create global API client instance
api_client = MovieAPIClient()
