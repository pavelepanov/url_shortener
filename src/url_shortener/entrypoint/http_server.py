import asyncio
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from logging import (DEBUG, FileHandler, StreamHandler, basicConfig, getLogger,
                     info)
from urllib.parse import parse_qs, urlparse

from url_shortener.application.contracts.url.requests import (
    CreateShortUrlRequest, GetFullUrlByShortUrlRequest)
from url_shortener.entrypoint.ioc import IoC
from url_shortener.infrastructure.adapters.short_url_id_generator_uuid import \
    UUIDShortUrlGenerator
from url_shortener.infrastructure.config import DomainUrl
from url_shortener.presentation.web_api.create_short_url import \
    create_short_url
from url_shortener.presentation.web_api.get_full_url_by_short_url import \
    get_full_url_by_short_url

logger = getLogger(__name__)

DictionaryDatabase = dict()


def configure_logging(level=DEBUG):
    format = '[%(asctime)s.%(msecs)03d] %(module)15s:%(lineno)-3d %(levelname)-7s - %(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'

    file_handler = FileHandler('logs.log')
    file_handler.setLevel(level)

    console_handler = StreamHandler()
    console_handler.setLevel(level)

    basicConfig(
        level=level,
        datefmt=datefmt,
        format=format,
        handlers=[file_handler, console_handler]
                        )


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.ioc = server.ioc
        super().__init__(request, client_address, server)

    def do_POST(self):
        try:
            url = urlparse(self.path)
            path = url.path

            if path == '/short_url':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()

                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                post_data_str = post_data.decode('utf-8')

                data = json.loads(post_data_str)

                response_presenation = asyncio.run(
                    create_short_url(
                        ioc=self.ioc, request=CreateShortUrlRequest(data['key'])
                    )
                )

                post_data_answer = {
                    'id': str(response_presenation.id),
                    'full_url': response_presenation.full_url,
                    'short_url': response_presenation.short_url,
                }

                response = {
                    'short_url': post_data_answer['short_url'],
                }

                self.wfile.write(json.dumps(response).encode("utf-8"))
            else:
                self.send_response(404)
                response = {
                    'error': 'Route not found',
                    'path': path
                }

                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            error_message = {'error': 'Internal Server Error', 'details': str(e)}
            self.wfile.write(json.dumps(error_message).encode('utf-8'))

    def do_GET(self):
        try:
            url = urlparse(self.path)
            path = url.path

            if path == '/short_url':
                query_params = parse_qs(url.query)
                response_presenation = asyncio.run(
                    get_full_url_by_short_url(
                        ioc=self.ioc,
                        request=GetFullUrlByShortUrlRequest(query_params['full_url'][0]),
                    )
                )

                response = {
                    'full_url': response_presenation.full_url,
                }

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))
            else:
                self.send_response(404)
                response = {
                    'error': 'Route not found',
                    'path': path
                }

                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode('utf-8'))

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            error_message = {'error': 'Internal Server Error', 'details': str(e)}
            self.wfile.write(json.dumps(error_message).encode('utf-8'))


class HTTPServerWithIoc(HTTPServer):
    def __init__(self, server_address, RequestHandlerClass, ioc: IoC):
        super().__init__(server_address, RequestHandlerClass)
        self.ioc = ioc


def get_http_server(server_class, handler_class, port, ioc):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class, ioc)
    print(f'Starting http server on {port}...')
    return httpd


def create_app(
    domain_url: DomainUrl, database: dict, id_generator_short_url, port: int = 8080
):
    ioc = IoC(
        domain_url=domain_url,
        database=database,
        id_generator_short_url=id_generator_short_url,
    )

    http_server = get_http_server(
        server_class=HTTPServerWithIoc,
        handler_class=HTTPRequestHandler,
        port=port,
        ioc=ioc,
    )

    configure_logging()

    info('Create application')

    return http_server


app = create_app(
    domain_url=DomainUrl.from_env(),
    database=DictionaryDatabase,
    id_generator_short_url=UUIDShortUrlGenerator(),
)
app.serve_forever()
