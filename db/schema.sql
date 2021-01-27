DROP TABLE IF EXISTS planet;

CREATE TABLE planet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    rotation_period TEXT,
    orbital_period TEXT,
    diameter TEXT,
    climate TEXT,
    gravity TEXT,
    terrain TEXT,
    surface_water TEXT,
    population INTEGER
);
