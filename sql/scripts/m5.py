import sqlite3


def main():
    print("Hello from sql!")
    con = sqlite3.connect("tmp.db")
    cur = con.cursor()

    # add a new column called director
    cur.execute("ALTER TABLE movie ADD COLUMN director TEXT")
    con.commit()

    # insert a new row
    cur.execute(
        "INSERT INTO movie(title, year, score, director) VALUES ('The Dark Knight', 2008, 9.0, 'Christopher Nolan')"
    )
    con.commit()

    cur.execute("SELECT * FROM movie")
    print(cur.fetchall())


if __name__ == "__main__":
    main()
