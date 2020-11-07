import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# Event logger
class Event(LoggingEventHandler):
    def on_created(self, event):
        print("created", event)
    def on_deleted(self, event):
        print("Deleted", event)
    def on_modified(self, event):
        print("Modified", event)
    def on_moved(self,event):
        print("Renamed or Moved", event)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(path)
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