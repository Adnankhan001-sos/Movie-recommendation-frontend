# 🎬 CinemaScope - Movie Recommendation System

A modern, full-stack movie recommendation application powered by real movie data from The Movie Database (TMDB).

## ✨ Features

### 🎭 **Real Movie Data**
- **Live TMDB Integration**: Real movies, posters, ratings, and descriptions
- **18+ Genres**: From Action to Western, discover movies across all genres
- **High-Quality Posters**: Professional movie posters from TMDB
- **Current Movies**: Always up-to-date with popular and trending films

### 🖥️ **Modern Frontend**
- **Beautiful UI**: Clean, responsive design with hover effects
- **Movie Grid**: Professional movie cards with posters and ratings
- **Detailed View**: Comprehensive movie information with large posters
- **Smooth Interactions**: Loading states, success messages, and animations

### ⚡ **Powerful Backend**
- **FastAPI**: High-performance REST API with automatic documentation
- **Smart Recommendations**: Intelligent movie selection with variety
- **Error Handling**: Robust error handling and validation
- **CORS Support**: Seamless frontend-backend communication

## 🏗️ **Architecture**

```
Frontend (Streamlit Cloud)
    ↓ HTTPS API Calls
Backend (Render)
    ↓ TMDB API Integration
The Movie Database
```

## 🚀 **Live Demo**

- **Frontend**: [Your Streamlit Cloud URL]
- **Backend API**: https://movie-recommendation-backend-2-fur6.onrender.com
- **API Docs**: https://movie-recommendation-backend-2-fur6.onrender.com/docs

## 🛠️ **Tech Stack**

**Backend:**
- FastAPI (Python web framework)
- Pydantic (data validation)
- Requests (HTTP client)
- Python-dotenv (environment variables)

**Frontend:**
- Streamlit (web app framework)
- Requests (API communication)
- Custom CSS (styling)

**External APIs:**
- The Movie Database (TMDB) API

## 📁 **Project Structure**

```
movie-recommendation-app/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI application
│   │   ├── models.py            # Pydantic models
│   │   ├── services/
│   │   │   ├── tmdb_service.py  # TMDB API integration
│   │   │   ├── movie_service.py # Movie business logic
│   │   │   └── recommendation_service.py # Recommendation logic
│   │   └── api/
│   │       └── endpoints.py     # API endpoints
│   ├── .env                     # Environment variables
│   ├── requirements.txt         # Python dependencies
│   └── start_server.py         # Development server
├── frontend/
│   ├── components/
│   │   └── movie_display.py    # Movie display components
│   ├── services/
│   │   └── api_client.py       # Backend API client
│   ├── utils/
│   │   └── constants.py        # App constants
│   ├── app.py                  # Main Streamlit app
│   └── requirements.txt        # Python dependencies
└── README.md
```

## 🔧 **Local Development**

### Prerequisites
- Python 3.8+
- TMDB API Key (free from themoviedb.org)

### Backend Setup
```bash
cd backend
pip install -r requirements.txt

# Create .env file with your TMDB API key
echo "TMDB_API_KEY=your_api_key_here" > .env

# Start the server
python start_server.py
```

### Frontend Setup
```bash
cd frontend
pip install -r requirements.txt

# Update constants.py with local backend URL if needed
# API_BASE_URL = "http://localhost:8000/api"

# Start the app
streamlit run app.py
```

## 🌐 **Deployment**

### Backend (Render)
1. Connect your GitHub repository to Render
2. Add environment variable: `TMDB_API_KEY`
3. Deploy from `backend/` folder

### Frontend (Streamlit Cloud)
1. Connect your GitHub repository to Streamlit Cloud
2. Set main file path: `frontend/app.py`
3. Deploy automatically

## 📊 **API Endpoints**

- `GET /` - Health check and API info
- `GET /api/health` - Service health status
- `GET /api/genres` - Available movie genres
- `GET /api/movies/recommendations` - Get movie recommendations
- `GET /api/movies/{id}` - Get detailed movie information
- `GET /docs` - Interactive API documentation

## 🎯 **Key Features Implemented**

### Backend
- ✅ TMDB API integration with error handling
- ✅ Genre-based movie discovery
- ✅ Random movie selection for variety
- ✅ Movie poster URL generation
- ✅ Comprehensive movie details
- ✅ RESTful API design
- ✅ Automatic API documentation

### Frontend
- ✅ Responsive movie grid layout
- ✅ Real movie poster display
- ✅ Interactive movie details modal
- ✅ Genre selection with preview
- ✅ Loading states and error handling
- ✅ Modern, professional UI design
- ✅ Mobile-friendly responsive design

## 🔮 **Future Enhancements**

- 🔍 **Search Functionality**: Search movies by title, actor, or director
- 👤 **User Profiles**: Save favorites and viewing history
- 🎬 **Watchlists**: Create and manage personal movie lists
- 🤖 **AI Recommendations**: Machine learning-based recommendations
- 🎭 **Actor Information**: Cast and crew details
- 🎪 **Movie Trailers**: Embedded video trailers
- 📱 **Mobile App**: React Native or Flutter mobile app
- 🔐 **Authentication**: User accounts and personalization

## 🤝 **Contributing**

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 **License**

This project is licensed under the MIT License.

## 🙏 **Credits**

- Movie data provided by [The Movie Database (TMDB)](https://www.themoviedb.org/)
- Built with [FastAPI](https://fastapi.tiangolo.com/) and [Streamlit](https://streamlit.io/)

---

**Built with ❤️ by Fallahuddin khan**