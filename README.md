# Los-fumadores

Este es el link del repositorio: [Github](https://github.com/alexlomu/Los-fumadores)

Nos pedían resolver el siguiente problema:

El caso de los fumadores consiste en un grupo de fumadores que para fumar necesitan los ingredientes que les faltan para hacer un cigarrillo y fumárselo, poseen un ingrediente en cantidades ilimitadas pero les faltan otros cuatro.

El agente posee cantidades ilimitadas de todos los ingredientes que son papel, tabaco, filtros, green y cerillas pero solo deja en una mesa dos de estos ingredientes a la vez. Cada fumador posee un ingrediente distinto de los cinco necesarios y según los ingredientes que deje el agente uno de los fumadores podrá fumar con los cuatro ingredientes que el agente deja.

El agente y los fumadores representan en la realidad a procesos y los ingredientes a los recursos de un sistema. La dificultad radica en sincronizar los agentes y fumadores para que el agente cuando deje ingredientes en la mesa el fumador correcto fume.

A primera vista podríamos intentar que cada uno de los fumadores tomase cada uno de los ingredientes que le falta y se pusiese a fumar representando un ingrediente como un semáforo, sin embargo, esta solución puede producir un bloqueo si uno de los otros fumadores que no pueden fumar según los ingredientes que ha dejado el agente le quitan al que podría fumar uno de los ingredientes que necesita. Por ejemplo, un caso de bloqueo sería el caso de que el agente deje en la mesa los ingredientes de tabaco y cerillas el fumador que podría fumar sería el 1 pero si el fumador 2 es más rápido y se ejecuta antes tomando el tabaco el fumador 1 se quedaría esperando a tomar tabaco y el fumador 2 también por no haber dejado el agente papel sino cerillas.

Código propuesto:

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
    
 Output recibido:
 
    El agente deja en la mesa: ['cerillas', 'papel']
    Fumador 5 toma los ingredientes y comienza a fumarFumador 1 toma los ingredientes y comienza a fumar

    Fumador 5 ha terminado de fumarFumador 1 ha terminado de fumar

    El agente deja en la mesa: ['green', 'papel']
    El agente deja en la mesa:Fumador 4 toma los ingredientes y comienza a fumarFumador 1 toma los ingredientes y comienza a fumar

    ['filtros', 'cerillas']
    Fumador 3 toma los ingredientes y comienza a fumarFumador 5 toma los ingredientes y comienza a fumar

    Fumador 3 ha terminado de fumarFumador 4 ha terminado de fumarFumador 5 ha terminado de fumarFumador 1 ha terminado de fumar



    El agente deja en la mesa: ['green', 'cerillas']
    El agente deja en la mesa:Fumador 4 toma los ingredientes y comienza a fumarFumador 5 toma los ingredientes y comienza a fumar

    ['filtros', 'cerillas']
    El agente deja en la mesa: Fumador 3 toma los ingredientes y comienza a fumar['cerillas', 'tabaco']

    El agente deja en la mesa:Fumador 2 toma los ingredientes y comienza a fumar
    ['filtros', 'cerillas']
    Fumador 4 ha terminado de fumarFumador 2 ha terminado de fumarFumador 5 ha terminado de fumarFumador 3 ha terminado de fumar



    El agente deja en la mesa:Fumador 5 toma los ingredientes y comienza a fumarFumador 3 toma los ingredientes y comienza a fumar

    ['cerillas', 'green']
    El agente deja en la mesa:Fumador 4 toma los ingredientes y comienza a fumar
    ['tabaco', 'filtros']
    El agente deja en la mesa:Fumador 2 toma los ingredientes y comienza a fumar
    ['cerillas', 'green']
    El agente deja en la mesa: ['filtros', 'green']
    Fumador 3 ha terminado de fumarFumador 5 ha terminado de fumarFumador 2 ha terminado de fumarFumador 4 ha terminado de fumar
    .
    .
    .
