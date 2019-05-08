# domoticz-bt-sound-player
Domoticz Bluetooth Sound Player
--------------------------------


Installation
------------

In your `domoticz/plugins` directory do

```bash
git clone https://github.com/nd2014-public/domoticz-bt-sound-player.git
```

Restart your Domoticz service with:

```bash
sudo service domoticz.sh restart
```

Now go to **Setup**, **Hardware** in Domoticz. There you add
**Sound Player**.

Fill devices Mac address of your bluetooth sound devices.


Install bluealsa and aplay

```bash
DOCUMENTION TO COME
```



Prerequisites
-------------

- Install bluealsa
- Connect to bluetooth sound device
- Check installation with aplay


Features to add
---------------

- Automatically connect to devices before playing sounds
- Auto detect sound devices by trying to connect/pair with all BT devices scanned



Licensed by 
<a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">
CC 3.0 BY</a>
