import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/raulg/Desktop/BYJU'S/proyecto 103 prueba"

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Oye, {event.src_path} ha sido creado.")

    def on_deleted(self, event):
        print(f"Oye, {event.src_path} ha sido eliminado.")

    def on_modified(self, event):
        print(f"Oye, {event.src_path} ha sido modificado.")

    def on_moved(self, event):
        print(f"Oye, {event.src_path} ha sido movido.")


# Inicia la clase event handler
event_handler = FileMovementHandler()

# Inicializa Observer
observer = Observer()

# Programa Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicia Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("ejecutando...")
except KeyboardInterrupt:
    print("¡detenido!")
    observer.stop()