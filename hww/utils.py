def parse_response(response):
    lines = response.strip().splitlines()
    status = lines[0] if lines else ""
    ip = lines[1] if len(lines) > 1 else None
    port = lines[2] if len(lines) > 2 else None
    return status, ip, port
