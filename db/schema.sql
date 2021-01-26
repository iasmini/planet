DROP TABLE IF EXISTS planet;

CREATE TABLE planet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    rotation_period INTEGER,
    orbital_period INTEGER,
    diameter INTEGER,
    climate TEXT,
    gravity TEXT,
    terrain TEXT,
    surface_water INTEGER,
    population INTEGER
);
