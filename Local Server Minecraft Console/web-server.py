from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ('', 2000)

httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

print('start')
httpd.serve_forever()
print('stop')