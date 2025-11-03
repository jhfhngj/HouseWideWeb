def parse_response(response):
    lines = response.strip().splitlines()
    status = lines[0] if lines else ""
    ip_port = lines[1] if len(lines) > 1 else None
    return status, ip_port
