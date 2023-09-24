import socket
import gc
import machine
# Crea un socket del servidor y configúralo
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 80))
s.listen(5)
led = machine.Pin(2, machine.Pin.OUT)
led.on()
print("Servidor web listo")

# Lee el contenido de "index.html" una vez durante la inicialización
with open("index.html", "r") as archivo:
    contenido_html = archivo.read()
def controlar_led(estado):
    led.value(estado)
def handle_request(conn):
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    #encabezado Content-Length que indica la longitud del contenido HTML que se enviará.
    conn.send('Content-Length: {}\n'.format(len(contenido_html)))
    conn.send('\n')
    request=conn.recv(1024)
    request=str(request)
    # Comprueba si la solicitud contiene "ON" o "OFF"
    if "/controlador?LED=ENCENDIDO" in request:
        controlar_led(0)
    elif "/controlador?LED=APAGADO" in request:
        controlar_led(1)
    conn.sendall(contenido_html)
    conn.close()

def runServer():
    print("Servidor iniciado...")
    while True:
        conn, addr = s.accept()
        print('Nueva solicitud desde %s' % str(addr))
        print(f"Memoria utilizada {gc.mem_alloc()/1024} kb")
        print(f"Memoria libre {gc.mem_free()/1024} kb")
        handle_request(conn)  # Llama a la función para manejar la solicitud


