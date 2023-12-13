import argparse
import psycopg2
from psycopg2 import sql

# Database connection parameters - replace with your own
DB_NAME = ""
DB_USER = ""
DB_PASSWORD = ""
DB_HOST = "localhost"

# Connect to the PostgreSQL database
def connect_db():
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    return conn

# Function to add a new birthday record
def add_birthday(name, month, day, year):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO birthdays (name, birth_month, birth_day, birth_year) VALUES (%s, %s, %s, %s)",
                (name, month, day, year))
    conn.commit()
    print(f"Added birthday for {name}.")
    cur.close()
    conn.close()

# Function to list all birthday records
def list_birthdays():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM birthdays")
    records = cur.fetchall()
    for row in records:
        print(row)
    cur.close()
    conn.close()

# Function to update a birthday record
def update_birthday(name, month, day, year):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE birthdays SET birth_month = %s, birth_day = %s, birth_year = %s WHERE name = %s",
                (month, day, year, name))
    conn.commit()
    print(f"Updated birthday for {name}.")
    cur.close()
    conn.close()

# Function to delete a birthday record
def delete_birthday(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM birthdays WHERE name = %s", (name,))
    conn.commit()
    print(f"Deleted birthday for {name}.")
    cur.close()
    conn.close()

# Command-line interface
def main():
    parser = argparse.ArgumentParser(description="Birthday Records Manager")
    parser.add_argument("action", help="Action to perform: add, list, update, delete")
    parser.add_argument("--name", help="Person's name")
    parser.add_argument("--month", type=int, help="Birth month")
    parser.add_argument("--day", type=int, help="Birth day")
    parser.add_argument("--year", type=int, help="Birth year", nargs='?', default=None)

    args = parser.parse_args()

    if args.action == "add":
        add_birthday(args.name, args.month, args.day, args.year)
    elif args.action == "list":
        list_birthdays()
    elif args.action == "update":
        update_birthday(args.name, args.month, args.day, args.year)
    elif args.action == "delete":
        delete_birthday(args.name)
    else:
        print("Invalid action.")

if __name__ == "__main__":
    main()
