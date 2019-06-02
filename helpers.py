from datetime import timedelta, datetime


def pairs(x):
    xiter = iter(x)
    return zip(xiter, xiter)


def to_time(seconds):
    td = timedelta(seconds=seconds)
    t = datetime(1, 1, 1)
    # Next line might not work on Windows
    return (t + td).strftime("%-I %p")
