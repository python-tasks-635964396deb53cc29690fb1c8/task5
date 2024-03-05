from re import match, I

pattern = r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$'


def is_ipv4(address: str) -> bool:
    return bool(match(pattern, address, I))
