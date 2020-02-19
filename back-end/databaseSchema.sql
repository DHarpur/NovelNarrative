DROP TABLE users;
DROP TABLE movies;
DROP TABLE shows;
DROP TABLE books;
DROP TABLE genre;

CREATE TABLE users (
  uid SERIAL PRIMARY KEY,
  username VARCHAR(255) UNIQUE,
  email VARCHAR(255),
  email_verified BOOLEAN,
  password VARCHAR(255),
  date_created DATE,
  last_login DATE
);

CREATE TABLE movies (
  movieid SERIAL PRIMARY KEY,
  movie_name VARCHAR(255),
  directed_by VARCHAR(255),
  description VARCHAR(255),
  year_released DATE,
  rating NUMBER(1,2),
  genreid INTEGER REFERENCES genre(genreid)
);

CREATE TABLE shows (
  showid SERIAL PRIMARY KEY,
  show_name VARCHAR(255),
  description VARCHAR(255),
  year_released DATE,
  episode_count INTEGER,
  season_count INTEGER,
  rating NUMBER(1,2),
  genreid INTEGER REFERENCES genre(genreid)
);

CREATE TABLE books (
  bookid SERIAL PRIMARY KEY,
  book_name VARCHAR(255),
  isbn VARCHAR(30) UNIQUE,
  author VARCHAR(255),
  description VARCHAR(255),
  rating NUMBER(1,2),
  genreid INTEGER REFERENCES genre(genreid)
);

CREATE TABLE genre (
  genreid SERIAL PRIMARY KEY,
  genre_name VARCHAR(100)
);