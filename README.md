# ServidorWeb_ESP8266
https://docs.micropython.org/en/v1.20.0/esp8266/tutorial/intro.html#intro

1.pip install esptool

2.conocer puerto com que se le asigno a la placa (conectar esp8266)

	-esptool.py --port COM3 erase_flash  
 
3.insatalar firmware primero ir a la carpeta donde este el bin

	NOTA: para que la consola se vea  usar baud rate 115200, usar putty o tera term
	ultima version:
	esptool.py --port COM3 --baud 115200  write_flash --flash_size=detect 0 ESP8266_GENERIC-20230426-v1.20.0.bin
	penultima version:
	esptool.py --port COM3 --baud 115200  write_flash --flash_size=detect 0 ESP8266_GENERIC-20220618-v1.19.1.bin
(La placa ya deberia soportar micropython)

4.descargar editor Mu o usar ampy (pip install adafruit-ampy) para cargar scripts

	con ampy:
		ampy --help
		ampy -p <puerto_serial> put mi_codigo.py
		ampy --port COM4 run holaMundo.py
	modificar archivo boot 
		ampy --port COMx get boot.py > boot.py 
		NOTA: para que el programa se ejecute al principio poner codigo en main.py
			presionar rst 
		NOTA: cada que se hagan cambios usar put

		NOTA: si se quiere usar la consola para controlar el chip 
			usar help(modulo) para ver los metodos dentro
		NOTA: usar TAB para ver modulos importados en un principio (funcion autocompletar) tambien funciona como help
		NOTA: para funciones relacionadas con redes usar import network o help() para ver configuraciones comunes
		NOTA: machine.reset() para restablecer	
----------------------------------------------------------------------------------------------------

SERVIDOR WEB

Para crear un servidor WEB es necesario crear un socket para ello server.py 
agregarlo con ampy usando put junto con el html.

En la consola de micropython conectarse primero a la red y luego importar el modulo server

Para acceder remotamente mediante el navegador  al a consola usar "import webrepl_setup" y seguir intrucciones o "import webrepl" si
se quiere configurar en el script 


NOTA: Es posible que por los recursos limitados del esp8266 solo pueda acceder un cliente a la vez
recargar pagina constantemente


-----------------------------------------------------------------------------------------------------
NOTA utilizar .mpy antes que .py 

los archivos .mpy son mas ligeros y se ejecutan mas rapido que los .py

mpy-cross archivo.py (genera un .mpy)
