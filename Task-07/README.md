# Task 07 - Dank Memer Discord Bot 

## Berry Broker

For this task, I built a Discord bot called "Berry Broker"using Python and
discord.py.

The bot is based on a simple pirate-themed economy. Users can collect Berries,
check their balance, claim daily rewards, interact with other users and appear
on a leaderboard.

I also used SQLite to store the user data so that the Berry balance can be
saved even after restarting the bot.

## Commands

The commands I successfully tested are:

- `!ping` - Checks whether the bot is responding.
- `!daily` - Gives the user their daily Berry reward.
- `!balance` - Shows the user's current Berry balance.
- `!roast @user` - Sends a random roast for the mentioned user.
- `!leaderboard` - Shows the users with the highest Berry balances.




## Project Structure

I divided the bot into different Cogs instead of keeping all the commands in
one large file.

Task-07/
│
├── bot.py
├── database.py
├── berry_broker.db
├── README.md
│
├── cogs/
│   ├── economy.py
│   ├── games.py
│   └── fun.py
│
├── screenshots/
└── venv/


# Main files

* bot.py:

This is the main file of the bot. It starts the Discord bot and loads the
different Cogs.

* database.py:

This file handles the SQLite database and stores information about users and
their Berry balances.

* cogs/economy.py:

This contains the commands related to the Berry economy, such as balance,
daily rewards, trading, robbing and the leaderboard.

* cogs/games.py:

This contains the game-related commands that I experimented with while
building the bot.

* cogs/fun.py:

This contains the fun and meme-style commands.

* berry_broker.db:

This is the SQLite database used to store the bot's user data.

Database :

I used SQLite for storing the user information.

The main users table contains information such as:

user_id - Discord user ID
username - Discord username
balance - Current Berry balance
last_daily - Used for the daily reward cooldown
last_rob - Used for the robbery cooldown

The Discord user ID is used to identify users in the database.

How I built it :

I started by creating a basic Discord bot and first tested whether it could
respond to a simple command.

After that, I added the SQLite database and created the user records. I then
worked on the economy commands and connected them to the database.

I later separated the commands into different Cogs. This made the project
easier to organise because related commands could be kept in separate files.

Finally, I tested the bot inside a Discord server and fixed issues that came
up during testing.

Concepts I learned:

During this task, I learned about:

Python Discord bots
discord.py
Discord commands
Cogs
Async functions
SQLite databases
SQL queries
Discord user IDs
Cooldowns
Python modules
Random number generation
Loading Cogs into a Discord bot
Keeping the bot token separate from the source code

One of the useful things I learned was how Cogs can be used to split a bot
into smaller and more manageable files.

Resources Used:

I referred to the following resources while working on the task:

discord.py documentation
Python documentation
SQLite / sqlite3 documentation
Python random module documentation
Testing

I tested the bot in a private Discord server.

The following commands were successfully tested:

!ping
!daily
!balance
!roast @user
!leaderboard

I also checked that the bot could store and retrieve Berry balances from the
database.

Screenshots of the working commands are included in the screenshots
directory.

What I learned from the task:

The most interesting part of this task was connecting a Discord bot to a
database.

Instead of just making the bot reply to messages, I had to make it remember
information about users and their Berry balances.

I also learned that organising a project into separate Cogs makes it easier
to work on individual features without making the main bot file too large.

There are still some commands that I need to debug and improve, but the main
bot structure and the tested commands are working.
