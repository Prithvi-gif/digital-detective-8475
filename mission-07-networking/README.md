# Mission 7 — How Computers Communicate

## Task 7.1 — Explain Network Concepts

| Concept | Explain it in your own words | Example |
|---|---|---|
| LAN (Local Area Network) | A network that connects devices within a small geographical area. | Computers connected in a college computer lab. |
| MAN (Metropolitan Area Network) | A network that connects devices across a city or a large campus area. | A network connecting different college buildings across a city. |
| WAN (Wide Area Network) | A network that connects devices over large geographical areas. | The Internet. |
| DNS (Domain Name System) | Translates a domain name into an IP address so computers can locate websites. | Translating `google.com` into an IP address. |
| Router | Connects networks and forwards data between them. | A home Wi-Fi router connecting devices to the Internet. |
| Protocol | A set of rules that devices follow to communicate. | HTTP and HTTPS are used for web communication. |
| Packet switching | Data is divided into smaller packets that travel across a network and are reassembled at the destination. | Sending a photo over the Internet. |
| Client-server | A client requests a service or resource, and a server provides it. | A web browser requesting a webpage from a web server. |

## Task 7.2 — Observe Network Information

### Connectivity Test

Command used:

`ping -c 4 example.com`

Observations:
- 4 packets were transmitted.
- 4 packets were received.
- Packet loss was 0%.
- Average round-trip time was 11.750 ms.

**Explanation:** A connectivity test helps check whether a computer can reach another host over a network. The ping command uses ICMP packets and measures response time.

### DNS Lookup

Command used:

`nslookup example.com`

Observations:
- Domain queried: `example.com`
- DNS server: `8.8.8.8`
- Two IP addresses were returned: `104.20.23.154` and `172.66.147.243`.
- The response was marked non-authoritative.

**Explanation:** DNS translates human-readable domain names into IP addresses. This allows computers to locate the correct website server without users having to remember IP addresses.

### Role of DNS

When a user enters a website name in a browser, DNS helps find the corresponding IP address so the browser can connect to the website.

## Task 7.3 — What Happens When You Open a Website?

1. The user enters a website address, such as `example.com`, into a web browser.
2. The browser checks whether it already has the required IP address stored in its cache.
3. If needed, the browser sends a DNS query to translate the domain name into an IP address.
4. The browser uses the IP address to connect to the destination server through the network.
5. The client and server establish a connection and communicate using the appropriate protocol, such as HTTPS.
6. The browser sends an HTTP request to the server, and the server processes the request and sends back a response containing webpage data.
7. The browser interprets the received HTML, CSS, JavaScript, and other resources and displays the webpage to the user.

### Conclusion

In this mission, I learned how computers communicate over networks, how DNS resolves domain names, and how connectivity can be tested using ping and nslookup. I also understood the basic process that takes place when a user opens a website.


