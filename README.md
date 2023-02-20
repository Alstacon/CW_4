![logo](./readme_assets/logo.svg)
<a href="https://codecov.io/gh/Alstacon/MovieCon" > <img src="https://img.shields.io/codecov/c/github/Alstacon/MovieCon?color=FFD400&style=plastic"></a>

### 🍿 MovieCon —
This is a web application, an interactive searchable movie database with the ability to add movies, genres or directors to favorites. 
___
## Tech stack:
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)&nbsp;&nbsp;
![Postgres](https://img.shields.io/badge/postgres-FFD400?style=for-the-badge&logo=postgresql&logoColor=black)&nbsp;&nbsp;
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)&nbsp;&nbsp;
![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-FFD400?style=for-the-badge&logo=alchemy&logoColor=000000)&nbsp;&nbsp;
![Docker](https://img.shields.io/badge/docker-000000?style=for-the-badge&logo=docker&logoColor=white)

___
### **👀 User**
    
    Each user has a profile page where they can choose their favorite genre, specify their first and last name, and change their password if necessary.    
    
    Implemented a mechanism for adding and removing movies to/from bookmarks, as well as viewing all movies saved to bookmarks.
### **🔑 Authentication**
    
    In order for each user to have the opportunity to bookmark their favorite movies for viewing later, JWT-based registration and authentication pages are implemented.
### **🎬 Films, directors, genres**
    
    For films, directors and genres, the ability to read is implemented.    
    
    Pagination is implemented for all objects.

___
## Usage:
1) Clone the repository
`git clone https://github.com/Alstacon/ToDoCon.git`.
2) Change `.env.example`'s file name for `.env` and fill it with valid parameters.
3) Run docker `docker-compose up --build -d`.
