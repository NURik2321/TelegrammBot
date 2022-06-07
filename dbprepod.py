import sqlite3

class DatabasePropod:
    def __init__(self, n):
        self.connection = sqlite3.connect(n)
        self.cursor = self.connection.cursor()

    def user_check(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(res))
    def getPrepod(self,name):
        with self.connection:
             res = self.cursor.execute("SELECT description FROM prepods WHERE name = ?", (name,)).fetchall()
             if len(res) == 0:
                 return None
             else:
                for row in res:
                   description = str(row[0])
                return description

