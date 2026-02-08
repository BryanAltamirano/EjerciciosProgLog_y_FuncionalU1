logs = [
("192.168.1.254", "/home", "OperaGX"),
("192.168.1.255", "/login", "Firefox"),
("192.168.1.256", "/dashboard", "Chrome"),
("192.168.1.257", "/home", "Edge"),
("192.168.1.258", "/home", "NavegadorX"),
]

ip_urls = {}
visitas = {}
navs = {}
ips = set()

for l in logs:

    ip = l[0]
    url = l[1]
    nav = l[2]

    ips.add(ip)

    if ip not in ip_urls:
        ip_urls[ip] = set()
    ip_urls[ip].add(url)

    if url in visitas:
        visitas[url] = visitas[url] + 1
    else:
        visitas[url] = 1

    if nav in navs:
        navs[nav] = navs[nav] + 1
    else:
        navs[nav] = 1

print(ip_urls)
print()
print(visitas)
print()
print(navs)
print()
print(sorted(list(ips)))
print()
