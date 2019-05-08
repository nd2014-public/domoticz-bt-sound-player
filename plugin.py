#           Fronius Inverter Plugin
#
#           Author:     ADJ, 2018
#
# http://denvycom.com/blog/playing-audio-over-bluetooth-on-rasbperry-pi-command-line/
# https://www.domoticz.com/wiki/BTAudio
"""
<plugin key="BlutetoothSoundPlayer" name="Blutetooth Sound Player" author="MSALLES" version="0.0.1" wikilink="https://github.com/nd2014public/domoticz-bluetooth-soundplayer-plugin.git" externallink="http://www.fronius.com">
    <params>
        <param field="Mode1" label="Mac adresse device 1" required="true" width="200px" />
        <param field="Mode2" label="Mac adresse device 2" required="false" width="200px" />
        <param field="Mode3" label="Mac adresse device 3" required="false" width="200px" />
        <param field="Mode4" label="Mac adresse device 4" required="false" width="200px" />
        <param field="Mode6" label="Debug" width="100px">
            <options>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal" default="true" />
                <option label="Logging" value="File"/>
            </options>
        </param>
    </params>
</plugin>
"""
import Domoticz
import sys
import json
import datetime
import urllib.request
import urllib.error
import subprocess
import os 

class BasePlugin:

    def onStart(self):
        if Parameters["Mode6"] != "Normal":
            Domoticz.Debugging(1)

        if (len(Devices) == 0):
            Domoticz.Device(Name="Speaker 1",  Unit=1, TypeName="Selector Switch", Options = { "LevelActions": "||", "LevelNames": "Off|Test|Intrusion", "LevelOffHidden": "false", "SelectorStyle": "1" }).Create()

            # if (Parameters["Mode2"] is not None)
            #     Domoticz.Device(Name="Speaker 2",  Unit=2, TypeName="Selector Switch", Options = { "LevelActions": "|||", "LevelNames": "Off|Test|Intrusion", "LevelOffHidden": "false", "SelectorStyle": "1" }).Create()

            # if (Parameters["Mode3"] is not None)
            #     Domoticz.Device(Name="Speaker 3",  Unit=3, TypeName="Selector Switch", Options = { "LevelActions": "|||", "LevelNames": "Off|Test|Intrusion", "LevelOffHidden": "false", "SelectorStyle": "1" }).Create()

            # if (Parameters["Mode4"] is not None)
            #     Domoticz.Device(Name="Speaker 4",  Unit=4, TypeName="Selector Switch", Options = { "LevelActions": "|||", "LevelNames": "Off|Test|Intrusion", "LevelOffHidden": "false", "SelectorStyle": "1" }).Create()

            logDebugMessage("Devices created.")

        # Domoticz.Heartbeat()
        
        # if ('BlutetoothSoundPlayer' not in Images): Domoticz.Image('Fronius Inverter Icons.zip').Create()

        # Devices[1].Update(0, sValue=Devices[1].sValue, Image=Images["BlutetoothSoundPlayer"].ID)
        # Devices[2].Update(0, sValue=Devices[2].sValue, Image=Images["BlutetoothSoundPlayer"].ID)
        # Devices[3].Update(0, sValue=Devices[3].sValue, Image=Images["BlutetoothSoundPlayer"].ID)
        # Devices[4].Update(0, sValue=Devices[4].sValue, Image=Images["BlutetoothSoundPlayer"].ID)
        return True

    def onCommand(self, Unit, Command, Level, Color):

        logDebugMessage("Devices modified" )
        logDebugMessage(str(Unit))
        logDebugMessage(str(Command))
        logDebugMessage(str(Level))
        logDebugMessage(str(Color))
        dir_path = os.path.dirname(os.path.realpath(__file__))

        param1 = "-D bluealsa:HCI=hci0,DEV=%s,PROFILE=a2dp"
        param2 = dir_path + "/sounds/%s.wav"


        if (Command == 'Set Level' and Level == 10):
            logDebugMessage("Launch " + "aplay " + param1 % (Parameters["Mode"+str(Unit)]) + " " + param2 % ("test"))
            os.system("aplay " + param1 % (Parameters["Mode"+str(Unit)]) + " " + param2 % ("test") + " &")

        if (Command == 'Set Level' and Level == 20):
            logDebugMessage("Launch " + "aplay " + param1 % (Parameters["Mode"+str(Unit)]) + " " + param2 % ("intrusion_fr"))
            os.system("aplay " + param1 % (Parameters["Mode"+str(Unit)]) + " " + param2 % ("intrusion_fr") + " &")

        
        return True

    def onHeartbeat(self):
        return True

    def logErrorCode(self, jsonObject):

        code = jsonObject["Head"]["Status"]["Code"]
        reason = jsonObject["Head"]["Status"]["Reason"]
        if (code != 12):
            logErrorMessage("Code: " + str(code) + ", reason: " + reason)

        return

    def onStop(self):
        logDebugMessage("onStop called")
        return True

global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onStop():
    global _plugin
    _plugin.onStop()

def onDisconnect(Connection):
    global _plugin
    _plugin.onDisconnect(Connection)

def onCommand(Unit, Command, Level, Color):
    global _plugin
    _plugin.onCommand(Unit, Command, Level, Color)

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

def logDebugMessage(message):
    if (Parameters["Mode6"] == "Debug"):
        now = datetime.datetime.now()
        f = open(Parameters["HomeFolder"] + "soundplayer-bluetooth-plugin.log", "a")
        f.write("DEBUG - " + now.isoformat() + " - " + message + "\r\n")
        f.close()
    Domoticz.Debug(message)

def logErrorMessage(message):
    if (Parameters["Mode6"] == "Debug"):
        now = datetime.datetime.now()
        f = open(Parameters["HomeFolder"] + "soundplayer-bluetooth-plugin.log", "a")
        f.write("ERROR - " + now.isoformat() + " - " + message + "\r\n")
        f.close()
    Domoticz.Error(message)
