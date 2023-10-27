import network
import webrepl
import server

sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("nombre_de_red","contra")
sta_if.isconnected()

# Configura una nueva contraseña para WebREPL
webrepl.start(password="123456")

server.runServer()
