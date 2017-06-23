import objectbox.customlib.matlab as matlab
from IceOBImp.objectbox.base.ob_base_iceimp import OBElementI
import win32com.client
import pythoncom
import OBBase.server_state
import IceOBUtil.proxyUtil as prxutil
import IceOBUtil.servantUtil as svtutil

class OBMatlabI(matlab.OBMatlab, OBElementI):
    def __init__(self, name=''):
        apply(OBElementI.__init__,(self,),{})
        self._name = name
        self._type = 'OBMatlab'
        self.version = "Matlab.Application.7.13"
        self.version = "Matlab.Desktop.Application.7.13"
        self._comObj = None

    def __str__(self):
        return apply(OBElementI.__str__, (self,))

    def open(self, current=None):
        pythoncom.CoInitialize()
        self._comObj = win32com.client.Dispatch(self.version)

    def close(self, current=None):
        self._comObj = None

    def executeCommand(self, command, current=None):
        self._comObj.Execute(command)

svtutil.updateServantFactory('OBMatlab',OBMatlabI)
prxutil.updatePrxFactory('OBMatlab', matlab.OBMatlabPrx.uncheckedCast)



