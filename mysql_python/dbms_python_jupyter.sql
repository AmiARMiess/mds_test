CREATE TABLE IF NOT EXISTS film (
    film_id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    release_year YEAR,
    language_id INT NOT NULL,
    original_language_id INT,
    rental_duration INT NOT NULL DEFAULT 3,
    rental_rate DECIMAL(4,2) NOT NULL DEFAULT 4.99,
    length SMALLINT,
    replacement_cost DECIMAL(5,2) NOT NULL DEFAULT 19.99,
    rating ENUM('G','PG','PG-13','R','NC-17') DEFAULT 'G',
    special_features SET('Trailers','Commentaries','Deleted Scenes','Behind the Scenes'),
    last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO film (film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update) VALUES
(1, 'ACADEMY DINOSAUR', 'A Epic Drama of a Feminist And a Mad Scientist...', 2006, 1, NULL, 6, 0.99, 86, 20.99, 'PG', 'Deleted Scenes,Behind the Scenes', '2006-02-15 05:03:42'),
(2, 'ACE GOLDFINGER', 'A Astounding Epistle of a Database Administrator...', 2006, 1, NULL, 3, 4.99, 48, 12.99, 'G', 'Trailers,Deleted Scenes', '2006-02-15 05:03:42'),
(3, 'ADAPTATION HOLES', 'A Astounding Reflection of a Lumberjack And a ...', 2006, 1, NULL, 7, 2.99, 50, 18.99, 'NC-17', 'Trailers,Deleted Scenes', '2006-02-15 05:03:42'),
(4, 'AFFAIR PREJUDICE', 'A Fanciful Documentary of a Frisbee And a Lumb...', 2006, 1, NULL, 5, 2.99, 117, 26.99, 'G', 'Commentaries,Behind the Scenes', '2006-02-15 05:03:42'),
(5, 'AFRICAN EGG', 'A Fast-Paced Documentary of a Pastry Chef And ...', 2006, 1, NULL, 6, 2.99, 130, 22.99, 'G', 'Deleted Scenes', '2006-02-15 05:03:42');