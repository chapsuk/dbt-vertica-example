import csv
import datetime
import random

from typing import Any, Iterable

countries = ['RU', 'US', 'UK', 'ES']
total_uids = 1000
days = 90
total_days = datetime.timedelta(days=days)
now = datetime.datetime.today()
from_date = now - total_days - datetime.timedelta(minutes=now.minute, hours=now.hour, seconds=now.second, microseconds=now.microsecond)

def gen_regs():
    yield ["user_id","email","country","ref","created_at"]
    reg_date = from_date
    total = 0
    print("Generating registrations...")
    for uid in range(1, total_uids):
        ref = ""
        if uid%30 == 0:
            ref = "http://bro.bro?bro=%d" % (uid-15)
        if uid%200 == 0:
            reg_date += datetime.timedelta(days=1)
        total +=1
        yield [uid, 'foo%d@bar.com' % uid, countries[uid%len(countries)], ref, reg_date + datetime.timedelta(seconds=random.randint(0, total_days.total_seconds()))]
    print("Generated %d registrations events" % total)

def gen_logins():
    yield ["user_id","created_at"]
    total = 0
    print("Generating logins...")
    for dt in [from_date - datetime.timedelta(days=x) for x in range(days)]:
        for _ in range(50):
            total +=1
            yield [random.randint(1, total_uids), dt + datetime.timedelta(seconds=random.randint(0, total_days.total_seconds()))]
    print("Generated %d logins events" % total)

def gen_bro():
    yield ["from_bro","to_bro","created_at"]
    total = 0
    print("Generating bros...")
    for dt in [from_date - datetime.timedelta(days=x) for x in range(days)]:
        for _ in range(250):
            total +=1
            yield [random.randint(1, total_uids), random.randint(1, total_uids), dt + datetime.timedelta(seconds=random.randint(0, total_days.total_seconds()))]
    print("Generated %d bros events" % total)

def write_csv(filename: str, rows: Iterable[Iterable[Any]]):
    with open(filename, 'w+', newline='') as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        w.writerows(rows)


if __name__ == "__main__":
    write_csv("./data/events_registration.csv", gen_regs())
    write_csv("./data/events_login.csv", gen_logins())
    write_csv("./data/events_bro.csv", gen_bro())
