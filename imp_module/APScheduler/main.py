import time
from apscheduler.schedulers.background import BackgroundScheduler


def job():
    print("hello", f"{time.time}")




if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, "interval", seconds=3)
    scheduler.start()
