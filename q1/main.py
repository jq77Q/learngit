import json
import os
# 定义函数
def analyze_log(filepath: str) -> dict:
    if not os.path.exists(filepath):
        return {"total": 0, "by_level": {}, "by_user": {}, "last_error": None}
    total = 0
    by_level = {}
    by_user = {}
    last_error = None
# 打开文件i
    f = open(filepath, "r", encoding="utf-8")
    print("开始读取日志文件")
    for line in f:
        line = line.strip()
        if not line:
            continue
# 防止报错
        try:
            log = json.loads(line)
            print(f"读取到日志: {log}")
            need_keys = {"timestamp", "level", "user", "message"}
            if not need_keys.issubset(log.keys()):
                print(f"日志缺少必要字段: {log}")
                continue
        except Exception:
            print(f"无法解析日志行: {line}")
            continue
        total = total + 1
        lv = log["level"]
        user = log["user"]
        if lv in by_level:
            by_level[lv] = by_level[lv] + 1
        else:
            by_level[lv] = 1
        if user in by_user:
            by_user[user] = by_user[user] + 1
        else:
            by_user[user] = 1
        if lv == "ERROR":
            last_error = log["message"]
# 关闭文件
    f.close()
    return {
        "total": total,
        "by_level": by_level,
        "by_user": by_user,
        "last_error": last_error
    }
if __name__ == "__main__":
    result = analyze_log("q1/app.jsonl")
    print(result)