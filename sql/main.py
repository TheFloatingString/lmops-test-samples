import sqlite3


def main():
    print("Hello from sql!")
    con = sqlite3.connect("tmp.db")
    cur = con.cursor()

    cur.execute("CREATE TABLE movie(title, year, score)")


if __name__ == "__main__":
    main()
