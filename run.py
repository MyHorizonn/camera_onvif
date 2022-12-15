from app import create_app
import sys
import signal

def signal_handler(sig, frame):
    print('Terminated')
    sys.exit(0)


if __name__ == '__main__':

    signal.signal(signal.SIGINT, signal_handler)
    
    host_info = {'host': '0.0.0.0', 'port': '8001', 'debug': True}
    _app = create_app()
    _app.run(**host_info)
