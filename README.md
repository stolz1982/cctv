CREATE TABLE IF NOT EXISTS autokennzeichen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    autokennzeichen VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)  ENGINE=INNODB;

# cctv
CCTV project
