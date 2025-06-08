import sqlite3


def main():
    print("Hello from sql!")
    con = sqlite3.connect("tmp.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM movie")
    print(cur.fetchall())


if __name__ == "__main__":
    main()
