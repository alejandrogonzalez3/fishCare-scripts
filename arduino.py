import serial

arduino = serial.Serial('/dev/ttyACM0', 115200)

print("Starting!")

while True:
      # comando = input('Introduce un comando: ') #Input
      # arduino.write(comando.encode()) #Mandar un comando hacia Arduino
      # if comando == 'H':
      #       print('LED ENCENDIDO')
      # elif comando == 'L':
      #      print('LED APAGADO')
            
      if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').rstrip()
            print(line)

arduino.close() #Finalizamos la comunicacion
