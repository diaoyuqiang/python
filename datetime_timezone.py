from datetime import datetime, timedelta, timezone

dt = datetime.utcnow()
dt = dt.replace(tzinfo=timezone.utc)  # 设置utc标准时区
print(dt)

zone = timezone(timedelta(hours=8))  # UTC+8 小时
local_tm = dt.astimezone(zone)  # 设置了新时区的时间
print(local_tm)

# 查看local_tm的时区
print(local_tm.tzinfo)