import re
from urllib.parse import urlparse

def is_api_endpoint(url):
    #Function checks if the string matches a potential url or api pattern
    url_regex = re.compile(
        r'^(https?://)?'       # http:// or https:// (optional)
        r'([a-zA-Z0-9.-]+)'    # Domain name
        r'(\.[a-zA-Z]{2,6})'   # .com, .net, etc.
        r'(:\d+)?'             # Optional port
        r'(/.*)?$',            # Optional path
        re.IGNORECASE
    )

    #Regex check
    if not url_regex.match(url):
        return False

    #URL parse does the breaking of substrings
    parsed_url = urlparse(url)
    return all([parsed_url.scheme, parsed_url.netloc])


