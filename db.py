import  sqlite3

class Database:
    def __int__(self,db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
    def add_user(self,user_id):
        with self.connection:
            self.cursor.execute("INSERT INTO 'users' (user_id) VALUE (?)",user_id)
    def user_check(self,user_id):
        with self.connection:
            res = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?",(user_id)).fetchall()
            return bool(len(res))
    def set_nickname(self,user_id,nickname):
        with self.connection:
            return  self.cursor.execute("UPDATE 'users' SET 'nickname' = ? WHERE 'user_ud' = ?",(nickname,user_id))
    def get_signup(self,user_id):
        with self.connection:
            res = self.cursor.execute("SELECT 'signup' FROM 'users' WHERE 'user_id' = ?",(user_id)).fetchall()
            for row in res:
                sign_up = str(row[0])
            return sign_up

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE 'users' SET 'signup' = ? WHERE 'user_ud' = ?", (signup, user_id))
