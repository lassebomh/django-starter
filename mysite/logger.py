import logging
import re
from typing import Any

request_log_regex = r"^\"([A-Z]+) /([^\/]*)[^\"]+\" (\d+) \d+$"

exclude_path = set(["static", "__debug__"])


class FilterPathBlacklist(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if record.name != "django.server":
            return True

        message = record.getMessage()

        m = re.match(request_log_regex, message)

        if m is None:
            return True

        method, path, status = m.groups()

        if path in exclude_path and status in ("200", "304"):
            return False

        return True


class VSCodeFormatter(logging.Formatter):
    def __init__(self, fmt: str | None = None, datefmt: str | None = None, style: Any = "%") -> None:
        logging.Formatter.__init__(self, fmt, datefmt, style)

    def format(self, record: logging.LogRecord) -> str:
        # Still apply the default formatter
        message = logging.Formatter.format(self, record)

        reset = "\x1b[0m"

        def getcolor() -> str:
            if record.levelno >= logging.CRITICAL:
                return "\x1b[41m\x1b[37m"
            elif record.levelno >= logging.ERROR:
                return "\x1b[31m"
            elif record.levelno >= logging.WARNING:
                return "\x1b[33m"
            elif record.levelno >= logging.INFO:
                faint = False
                m = re.match(request_log_regex, message)
                if m is not None:
                    method, path, status = m.groups()
                    if method == "GET" and status in ("200", "304"):
                        faint = True

                return ("\033[2m" if faint else "") + "\x1b[36m"
            else:
                return "\x1b[37m"

        color = getcolor()

        return color + message.replace(reset, reset + color) + reset
