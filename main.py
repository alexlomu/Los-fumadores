import threading
import time
import random

# Creamos los semáforos
ingredientes_sem = {
    'papel': threading.Semaphore(0),
    'tabaco': threading.Semaphore(0),
    'filtros': threading.Semaphore(0),
    'green': threading.Semaphore(0),
    'cerillas': threading.Semaphore(0)
}

puede_dejar_sem = threading.Semaphore(0)

