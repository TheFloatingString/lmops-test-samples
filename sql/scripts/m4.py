import sqlite3


def main():
    print("Hello from sql!")
    con = sqlite3.connect("tmp.db")
    cur = con.cursor()

    # alter existing row
    cur.execute("UPDATE movie SET score = 9.0 WHERE title = 'Return of the Jedi'")
    con.commit()

    cur.execute("SELECT * FROM movie WHERE year > 1980")
    print(cur.fetchall())


if __name__ == "__main__":
    main()
