import sqlite3

class Database:
    def __init__(self, n):
        self.connection = sqlite3.connect(n)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))

    def user_check(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(res))

    def set_nickname(self, user_id, nickname):
        with self.connection:
            return self.cursor.execute("UPDATE users SET nickname = ? WHERE user_id = ?", (nickname, user_id))

    def get_signup(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT signup FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in res:
                signup = str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE users SET signup = ? WHERE user_id = ?", (signup, user_id))
    def set_email(self,user_id,email):
        with self.connection:
            return self.cursor.execute("UPDATE users SET email = ? WHERE user_id = ?", (email, user_id))
    def get_email(self,user_id):
        with self.connection:
            res = self.cursor.execute("SELECT email FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in res:
                email = str(row[0])
            return email
    def set_password(self,user_id,password):
        with self.connection:
            return self.cursor.execute("UPDATE users SET password = ? WHERE user_id = ?", (password, user_id))
    def get_password(self,user_id):
        with self.connection:
            res = self.cursor.execute("SELECT password FROM users WHERE user_id = ?", (user_id,)).fetchall()
            for row in res:
                password = str(row[0])
            return password
