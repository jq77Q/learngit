import json
import os
total=0
level_count={}
user_count={}
last_err_mag=None
#定义函数
def analyze_log(filepath) -> dict:
    f=open(filepath,"r",encoding="utf_8")
    for line in f:
        line =  line.strip()
        if not line:
            continue
        try:
            log = json.loads(line)
            need_keys = ["timestamp","level","user","message"]
            total = total + 1
            lv = log.get("level")
            user = log.get("user")
            lever_count[lv]= lever_count.get(lv,0)+1
            user_count[user]= user_count.get(user,0)+1
            if lv =="error":
                last_err_msg = log.get("message")
                return{
                    "total":dict(by_level=level_count,by_user=user_count),}                
                    if __name__=="__main__":
                        result = analyze_log("app>jsonl")
                        print(result)

