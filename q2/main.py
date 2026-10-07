import json
import os
class UserManager:
    def __init__(self):
        self.filename = "users.json"
        self.users = []
        self.load_data()
    def load_data(self):
        if os.path.exists(self.filename):
            f = open(self.filename, "r", encoding="utf-8")
            try:
                self.users = json.load(f)
            except:
                self.users = []
            f.close()
    def save_data(self):
        f = open(self.filename, "w", encoding="utf-8")
        json.dump(self.users, f, ensure_ascii=False)
        f.close()
    # 添加用户
    def add_user(self, name, age):
        if len(self.users) ==0:
            new_id = 1
        else:
            new_id = self.users[-1]["id"] + 1
        user = {"id": new_id, "name": name, "age": age}
        self.users.append(user)
        self.save_data()
        return user
    # 查用户
    def get_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                return u
        return None
# 改年龄
    def update_age(self, user_id, new_age):
        for u in self.users:
            if u["id"] == user_id:
                u["age"] = new_age
                self.save_data()
                return True
        return False
# 测试
if __name__ == "__main__":
    m = UserManager()
    print(m.add_user("张三", 18))
    print(m.add_user("李四", 20))
    print(m.get_user(1))
    print(m.update_age(1, 25))
    print(m.get_user(1))