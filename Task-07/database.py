import sqlite3
from datetime import datetime


DATABASE = "berry_broker.db"


def connect():
    """Create and return a connection to the SQLite database."""
    return sqlite3.connect(DATABASE)


def initialize_database():
    """Create the users table if it does not already exist."""
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            balance INTEGER NOT NULL DEFAULT 100,
            last_daily TEXT,
            last_rob TEXT
        )
    """)

    connection.commit()
    connection.close()


def get_user(user_id, username):
    """Get a user from the database, creating them if necessary."""
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT user_id, username, balance, last_daily, last_rob "
        "FROM users WHERE user_id = ?",
        (str(user_id),)
    )

    user = cursor.fetchone()

    if user is None:
        cursor.execute(
            """
            INSERT INTO users (user_id, username, balance)
            VALUES (?, ?, ?)
            """,
            (str(user_id), username, 100)
        )
        connection.commit()

        cursor.execute(
            "SELECT user_id, username, balance, last_daily, last_rob "
            "FROM users WHERE user_id = ?",
            (str(user_id),)
        )

        user = cursor.fetchone()

    else:
        # Keep the username updated if the Discord username changes.
        cursor.execute(
            "UPDATE users SET username = ? WHERE user_id = ?",
            (username, str(user_id))
        )
        connection.commit()

    connection.close()
    return user


def get_balance(user_id, username):
    """Return a user's current Berry balance."""
    user = get_user(user_id, username)
    return user[2]


def change_balance(user_id, username, amount):
    """Add or subtract Berries from a user's balance."""
    get_user(user_id, username)

    connection = connect()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET balance = balance + ?
        WHERE user_id = ?
        """,
        (amount, str(user_id))
    )

    connection.commit()
    connection.close()


def set_last_daily(user_id, username):
    """Store the current time as the user's last daily claim."""
    get_user(user_id, username)

    connection = connect()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET last_daily = ?
        WHERE user_id = ?
        """,
        (datetime.now().isoformat(), str(user_id))
    )

    connection.commit()
    connection.close()


def get_last_daily(user_id, username):
    """Return the time of the user's last daily claim."""
    user = get_user(user_id, username)
    return user[3]


def set_last_rob(user_id, username):
    """Store the current time as the user's last raid."""
    get_user(user_id, username)

    connection = connect()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE users
        SET last_rob = ?
        WHERE user_id = ?
        """,
        (datetime.now().isoformat(), str(user_id))
    )

    connection.commit()
    connection.close()


def get_last_rob(user_id, username):
    """Return the time of the user's last raid."""
    user = get_user(user_id, username)
    return user[4]


def get_top_users(limit=5):
    """Return the richest pirates."""
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT username, balance
        FROM users
        ORDER BY balance DESC
        LIMIT ?
        """,
        (limit,)
    )

    users = cursor.fetchall()
    connection.close()

    return users