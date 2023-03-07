#database
from multiprocessing import connection
import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

db = sqlite3.connect("RealDB.db")
cursor = db.cursor()

