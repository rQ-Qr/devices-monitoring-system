import Adafruit_DHT as DHT

import paho.mqtt.client as mqtt
import time

import csv

server_address = "mqtt.thingspeak.com"
port = 1883

channel_id = '1358823'
write_api_key = 'V7KSGCGVD3VW7I9V'
topic = "channels/"+channel_id+"/publish/"+write_api_key
client = mqtt.Client()
client.connect(server_address, port)
sensor  = DHT.DHT22
pin = 27

with open('data.csv', 'w', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Time (s)', 'Temperature (C)', 'Humidity (%)'])
	
	counter = 0
	running_time = 0
	AC = False
	
	while counter <= 20:
		h, t = DHT.read_retry(sensor,pin)
		print("Temp: ",t)
		print("Humidity : ",h)
		
		if t > 32:
			data = "field1="+str(t)+"&field2="+str(h)
			client.publish(topic,data)
			if AC == False:
				AC = True
				print("Switching on AC")
				exec(open("SMS.py").read())
			print("Cloud Backup...")
		else: 
			if AC == True:
				AC = False
				print("Switching off AC")
	
		writer.writerow([running_time, t, h])
		time.sleep(15)
		
		counter += 1
		running_time += 15	
