from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ('', 80)  # Port 80 - HTTP; 20, 21 - FTP; 25565 - Minecraft;

httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

print('start')
httpd.serve_forever()
print('stop')

# HTTPS - Hypertext Transfer Protocol Secured
# HTTP - Hypertext Transfer Protocol
# HTML - Hypertext markup language