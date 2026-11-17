from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TCP/IP Protocol Suite</title>
  <style>
    body { font-family: Arial, sans-serif; background: #f4f6f9; margin: 0; padding: 20px; color: #222; }
    h1 { text-align: center; color: #1a3c6e; }
    .container { max-width: 900px; margin: auto; }
    .layer { background: #fff; border-left: 6px solid #1a3c6e; border-radius: 6px;
             padding: 12px 20px; margin-bottom: 16px; box-shadow: 0 1px 4px rgba(0,0,0,.1); }
    .layer h2 { margin: 0 0 8px; font-size: 1.2em; color: #1a3c6e; }
    .layer ul { margin: 0; padding-left: 20px; columns: 2; }
    .layer li { margin-bottom: 4px; }
    .app { border-color: #2e7d32; } .app h2 { color: #2e7d32; }
    .trans { border-color: #ef6c00; } .trans h2 { color: #ef6c00; }
    .net { border-color: #6a1b9a; } .net h2 { color: #6a1b9a; }
    .link { border-color: #c62828; } .link h2 { color: #c62828; }
  </style>
</head>
<body>
  <div class="container">
    <h1>TCP/IP Protocol Suite</h1>

    <div class="layer app">
      <h2>4. Application Layer</h2>
      <ul>
        <li>HTTP – Hypertext Transfer Protocol</li>
        <li>HTTPS – HTTP Secure</li>
        <li>FTP – File Transfer Protocol</li>
        <li>TFTP – Trivial File Transfer Protocol</li>
        <li>SMTP – Simple Mail Transfer Protocol</li>
        <li>POP3 – Post Office Protocol v3</li>
        <li>IMAP – Internet Message Access Protocol</li>
        <li>DNS – Domain Name System</li>
        <li>DHCP – Dynamic Host Configuration Protocol</li>
        <li>Telnet – Remote Terminal Protocol</li>
        <li>SSH – Secure Shell</li>
        <li>SNMP – Simple Network Management Protocol</li>
        <li>NTP – Network Time Protocol</li>
      </ul>
    </div>

    <div class="layer trans">
      <h2>3. Transport Layer</h2>
      <ul>
        <li>TCP – Transmission Control Protocol</li>
        <li>UDP – User Datagram Protocol</li>
        <li>SCTP – Stream Control Transmission Protocol</li>
      </ul>
    </div>

    <div class="layer net">
      <h2>2. Internet (Network) Layer</h2>
      <ul>
        <li>IPv4 – Internet Protocol version 4</li>
        <li>IPv6 – Internet Protocol version 6</li>
        <li>ICMP – Internet Control Message Protocol</li>
        <li>IGMP – Internet Group Management Protocol</li>
        <li>ARP – Address Resolution Protocol</li>
        <li>RARP – Reverse Address Resolution Protocol</li>
        <li>IPsec – IP Security</li>
        <li>RIP – Routing Information Protocol</li>
        <li>OSPF – Open Shortest Path First</li>
        <li>BGP – Border Gateway Protocol</li>
      </ul>
    </div>

    <div class="layer link">
      <h2>1. Network Access (Link) Layer</h2>
      <ul>
        <li>Ethernet (IEEE 802.3)</li>
        <li>Wi-Fi (IEEE 802.11)</li>
        <li>PPP – Point-to-Point Protocol</li>
        <li>HDLC – High-Level Data Link Control</li>
        <li>Frame Relay</li>
        <li>ATM – Asynchronous Transfer Mode</li>
      </ul>
    </div>
  </div>
</body>
</html>
        """

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()