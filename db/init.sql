USE summary;

CREATE TABLE text_data(
        id INT AUTO_INCREMENT PRIMARY KEY,
        text TEXT,
        text_summary TEXT
);

INSERT INTO text_data(text, text_summary) VALUES ('This is a test', 'Test.');

SELECT * FROM text_data;
