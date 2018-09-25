import argparse
import asyncio
import aiohttp
from demo import create_app
from demo.settings import load_config

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print('uvloop is not available')


parser = argparse.ArgumentParser(description='Demo project')
parser.add_argument('--host', help='host to listen', default='0.0.0.0')
parser.add_argument('--port', help='port to accept connecttions', default=5000)
parser.add_argument('--reload', action='store_true', help='autoreload code on change')
parser.add_argument('-c', '--config', type=argparse.FileType('r'),
                    help='Path to conf file')

args = parser.parse_args()

app = create_app(config=load_config(args.config))

if args.reload:
    print('start with code reload')

if __name__ == '__main__':
    aiohttp.web.run_app(app, host=args.host, port=args.port)


