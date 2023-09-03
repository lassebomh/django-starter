import re
from logging import Filter, LogRecord

successful_staticfile_regex = r"\"GET /static/[^\"]+\" (200|304)"

class SkipStaticFilter(Filter):
    """ Logging filter to skip logging of staticfiles to terminal """
    def filter(self, record: LogRecord) -> bool:
        return not (
            record.name == 'django.server' and
            re.match(successful_staticfile_regex, record.getMessage())
        )
