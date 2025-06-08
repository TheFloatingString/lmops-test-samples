import sqlite3


def main():
    print("Hello from sql!")
    con = sqlite3.connect("tmp.db")
    cur = con.cursor()

    cur.execute("INSERT INTO movie(title, year, score) VALUES ('Star Wars', 1977, 8.6)")
    cur.execute(
        "INSERT INTO movie(title, year, score) VALUES ('The Empire Strikes Back', 1980, 8.7)"
    )
    cur.execute(
        "INSERT INTO movie(title, year, score) VALUES ('Return of the Jedi', 1983, 8.3)"
    )
    con.commit()

    cur.execute("SELECT * FROM movie")
    print(cur.fetchall())


if __name__ == "__main__":
    main()
