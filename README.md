# ESP32 MicroPython

### Development Setup
```bash
$ pip3 install virtualenv --user
$ virtualenv venv
$ venv/Scripts/activate
$ pip install -r requirements.txt    
``` 

### Installing libraries
```bash
$ import boot
$ connect()
$ import upip
$ upip.install("micropython-umqtt.simple")
```