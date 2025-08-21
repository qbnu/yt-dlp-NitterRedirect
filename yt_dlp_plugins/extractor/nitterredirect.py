import re

from yt_dlp.extractor.twitter import TwitterIE

class NitterRedirectIE(TwitterIE):
    IE_NAME = 'NitterRedirect'

    INSTANCES = (
        'xcancel.com',
        'nuku.trabun.org',
        'lightbrd.com',
    )
    _DOMAIN_RE = r'nitter(?:\.[a-zA-Z0-9-]+){1,2}'
    _INSTANCES_RE = fr'(?:{_DOMAIN_RE}|{"|".join(map(re.escape, INSTANCES))})'
    _VALID_URL = fr'https?://{_INSTANCES_RE}/(?:[^/]+)/status/(?P<id>[0-9]+)(#.)?(?P<index>)?'
