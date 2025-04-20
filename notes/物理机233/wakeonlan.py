import os
import time
import datetime

MAC_ADDRESS = "44:8a:5b:9a:08:6b"

def wake_up():
    """使用 wakeonlan 命令发送 WoL 魔法包"""
    os.system(f"wakeonlan {MAC_ADDRESS}")
    print(f"[{datetime.datetime.now()}] 已发送魔法包到 {MAC_ADDRESS}")

def main():
    """每 30 秒检测一次时间，如果是 4:10 AM，则发送 WoL"""
    while True:
        now = datetime.datetime.now()
        print(now)
        # print(f"{now.hour}")
        # print(f"{now.minute}")

        if now.hour == 20 and now.minute == 10:
            wake_up()
            print("[qwq]启动了奥！")

        time.sleep(30)


if __name__ == "__main__":
    main()


    
    
# def main():
#     """每 30 秒检测一次时间，如果是 4:10 AM，则发送 WoL"""
#     sent_today = False
#     while True:
#         now = datetime.datetime.now()

#         if now.hour == 4 and now.minute == 10:
#             if not sent_today:
#                 wake_up()
#                 sent_today = True
#         else:
#             sent_today = False  # 时间过了 4:10 AM，重置标记，允许下一天发送

#         time.sleep(30)
