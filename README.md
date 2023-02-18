### 🍿 MovieCon —
This is a web application, an interactive searchable movie database with the ability to add movies, genres or directors to favorites. 

## Tech stack:
  - Flask
  - SQLAlchemy
  - Marshmallow
  - REST
  - CRUD
  - JWT

### **Пользователи**
    
    У каждого пользователя есть страница с его профилем, где он сможет выбрать любимый жанр, указать имя и фамилию, а также в случае необходимости сменить пароль.
    
    Реализован механизм добавления и удаления фильмов в/из закладок, а также просмотр всех сохраненных в закладки фильмов.

### **Аутентификация**
    
    Для того чтобы у каждого пользователя была возможность добавлять понравившиеся фильмы в закладки для просмотра позже реализованы страницы с регистрацией и аутентификацией на основе JWT.

### **Фильмы, режиссеры, жанры**
    
    Для фильмов, режиссеров и жанров реализована возможность чтения (get-запросы).
    
    Для всех объектов реализована пагинация.



## Usage:
1) Clone the repository
`git clone https://github.com/Alstacon/ToDoCon.git`.
2) Change `.env.example`'s file name for `.env` and fill it with valid parameters.
3) Run docker `docker-compose up --build -d`.