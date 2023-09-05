# Instalación

Raspberry Pi OS 64

pi/ParqueCiencias55

## ssh y VNC

## Actualización


```sh
sudo apt update
sudo apt full-upgrade
sudo apt autoclean
sudo apt autoremove
```

Cambiamos el idioma y la configuración de teclado   


## Software

### MQTT broker - mosquitto

```sh
sudo apt install mosquitto mosquitto-clients
```

Editamos la configuracion __/etc/mosquitto/mosquitto.conf__

```sh
port 1883

allow_anonymous true
```

(http://www.steves-internet-guide.com/mossquitto-conf-file/)

#### test

```sh
mosquitto_sub -t "#" -v


# (desde otra maquina)

mosquitto_pub -h raspiIOT -t '/test' -m 'hola'
```

# micro:bit

Emparejamos micro:bit

[Programa IOT]https://makecode.microbit.org/_6FhDDqfjR7Xr)

```
Luz - 1
TMP - 2
LED - 16
```

Cada uno tiene que cambiar su número en el nombre de su microbit

## node-red

instalacion

```sh 
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
```

Activamos como servicio

```sh
sudo systemctl enable nodered.service
````

Arrancamos

```sh
sudo systemctl start nodered.service
````

Accedemos desde un navegador

```
http://raspiIOT:1880
```

# Flujo

* Damos de alta el servidor MQTT
* Añadimos la paleta de influxDB
* Damos de alta el servidor InfluxDB

![](./images/instalacion/flujo_IOTbit_.png)

## influxDB

```sh
sudo apt install influxdb influxdb-clients
influxdb

>> create database IOTPC
```

# Grafana

## instalacion grafana

```sh
curl https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/grafana-archive-keyrings.gpg >/dev/null

echo "deb [signed-by=/usr/share/keyrings/grafana-archive-keyrings.gpg] https://apt.grafana.com stable main" | sudo tee /etc/apt/sources.list.d/grafana.list

sudo apt update 

sudo apt install grafana

## admin/ParqueCiencias55

sudo systemctl enable grafana-server.service

sudo systemctl start grafana-server.service
```

## Configuración de vistas


* add influxdb como Datasource

* Add dashboard y select measurement

sudo /bin/systemctl enable grafana-server

sudo /bin/systemctl start grafana-server




