from decouple import config

DATABASE_URL = config("DATABASE_URL", default="sqlite+aiosqlite:///./app/db/while_you_are_at_it.db")
