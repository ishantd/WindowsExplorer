import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import os
import requests

os.environ['NO_PROXY'] = '127.0.0.1'

# Event logger
class Event(LoggingEventHandler):
    def on_created(self, event):
        url = 'http://127.0.0.1:8000/created/'
        data = {'event': event}
        r = requests.post(url, data=data)
    def on_deleted(self, event):
        url = 'http://127.0.0.1:8000/deleted/'
        data = {'event': event}
        r = requests.post(url, data=data)
    def on_modified(self, event):
        url = 'http://127.0.0.1:8000/modified/'
        data = {'event': event}
        r = requests.post(url, data=data)
    def on_moved(self,event):
        url = 'http://127.0.0.1:8000/moved/'
        data = {'event': event}
        r = requests.post(url, data=data)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = '/home/ishant/Downloads/new'
    event_handler = Event()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()