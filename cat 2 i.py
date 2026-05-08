from datetime import datetime, timedelta


dt_str = input("Enter date (YYYY-MM-DD): ")
t1_str = input("Enter first time (YYYY-MM-DD HH:MM:SS): ")
t2_str = input("Enter second time (YYYY-MM-DD HH:MM:SS): ")


dt = datetime.strptime(dt_str, "%Y-%m-%d")
print(f"Date: {dt.date()}")


t1, t2 = datetime.strptime(t1_str, "%Y-%m-%d %H:%M:%S"), datetime.strptime(t2_str, "%Y-%m-%d %H:%M:%S")
print(f"Diff: {abs((t2 - t1).total_seconds())} seconds")


now = datetime.now()
print(f"Now: {now.strftime('%Y-%m-%d %H:%M:%S, %A')}")


days = int(input("Days to shift: "))
print(f"Plus: {(dt + timedelta(days=days)).date()}, Minus: {(dt - timedelta(days=days)).date()}")


start = datetime.strptime(input("Start (YYYY-MM-DD): "), "%Y-%m-%d")
end = datetime.strptime(input("End (YYYY-MM-DD): "), "%Y-%m-%d")
weekends = sum(1 for i in range((end - start).days + 1) if (start + timedelta(days=i)).weekday() >= 5)
print(f"Weekends: {weekends}")
