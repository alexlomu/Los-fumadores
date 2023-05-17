import threading
import time
import random

# Creamos los semáforos
ingredientes_semaforos = {
    'papel': threading.Semaphore(0),
    'tabaco': threading.Semaphore(0),
    'filtros': threading.Semaphore(0),
    'green': threading.Semaphore(0),
    'cerillas': threading.Semaphore(0)
}
puede_dejar_sem = threading.Semaphore(0)

# Función de los fumadores
def fumador(identificador, ingrediente_faltante):
    while True:
        ingredientes_semaforos[ingrediente_faltante].acquire()  
        print(f'Fumador {identificador} toma los ingredientes y comienza a fumar')
        time.sleep(2)  
        print(f'Fumador {identificador} ha terminado de fumar')
        puede_dejar_sem.release()  

# Función del agente
def agente():
    while True:
        ingredientes_dejados = random.sample(list(ingredientes_semaforos.keys()), 2)
        print('El agente deja en la mesa:', ingredientes_dejados)
        
        for ingrediente in ingredientes_dejados:
            ingredientes_semaforos[ingrediente].release()
        
        puede_dejar_sem.acquire()


# Creamos los hilos
fumador_1 = threading.Thread(target=fumador, args=(1, 'papel'))
fumador_2 = threading.Thread(target=fumador, args=(2, 'tabaco'))
fumador_3 = threading.Thread(target=fumador, args=(3, 'filtros'))
fumador_4 = threading.Thread(target=fumador, args=(4, 'green'))
fumador_5 = threading.Thread(target=fumador, args=(5, 'cerillas'))
agente_hilo = threading.Thread(target=agente)

# Iniciamos los hilos
fumador_1.start()
fumador_2.start()
fumador_3.start()
fumador_4.start()
fumador_5.start()
agente_hilo.start()


