# Addressable LED controller

* https://randomnerdtutorials.com/micropython-ws2812b-addressable-rgb-leds-neopixel-esp32-esp8266/
* https://www.thegeekpub.com/16187/controlling-ws2812b-leds-with-a-raspberry-pi/

# MySQL preparations

## Create ciew table

```mysql
CREATE OR REPLACE VIEW budapest_statuses_view as
SELECT worksheets.container,work_status.name, work_status.id,worksheets.updated_at
FROM worksheets, work_status
WHERE worksheets.work_state_id = work_status.id
    AND worksheets.container NOT IN ('', 0)
    AND worksheets.service_station = 1
    AND worksheets.work_state_id in (4, 11)
```

## Set permissions

* Generate strong password:
```shell
pwgen -n 25 -n -y -s 1
```
* Create user - update password
```mysql
CREATE USER 'query_status'@'%' IDENTIFIED BY '<supersecure pass>'
    WITH MAX_QUERIES_PER_HOUR 4000
    MAX_UPDATES_PER_HOUR 0
    MAX_CONNECTIONS_PER_HOUR 50
    MAX_USER_CONNECTIONS 10;
```
* Grant permission
```mysql
GRANT select on weloveapple.budapest_statuses_view to 'query_status'@'%';
GRANT select on weloveapple.worksheets to 'query_status'@'%';
```

## Install

### Ubuntu

*sudo apt-get install python3-pip python3-pyaudio
*pip3 install -r requirements.txt

### Raspberry Pi

* sudo pip3 install python3-pip rpi_ws281x adafruit-circuitpython-neopixel
* pip3 install -r requirements.txt

##  Config
By default `budapest_statuses_view` DB table is used to fetch data.
It can be overritten by setting the following environment variable

```shell
set DBTABLE=<other DB>
```

By default it uses the GPIO port `5`. It can be changed like this: 

```shell
set GPIO=<other GPIO>
```

##  Run

```shell
cd led_control
python3 main.py
```
