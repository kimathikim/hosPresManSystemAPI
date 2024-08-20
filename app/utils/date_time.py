<<<<<<< HEAD
# util/date_utils.py

from datetime import datetime


def format_datetime(dt, fmt="%Y-%m-%d %H:%M:%S"):
    """Format a datetime object into a string."""
    return dt.strftime(fmt)


def parse_datetime(date_string, fmt="%Y-%m-%d %H:%M:%S"):
    """Parse a string into a datetime object."""
    return datetime.strptime(date_string, fmt)
=======
# util/date_utils.py

from datetime import datetime


def format_datetime(dt, fmt="%Y-%m-%d %H:%M:%S"):
    if isinstance(dt, str):
        dt = datetime.strptime(dt, fmt)
    return dt.strftime(fmt)


def parse_datetime(date_string, fmt="%Y-%m-%d %H:%M:%S"):
    """Parse a string into a datetime object."""
    return datetime.strptime(date_string, fmt)
>>>>>>> refs/remotes/origin/main
