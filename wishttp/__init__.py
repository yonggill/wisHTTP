"""
features
-basic HTTP request, GET/POST/PUT/PATCH/DELETE.
-Python friendly parameter management.
"""

import re
import urllib.request
import base64
import json
from io import StringIO

WISHTTP_VERSION = '0.01'


def _call(path, method='GET', headers={}, params={}):
    protocol_with_domain = re.split('://|\?|#|/', path)
    protocol = protocol_with_domain[0]
    domain = protocol_with_domain[1]

    # split detail path data.
    detail_location = re.split('[#?]', path.split(domain)[1])
    location = detail_location[0]
    path_params = detail_location[1] if len(detail_location) > 1 else None

    headers = dict((k.lower(), v) for k, v in headers.items())
    headers["user-agent"] = 'wishttp/%s' % WISHTTP_VERSION

    data = dict()

    request = urllib.request.Request(
        '%s://%s%s' % (protocol, domain, location),
        data if data else None,
        headers
    )
    request.get_method = lambda: method

    result = urllib.request.urlopen(request)
    print(result.read())


