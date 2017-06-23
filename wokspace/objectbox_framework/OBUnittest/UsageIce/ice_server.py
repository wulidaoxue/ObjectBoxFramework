import Ice
import sys
import IceOBImp.objectbox.base.ob_base_iceimp as IceBaseImp
import IceOBImp.objectbox.customlib.matlab.ob_matlab_iceimp as matlab
import OBBase.server_state as gbss
import logging
obLogger = logging.getLogger('ObjectBox.ice_server')

class Server(Ice.Application):
    def run(self, args):
        communicator = self.communicator()
        gbss.FrameWorkAdapter = communicator.createObjectAdapter("Server")
        gbss.FrameWorkAdapter.activate()
        sl = IceBaseImp.OBElementDefaultServantLocator()
        gbss.FrameWorkAdapter.addServantLocator(sl, 'OBElement');

        gbss.OBCenter = IceBaseImp.OBCenterI()

        gbss.OBCenter.createOBElement('GlobalVariableBox','OBContainer')
        gbss.OBCenter.createOBElement('Matlab','OBMatlab')
        gbss.OBCenter.createOBElement('PythonRunner','OBPythonRunner')

        OBCenterPrx = gbss.AddOBElementToFrameWorkAdapter(gbss.OBCenter)

        obLogger.info('over...')
        self.communicator().waitForShutdown()
        return 0

app = Server()
sys.exit(app.main(sys.argv, r"config.server"))




